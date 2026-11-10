"""Rebuild the standalone Plummer chart (requires numpy, Pillow, matplotlib)."""
from pathlib import Path
import csv
import math
import os
os.environ.setdefault('MPLCONFIGDIR', str(Path(__file__).resolve().parents[1] / 'tmp/matplotlib-cache'))
import numpy as np
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[1]
G = 9.80665
ARMATURE_KG = 0.77
PAYLOAD_KG = 0.50
FORCE_N = 1000.0
VELOCITY_M_S = 1.65
STIFFNESS_KGF_MM = 3.04

def envelope(frequency, adapter_kg):
    added_mass = adapter_kg + PAYLOAD_KG
    moving_mass = added_mass + ARMATURE_KG
    stroke_m = (12.7 - 2 * added_mass / STIFFNESS_KGF_MM) / 1000
    omega = 2 * np.pi * np.asarray(frequency, dtype=float)
    return np.minimum.reduce([
        omega ** 2 * stroke_m / 2,
        omega * VELOCITY_M_S,
        np.full_like(omega, FORCE_N / moving_mass),
        np.full_like(omega, 100 * G),
    ]) / G

def build():
    image = Image.open(ROOT / 'scripts/assets/gw-v100-sine-envelope.png').convert('RGB')
    assert image.size == (1070, 705)
    header, height = 100, 725
    fig = plt.figure(figsize=(10.70, height / 100), dpi=200, facecolor='white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, 1070), ylim=(height, 0))
    ax.axis('off')
    ax.imshow(image, extent=[0, 1070, header + 705, header], interpolation='none', zorder=0)
    ax.add_patch(Rectangle((0, header), 1070, 28, facecolor='white', edgecolor='none', zorder=1))
    ax.plot([226, 271], [header + 14] * 2, color='#231f20', lw=2.6, zorder=2)
    ax.text(283, header + 14, 'Unloaded shaker', fontsize=11, va='center', color='#231f20', zorder=2)
    ax.plot([667, 712], [header + 14] * 2, color='#2ea8d1', lw=2.6, zorder=2)
    ax.text(724, header + 14, '10 kg added load', fontsize=11, va='center', color='#231f20', zorder=2)
    ax.text(42, 23, 'Adapter mass and acceleration capacity', fontsize=15, weight='bold', va='center', color='#20262d')
    frequency = np.geomspace(5, 2000, 2400)
    for i, (mass, color, label) in enumerate([
        (3.19, '#D46A00', 'Original adapter: 3.19 kg'),
        (1.90, '#9C27B0', 'Optimized adapter: 1.90 kg'),
    ]):
        y = 51 + 25 * i
        ax.plot([45, 100], [y, y], color=color, lw=2.6)
        ax.text(112, y, label, fontsize=11.5, va='center', color=color)
        acceleration = envelope(frequency, mass)
        x = 145 + (991 - 145) * np.log10(frequency) / 4
        y_curve = header + 537 - (537 - 62) * (np.log10(acceleration) + 1) / 4
        line, = ax.plot(x, y_curve, color=color, lw=2.15, zorder=3, solid_joinstyle='round')
        line.set_clip_path(Rectangle((145, header + 62), 991 - 145, 537 - 62, transform=ax.transData))
        plateau = FORCE_N / (mass + PAYLOAD_KG + ARMATURE_KG) / G
        y_plateau = header + 537 - (537 - 62) * (math.log10(plateau) + 1) / 4
        ax.text(858, y_plateau, f'{plateau:.1f} g', fontsize=10.5, weight='bold', color=color, va='center',
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .88, 'pad': 1.2}, zorder=4)
    output = ROOT / 'public/Pictures/Plummer/Shaker-Acceleration-Envelope.webp'
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.canvas.draw()
    rendered = Image.fromarray(np.asarray(fig.canvas.buffer_rgba())).convert('RGB')
    rendered.save(output, 'WEBP', lossless=True)
    plt.close(fig)
    data = ROOT / 'public/Reports/Shaker_Acceleration_Comparison.csv'
    with data.open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['frequency_Hz', 'original_peak_acceleration_g', 'optimized_peak_acceleration_g'])
        writer.writerows(zip(frequency, envelope(frequency, 3.19), envelope(frequency, 1.90)))
    print(f'Created {output.name}: {rendered.width} x {rendered.height}; {output.stat().st_size:,} bytes')

if __name__ == '__main__':
    build()
