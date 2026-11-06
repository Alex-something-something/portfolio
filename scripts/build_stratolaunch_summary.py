"""Build the focused Stratolaunch internship project summary and editable text."""
from pathlib import Path
from io import BytesIO
from html import escape
import shutil

from PIL import Image as PILImage
from pypdf import PdfReader
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
TEXT = ROOT / 'output/application'
OUT.mkdir(parents=True, exist_ok=True)
TEXT.mkdir(parents=True, exist_ok=True)
PDF = OUT / 'Alexander_Tong_Stratolaunch_Project_Summary.pdf'
FONTS = Path('C:/Windows/Fonts')
for name, filename in [('Arial', 'arial.ttf'), ('ArialBold', 'arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONTS / filename)))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='ArialBold')
INK = HexColor('#172331')
MUTED = HexColor('#526171')
ACCENT = HexColor('#963446')
RULE = HexColor('#d6dce2')
STYLES = {
    'title': ParagraphStyle('title', fontName='ArialBold', fontSize=22, leading=26, textColor=INK, spaceAfter=6),
    'name': ParagraphStyle('name', fontName='ArialBold', fontSize=11, leading=14, textColor=INK, spaceAfter=3),
    'meta': ParagraphStyle('meta', fontName='Arial', fontSize=9, leading=12.4, textColor=MUTED, spaceAfter=4),
    'body': ParagraphStyle('body', fontName='Arial', fontSize=10.4, leading=14.2, textColor=INK, spaceAfter=8),
    'heading': ParagraphStyle('heading', fontName='ArialBold', fontSize=11.5, leading=15, textColor=INK, spaceBefore=8, spaceAfter=5, keepWithNext=True),
    'caption': ParagraphStyle('caption', fontName='Arial', fontSize=8.5, leading=11.5, textColor=MUTED, spaceAfter=4),
    'eyebrow': ParagraphStyle('eyebrow', fontName='ArialBold', fontSize=8.3, leading=11, textColor=ACCENT, spaceAfter=7),
}

PAGES = [
    [
        ('heading', 'Project and individual responsibility'),
        ('body', "I co-lead separation and recovery development for Argo, Boston University Rocket Propulsion Group's 135 lb dry-mass liquid bipropellant rocket targeting 100,000 ft. Its inherited dual-break, dual-deploy architecture calls for drogue deployment near apogee and main release at 2,000 ft above ground. I develop hardware within that architecture through load analysis, CAD, drawings, machining, integration, and test operations. Flight performance remains unverified."),
        ('heading', 'Engineering evidence'),
        ('body', "Recovery sizing: I compared 23 commercial parachute candidates and five published load-estimation methods. Calculated opening and snatch loads of 823 and 1,230 lbf guided hardware selection and 6,000 lbf nominal-rated Kevlar line selection. The earlier black-powder configuration was 18.7 lbm against a 20 lbm allocation, with a $1,076 bill of materials; these figures do not describe the current CO2 configuration."),
        ('body', "Manufactured hardware: I redesigned the Catclaw cable-cutter body, produced its drawing, and machined it on a manual mill and lathe. Mass fell 49.5% from the earlier design, with a calculated body factor of safety (FOS) of 2.01. The selected configuration broke the restraint in eight of eight recorded trials. I also introduced Brummel eye splices; a dynamic test reached an estimated 1,800 lbf, approximately 1.46 times the calculated snatch load, with no observed slip. This was a proof test, not an ultimate-strength measurement."),
        ('body', "CO2 redesign: I proposed the cartridge-piercing replacement after integrated vinyl-charge failures. I sized it using pressure and Lamé thick-wall stress calculations, then contributed Fusion 360 CAD, drawings, machining, and component tests in a three-person team. Calculated housing margins were 2.01 FOS in hoop stress and 6.31 against internal-thread shear. Design and fabrication were shared; my co-lead developed pressure acquisition and analyzed the data."),
        ('heading', 'Why I chose the project'),
        ('body', "I sought recovery work because it offered a full design cycle and direct tests of my decisions. I enjoy moving from a component's material behavior to its load path, manufacturing constraints, and effect on the complete system. Comparing real hardware with first-principles predictions, then tracing the differences, is what makes this work exciting to me."),
    ],
    [
        ('heading', 'Test execution and design decisions'),
        ('body', "I authored the integrated black-powder test standard operating procedure (SOP) and led the second integrated test, including crew briefings and fire or abort decisions. My co-lead led the first test. Inspection and failure assessment were collaborative. One of three deployment charges failed in each test; the second also damaged the parachute bag and canopy. Documented assembly procedures and a small set of successful standalone tests had not established reliability in the packed subsystem."),
        ('body', "I helped operate reduced-pressure CO2 component trials, including a firing at a reported initial chamber pressure of 0.011 atm. The subsequent integrated CO2 test partially failed; our team attributed the failure to inadequately sealed wiring openings. We revised the feedthrough using an NPT fitting, a smaller opening, epoxy around the required redundant wiring, and supplemental vacuum putty. A retest is planned, with CO2 indicators under consideration for leakage assessment. The revised seal and full-system CO2 deployment are not yet verified."),
        ('heading', 'What changed in my engineering practice'),
        ('body', "I now document observations, assumptions, and hypotheses separately so the team can assess a design from the same evidence. Recovery also taught me to coordinate mechanical and electrical interfaces early, write clear test procedures, and look for redundancy at each stage. When the schedule allows, I am more willing to test an alternative to inherited hardware rather than rely on its earlier success in a different configuration."),
        ('heading', 'Why Stratolaunch'),
        ('body', "Stratolaunch's reusable Talon-A flight testing connects vehicle design and integration with the flight data needed to evaluate performance. That design-to-test responsibility is what I seek. My Argo aerocover work has expanded my interest in compressible flow and coupled thermal and structural constraints: I performed first-order drag trades and a converged Mach 2.81 Ansys Fluent baseline that remains under review. I want to apply my hardware and test experience while learning how those disciplines come together in hypersonic flight testing."),
        ('heading', 'Additional relevant experience'),
        ('body', "As a Mechanical Engineering Intern at BU's Plummer Laboratory, I performed SolidWorks dynamic FEA and CNC-machined shaker hardware on a Haas VF-2. In BU Space Physics and Technology Lab research, I wrote and assembled Python functions and used pySPEDAS for instrument-data analysis."),
    ],
]

def p(text, style='body'):
    return Paragraph(escape(text), STYLES[style])

def picture():
    im = PILImage.open(ROOT / 'public/Pictures/CO2/Manufactured-Piercer-Card.webp').convert('RGB')
    im.thumbnail((1100, 700))
    stream = BytesIO()
    im.save(stream, format='JPEG', quality=90, optimize=True)
    stream.seek(0)
    width = 223
    visual = Image(stream, width=width, height=width * im.height / im.width)
    caption = [p('CO2 deployment hardware', 'name'), p('Cartridge and piercer assembly from the shared three-person design and fabrication effort. This photograph shows the earlier hardware; the latest feedthrough revision is not pictured.', 'caption'), Spacer(1, 4), p('Calculated margins and component trials are distinct from integrated deployment verification.', 'caption')]
    table = Table([[visual, caption]], colWidths=[239, 289])
    table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'), ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),10), ('TOPPADDING',(0,0),(-1,-1),4), ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    return table

def footer(c, doc):
    c.saveState()
    c.setStrokeColor(RULE)
    c.setLineWidth(0.6)
    c.line(42, 38, 570, 38)
    c.setFillColor(MUTED)
    c.setFont('Arial', 8)
    c.drawString(42, 25, 'Alexander Tong | Stratolaunch Engineering Intern Summer 2027 | November 6, 2026')
    c.drawRightString(570, 25, f'{doc.page} / 2')
    c.restoreState()

story = [
    p('PROJECT SUMMARY FOR STRATOLAUNCH', 'eyebrow'),
    p('Argo Separation and Recovery', 'title'),
    p('Alexander Tong', 'name'),
    p('Boston University | B.S. Mechanical Engineering, Aerospace Concentration | Expected May 2028', 'meta'),
    Paragraph('<a href="mailto:alto335@bu.edu" color="#526171">alto335@bu.edu</a> | <a href="https://alexandertong.space" color="#526171">alexandertong.space</a> | Subsystem Co-Lead, June 2025-present', STYLES['meta']),
    Spacer(1, 3),
]
for index, blocks in enumerate(PAGES):
    if index:
        story.extend([PageBreak(), p('ARGO SEPARATION AND RECOVERY', 'eyebrow'), p('Testing and Engineering Judgment', 'title')])
    for style, text in blocks:
        story.append(p(text, style))
    if index == 0:
        story.extend([Spacer(1, 2), picture()])
    else:
        story.extend([Spacer(1, 4), p('Summer 2027 availability: June 1-August 27. Available for a 10-12-week onsite internship in Mojave.', 'meta')])

doc = SimpleDocTemplate(str(PDF), pagesize=(612, 792), leftMargin=42, rightMargin=42,
    topMargin=36, bottomMargin=49, title='Argo Separation and Recovery - Alexander Tong', author='Alexander Tong')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
reader = PdfReader(str(PDF))
if len(reader.pages) != 2:
    raise RuntimeError(f'Expected two pages; got {len(reader.pages)}')
plain = ['Argo Separation and Recovery', 'Alexander Tong', 'Project summary for Stratolaunch Engineering Intern Summer 2027', 'November 6, 2026', '']
for blocks in PAGES:
    for _, text in blocks:
        plain.extend([text, ''])
plain.extend(['Summer 2027 availability: June 1-August 27. Available for a 10-12-week onsite internship in Mojave.', ''])
(TEXT / 'Alexander_Tong_Stratolaunch_Project_Summary.txt').write_text('\n'.join(plain), encoding='utf-8')
application = ROOT / 'applications/stratolaunch-2027'
application.mkdir(parents=True, exist_ok=True)
shutil.copy2(PDF, application / PDF.name)
shutil.copy2(TEXT / 'Alexander_Tong_Stratolaunch_Project_Summary.txt', application / 'Project_Summary.txt')
print(f'Created {PDF} ({len(reader.pages)} pages, {PDF.stat().st_size:,} bytes)')
for i, page in enumerate(reader.pages, 1):
    print(f'Page {i}: {len(page.extract_text().split())} words')
