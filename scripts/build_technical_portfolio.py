"""Build the four-page technical portfolio. Run from any directory with Python/reportlab/Pillow/pypdf."""
from pathlib import Path
from io import BytesIO
import shutil
from PIL import Image as PILImage
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / 'Alexander_Tong_Technical_Portfolio.pdf'
FONT = Path('C:/Windows/Fonts')
for name, file in [('Body','arial.ttf'),('Bold','arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Body',boldItalic='Bold')
INK=HexColor('#172331'); MUTED=HexColor('#516171'); RED=HexColor('#ba2637'); LINE=HexColor('#d9dfe5'); LIGHT=HexColor('#f3f5f7')
styles={
 'body':ParagraphStyle('body',fontName='Body',fontSize=10,leading=13.4,textColor=INK,spaceAfter=6),
 'small':ParagraphStyle('small',fontName='Body',fontSize=8.4,leading=11.2,textColor=MUTED,spaceAfter=4),
 'caption':ParagraphStyle('caption',fontName='Body',fontSize=8,leading=10.5,textColor=MUTED,spaceAfter=0),
 'h1':ParagraphStyle('h1',fontName='Bold',fontSize=23,leading=27,textColor=INK,spaceAfter=4),
 'h2':ParagraphStyle('h2',fontName='Bold',fontSize=17,leading=21,textColor=INK,spaceAfter=5),
 'h3':ParagraphStyle('h3',fontName='Bold',fontSize=11,leading=14,textColor=INK,spaceBefore=7,spaceAfter=4),
 'label':ParagraphStyle('label',fontName='Bold',fontSize=8.5,leading=11,textColor=RED,spaceAfter=5),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=9,leading=11.5,textColor=INK),
 'metric':ParagraphStyle('metric',fontName='Bold',fontSize=17,leading=20,textColor=RED,spaceAfter=3),
}
def p(t,style='body'): return Paragraph(t,styles[style])
def bullet(t): return p('&#8226; '+t)
def link(route,label): return f'<a href="https://alexandertong.space/{route}" color="#ba2637"><u>{label}</u></a>'
def picture(path,w,h):
    im=PILImage.open(ROOT/'public'/path).convert('RGB')
    im.thumbnail((1600,1200))
    buf=BytesIO(); im.save(buf,format='JPEG',quality=85,optimize=True);buf.seek(0)
    return Image(buf,width=w,height=h,kind='proportional',hAlign='CENTER')
def metrics(items):
    cells=[[p(a,'metric'),p(b,'small')] for a,b in items]
    tab=Table([cells],colWidths=[180]*3,hAlign='LEFT')
    tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    return tab
def calc(rows):
    tab=Table([[p(a,'cell'),p(b,'cell')] for a,b in rows],colWidths=[155,385],hAlign='LEFT')
    tab.setStyle(TableStyle([('BACKGROUND',(0,0),(0,-1),LIGHT),('LINEBELOW',(0,0),(-1,-1),.5,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    return tab
styles['body'].fontSize=10
styles['body'].leading=13.4
styles['small'].leading=11.2
styles['cell'].fontSize=9
styles['cell'].leading=11.5
base_calc=calc
def calc(rows):
    tab=base_calc(rows)
    tab.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
    return tab

def photos(items,widths,height=151):
    cells=[]
    for (path,caption),w in zip(items,widths):
        image_cell=Table([[picture(path,w-10,height)]],colWidths=[w-10])
        image_cell.setStyle(TableStyle([
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('LEFTPADDING',(0,0),(-1,-1),0),
            ('RIGHTPADDING',(0,0),(-1,-1),0),
            ('TOPPADDING',(0,0),(-1,-1),0),
            ('BOTTOMPADDING',(0,0),(-1,-1),0),
        ]))
        cells.append([image_cell,Spacer(1,5),p(caption,'caption')])
    tab=Table([cells],colWidths=widths,hAlign='LEFT')
    tab.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),5),
        ('RIGHTPADDING',(0,0),(-1,-1),5),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),8),
    ]))
    return tab

styles['recovery-body']=ParagraphStyle('recovery-body',parent=styles['body'],spaceAfter=4)
styles['recovery-heading']=ParagraphStyle('recovery-heading',parent=styles['h3'],spaceBefore=5,spaceAfter=3)

def recovery_calc(rows):
    tab=calc(rows)
    tab.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    return tab

def project_index():
    entries = [
        [('plummer/','Plummer Laboratory','CNC-machined shaker adapter; plate-and-bolt hardware estimate reduced from $1,170 to $71.11, excluding labor. Designed the matrix and procedure for 48 Instron tests.'),('dbf/','AIAA Design-Build-Fly wing','Complete Prototype 1 wing 42.7% lighter than the previous complete wing; build time reduced from three months to one. Led design, fabrication and member training.')],
        [('project_nozzle/','Hybrid rocket nozzle','73% mass reduction from my initial design; approximately two-second hotfire. Minimum yield FOS 7.8 in SolidWorks FEA for mechanical loads only; thermal effects excluded. Thrust gain unmeasured.'),('robot/','EK210 line-following car','Designed and programmed the vehicle: six loaded course runs in 70-86 seconds against a 90-second limit. Recorded component cost $73.94 against a $200 budget.')],
        [('culturon/','Culturon','Executed the company\u2019s first full-scale nanoparticle deposition map using microscopy and ImageJ. Designed adhesive-free sample racks; presented prevention concepts.'),('manufacturing/','Manufacturing &amp; mentoring','CNC and manual machining, hot-wire foam cutting and composite fabrication. Taught BURPG members turning and milling through the machinist\u2019s-hammer project beginning Fall 2025.')],
    ]
    rows=[[[p(link(route,title),'h3'),p(detail)] for route,title,detail in row] for row in entries]
    tab=Table(rows,colWidths=[270,270],hAlign='LEFT')
    tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,-2),.5,LINE)]))
    return tab

def footer(c,d):
    c.saveState()
    c.setStrokeColor(LINE);c.setLineWidth(.6);c.line(36,35,576,35)
    c.setFillColor(MUTED);c.setFont('Body',8)
    c.drawString(36,23,'Alexander Tong | Technical portfolio | October 19, 2026')
    c.drawRightString(576,23,f'{d.page} / 4')
    c.restoreState()

story = [
 p('ALEXANDER TONG','h1'),
 p('Mechanical engineering | Recovery hardware and supersonic aerodynamics','body'),
 p('Boston University, B.S. Mechanical Engineering, Aerospace Concentration | Expected May 2028<br/>alto335@bu.edu | 860-706-3624 | '+link('','alexandertong.space'),'small'),Spacer(1,7),
 p('PORTFOLIO AT A GLANCE','label'),
 p('Project Index','h2'),
 calc([('Page 2 / Separation &amp; recovery',link('project_recovery/','Earlier black-powder configuration: 18.7 lbm within a 20 lbm allocation')+'. Load sizing, CO2 redesign and an operational vacuum chamber.'),('Page 3 / Aerodynamic fairing',link('project_aerocover/','Three concept studies; Ansys CFD baseline converged and under review')+'. Shared aerodynamic analysis, integration and manufacturing trade.'),('Page 4 / Plummer shaker hardware',link('plummer/','Structural analysis, bored-bolt checks and CNC fabrication')+'. Installed plate-and-bolt hardware at 93.9% lower estimated cost.')]),Spacer(1,12),
 photos([('Pictures/Plummer/Shaker-Plate-On-Shaker.jpg','Plummer: machined adapter installed.'),('Pictures/AIAA/Prototype-1-Assembled.webp','AIAA: assembled Prototype 1 aircraft.'),('Pictures/Nozzle/Hotfire-Thumbnail.webp','Hybrid nozzle: hotfire test frame.')],[180,180,180],90),
 p('Additional Projects','h3'),
 project_index(),
 Spacer(1,10),p('Additional research &amp; coursework','h3'),
 p('Space Physics &amp; Technology Lab: instrument-data analysis with Python/pySPEDAS and assistance with flight-spare laser calibration. University of Sydney pulsed plasma thruster: inductor-spool design and coil-winding calculations. '+link('me360/','ME360 course project')+' is in progress.','small'),
 PageBreak(),
 p('01 / RECOVERY HARDWARE','label'),
 p('Argo Separation and Recovery Subsystem','h2'),
 p('Boston University Rocket Propulsion Group | Subsystem Co-Lead | June 2025-present','small'),
 metrics([('18.7 / 20 lbm','Earlier BP mass / allocation; BP BOM $1,076'),('823 / 1,230 lbf','Calculated parachute opening / snatch loads'),('352 L','Operational vacuum chamber; reported test pressure 0.011 atm')]),Spacer(1,10),
 photos([('Pictures/Recovery/Pre-CO2-Coldflow-Setup.webp','Integrated subsystem before CO2 coldflow; full-system CO2 separation testing is pending.'),('Pictures/CO2/Manufactured-Piercer-Card.webp','Manufactured CO2 cartridge/piercer assembly. Design and fabrication shared by our three-person team.'),('Pictures/Vacuum/Chamber-Full.webp','Door, adapter and seal designed by me; fabricated by my co-lead, who designed the clamps.')],[180,180,180],90),
 p('Design and Test Leadership','recovery-heading'),
 p('Co-led architecture and deployment-hardware trades through four reviews. Compared five published load methods to size lines and check hardware; paired flight computers provide separate firing paths.','recovery-body'),
 p('Authored the integrated vinyl-charge black-powder SOP and led the second integrated test; collaborated on inspection and failure assessment. One of three charges failed in each test; the second damaged the parachute bag and canopy.','recovery-body'),
 p('Standalone vinyl-charge successes did not establish integrated reliability. End-seal manufacturing variability is the leading hypothesis; adjacent-charge damage was inferred afterward. Root cause remains unconfirmed.','small'),
 p('Designed and sized CO2 piercers using pressure, Lam\u00e9 thick-wall hoop-stress and thread-shear calculations; contributed CAD, drawings, machining and component testing in a three-person team.','recovery-body'),
 p('Calculation basis','recovery-heading'),
 recovery_calc([('Recovery lines','Selected 1/2 in, 6,000 lbf Kevlar stock. Design rationale: near-full strength retention, approximately 2× a 50%-efficient knot. Our strength gain remains unmeasured.'),('CO2 deployment sizing','Calculated 4.66 psi separation requirement for four nylon shear pins plus estimated interface friction. Ideal-gas estimate for the modeled free volume: 10.9 g versus a selected 16 g cartridge.'),('CO2 piercer housing','Minimum calculated factor of safety (FOS) 2.01 in Lam\u00e9 hoop stress; internal-thread shear FOS 6.31. Analytical margins, not proof-test results.'),('Vacuum door / Roark','12 in unsupported diameter, 0.25 in thick 6061-T6 plate; 14.7 psi differential gives 1,663 lbf total load. Recorded bending stress 16.5 ksi; deflection 0.0848 in; minimum yield FOS 2.12 using 240 MPa yield strength. Uniform pressure; simply supported around the outer circumference. Deflection uses the Roark plate model; stress is a separately entered calculator result.'),('Legacy Catclaw body','Recorded minimum body FOS 2.01 after my material reduction and piston-retention-slot modification. This tie cutter is separate from the CO2 piercer.')]),
 p('Verification Status','recovery-heading'),
 p('CO2 component firing at 0.011 atm initial chamber pressure complete. Kevlar splice proof load reached 1,800 lbf (1.46 times the 1,230 lbf snatch load) without observed slip, limited by the setup. Preparing the integrated CO2 test SOP; integrated separation and subscale testing remain pending. Chamber instrumentation and data analysis by my co-lead.','recovery-body'),
 p(link('project_recovery/','Recovery architecture, hardware &amp; tests')+' | '+link('project_co2/','CO2 sizing &amp; stress calculations')+' | '+link('project_vacuum/','Chamber design'),'small'),
 PageBreak(),
 p('02 / AERODYNAMICS','label'),
 p('Argo Downcomer Aerocover','h2'),
 p('Boston University Rocket Propulsion Group | Project Lead | August 2026-present','small'),
 metrics([('63 in \u00d7 1.6 in','Fairing length / nominal height on an 8 in diameter rocket'),('Mach 2.0-2.81','Priority comparison range from the simulated trajectory'),('3 concepts','Teammate-owned geometries; shared requirements and analysis by me')]),Spacer(1,10),
 photos([('Pictures/Aerocover/First-Principles-Regions.webp','My CoDR diagram: a first-principles decomposition, not a measured allocation of drag. Pressure and friction act across the whole fairing.')],[540],140),
 photos([('Pictures/Aerocover/CoDR-Flight-Profile.webp','Trajectory used to select high-dynamic-pressure analysis conditions; simulation, not flight data.'),('Pictures/Aerocover/Icarus-Built-Cover.webp','Legacy Icarus fairing: the CFD baseline and a backup flight candidate, not a new design by me.')],[270,270],110),
 p('Analysis','h3'),
 p('Used D = q Sref CD to prioritize conditions by dynamic pressure as well as Mach. Evaluated leading-edge pressure drag, midsection wetted area and aft pressure recovery together with thermal loads, attachment integrity and manufacturing constraints. Isolated axisymmetric profile rankings cannot establish the performance of a partial fairing attached to the rocket body: junction flow and fin interference require integrated analysis.'),
 calc([('Preliminary friction estimate','At Mach 2.81 and recorded Re = 2.04 \u00d7 10\u2078: CD,f \u2248 0.0792, using 477 in\u00b2 wetted area, 7.99 in\u00b2 reference area and a 10% preliminary roughness allowance.'),('Leading-edge surrogate','A 15\u00b0 full-cone correlation gives Cp \u2248 0.1888. It is a screening surrogate for the wedge-like legacy front, not the mounted fairing\u2019s total drag coefficient.')]),
 p('Contributions and Status','h3'),
 p('I developed the common analysis, integration/manufacturing trade and CoDR. Quinn Colleran, Hannah Ruan and Aaron Lin own the three concept geometries. My Mach 2.81 Icarus solve in <b>Ansys Fluent is converged and under review</b>; candidate ranking and Ansys adjoint optimization remain pending.'),
 p('The investigation also led to a nine-profile-family nosecone sweep in RASAero II. A ranking difference from published comparisons prompted further investigation; it does not establish a better flight design.','small'),
 p(link('project_aerocover/','Concept credits, hand calculations, sources &amp; nosecone sweep')+' | Hand-calculation reference: S. S. Chin, <i>Missile Configuration Design</i> (1961).','small'),
 PageBreak(),
 p('03 / BU PLUMMER LABORATORY','label'),
 p('Shaker Adapter and Mounting Bolts','h2'),
 p('Mechanical Design Assistant | June 2026-present','small'),
 metrics([('0.173 mm','Plate displacement predicted in the design-review FEA case'),('20.1 Hz','Shaker operating frequency; analyzed with a 3 kg fixture load'),('2.46 FOS','Plate bearing under the modeled combined bolt load')]),Spacer(1,10),
 p('The adapter mounts a physical Ising-model fixture for controlled shaker vibration tests of bistable buckling elements.'),
 photos([('Pictures/Plummer/Shaker-Analysis.png','SolidWorks plate-displacement result: 0.173 mm maximum. This is a model prediction.'),('Pictures/Plummer/Shaker-Engineering-Drawing.png','My 12 \u00d7 12 in adapter drawing, including underside geometry.')],[360,180],140),
 p('Design and Manufacturing','h3'),
 p('Replaced an estimated $1,170 outsourced plate/custom-bolt solution with $71.11 of in-house hardware. Developed SolidWorks CAD/FEA, drawings and CAM/G-code; machined the 6061-T6 plate on a Haas VF-2 and checked plate dimensions with calipers against the \u00b10.005 in drawing tolerance.'),
 p('Load-path and displacement calculations guided material removal; SolidWorks FEA checked the lightened plate. Finished mass: 1.90 kg from 3.19 kg stock (40.4% stock-to-part reduction).'),
 p('Drilled 5 mm axial bores in standard medium-carbon-steel M10 bolts for the required shaker interface after unsuccessful stainless-steel machining attempts. The bored bolts and adapter are installed.'),
 p('Structural calculation basis','h3'),
 calc([('Installed joint geometry','M10 \u00d7 1.5 with a 5 mm axial bore; modeled remaining tensile area 38.35 mm\u00b2. Nominal Class 8.8 yield strength 640 MPa; local plate bearing thickness 9.7 mm; thread engagement 9.35 mm.'),('Per-bolt load path','5 kg allowance (2 kg plate + 3 kg fixture) at 11 G, shared by four bolts: 134.9 N external load per bolt. Workbook conservatively adds the full external load to 16.36 kN preload: 16.50 kN combined. Torque estimate: 21.7 ft-lbf at K = 0.18; joint stiffness sharing is not modeled.'),('Static FOS by checked mode','Bolt tensile yield: 1.49 under preload plus full external load; preload alone gives 1.50. Plate bearing 2.46; pull-through 4.99; external-thread shear 3.71; internal-thread shear 3.60. These are mode-specific ratios, not an overall dynamic FOS.'),('Displacement checks','Selected L/240 limit for the 12 in plate span: 1.27 mm; review plate FEA: 0.173 mm. The later 3 kg dynamic fixture model predicts 0.44 mm deformation relative to the base at 20.1 Hz and 13 mm peak-to-peak base motion. These are separate load cases.')]),
 Spacer(1,7),p('Preload maintains joint compression; bolt/joint stiffness determines cyclic load sharing. The 1.49 ratio checks static tensile yield, not fatigue at 20.1 Hz. Preload scatter, separation and fatigue are not quantified here. Displacements are predictions; cost covers plate and bolts only.','small'),
 p(link('plummer/','Full calculations, drawings, FEA and machining evidence')+' | Sources: my design review and DSRF Calcs; joint interpretation: <link href="https://ntrs.nasa.gov/citations/19960012183" color="#B62836">NASA TM-106943</link>.','small'),
]
doc=SimpleDocTemplate(str(PDF),pagesize=(612,792),leftMargin=36,rightMargin=36,topMargin=31,bottomMargin=47,title='Alexander Tong - Technical Portfolio',author='Alexander Tong')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
reader=PdfReader(PDF)
assert len(reader.pages)==4, f'Expected 4 pages; got {len(reader.pages)}'
texts=[page.extract_text() for page in reader.pages]
assert '48 Instron' in texts[0] and '823 / 1,230' in texts[1] and 'Ansys Fluent' in texts[2]
assert '38.35' in texts[3] and 'calipers' in texts[3]
assert '2.12' in texts[1] and '0.0848' in texts[1] and '7.8' in texts[0]
(OUT/'portfolio-text-check.txt').write_text('\n\n'.join(texts),encoding='utf-8')
shutil.copy2(PDF, ROOT / 'public/Reports' / PDF.name)
print(f'Updated PDF: {len(reader.pages)} pages; {PDF.stat().st_size:,} bytes; links per page {[len(pg.get("/Annots",[])) for pg in reader.pages]}')
