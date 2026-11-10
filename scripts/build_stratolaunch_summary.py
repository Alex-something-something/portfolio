"""Build the application project summary and its public portfolio copy."""
from pathlib import Path
from html import escape
import shutil

from pypdf import PdfReader
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
TEXT = ROOT / 'output/application'
OUT.mkdir(parents=True, exist_ok=True)
TEXT.mkdir(parents=True, exist_ok=True)
PDF = OUT / 'Alexander_Tong_Stratolaunch_Project_Summary.pdf'
for name, filename in [('Arial', 'arial.ttf'), ('ArialBold', 'arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(Path('C:/Windows/Fonts') / filename)))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='ArialBold')
INK = HexColor('#172331')
MUTED = HexColor('#526171')
STYLES = {
    'title': ParagraphStyle('title', fontName='ArialBold', fontSize=22, leading=26, textColor=INK, spaceAfter=7),
    'name': ParagraphStyle('name', fontName='ArialBold', fontSize=11, leading=14, textColor=INK, spaceAfter=3),
    'meta': ParagraphStyle('meta', fontName='Arial', fontSize=9, leading=12, textColor=MUTED, spaceAfter=4),
    'body': ParagraphStyle('body', fontName='Arial', fontSize=10.5, leading=14, textColor=INK, spaceAfter=8),
    'heading': ParagraphStyle('heading', fontName='ArialBold', fontSize=11.5, leading=15, textColor=INK, spaceBefore=6, spaceAfter=5, keepWithNext=True),
}

BLOCKS = [
    ('body', "I co-lead separation and recovery for Argo, Boston University Rocket Propulsion Group's 135 lb dry-mass liquid bipropellant rocket targeting 100,000 ft. Within its single-break, dual-deploy architecture, I develop hardware through analysis, CAD, machining, integration, and testing. The design calls for nosecone separation near apogee and main-parachute deployment at 2,000 ft above ground. Flight verification remains pending."),
    ('heading', 'Design and hardware'),
    ('body', "I compared 23 commercial parachute candidates and five published load-estimation methods. I applied a 1.5 design factor of safety (FOS) to the 823 lbf opening estimate for a 1,230 lbf line-sizing load. A separate 2.0 line-strength design FOS and termination efficiencies supported 6,000 lbf-rated Kevlar stock. Published comparisons of approximately 2x splice-versus-knot strength motivated Brummel eye splices; dynamic tests showed no observed slip. Peak force and ultimate strength were not measured."),
    ('body', "For the Catclaw restraint release, I removed material from the existing body, reshaped its slot to retain the piston, produced the drawing, and machined the part on a manual mill and lathe. The redesigned body weighed 49.5% less and broke the zip-tie restraint in eight of eight trials at the selected setting."),
    ('heading', 'Testing and iteration'),
    ('body', "I wrote the integrated black-powder test procedure and led the second test, including crew briefings and fire or abort decisions. My co-lead led the first. One of three charges failed in each test; the second also damaged the parachute bag and canopy. Successful standalone trials had not translated into consistent operation in the packed assembly."),
    ('body', "I proposed a CO2 replacement and contributed pressure and thick-wall calculations (hoop FOS 2.01; thread-shear FOS 6.31), Fusion 360 CAD, drawings, machining, and component testing within a three-person team. I designed the complete 352 L vacuum chamber, including detailed door, adapter, and seal analysis. My co-lead developed the DAQ system and led pressure-data acquisition and analysis. In the integrated trial, the cartridge was fully punctured and discharged, but the nosecone did not separate and its shear pins remained intact. Visible discharge through the wiring port and displaced sealing putty identified a leakage path. We revised the feedthrough with an NPT fitting, a smaller opening, epoxy around redundant wiring, and supplemental vacuum putty. Complete deployment with the revised seal awaits retest."),
    ('heading', 'Why this work'),
    ('body', "I chose recovery for the chance to follow a design from first principles to a physical test. I enjoy tracing why hardware behaves differently from a calculation, then using that evidence to improve the system. The work taught me to coordinate mechanical and electrical interfaces early and document observations separately from assumptions. Stratolaunch's reusable hypersonic flight testing appeals to me for the same connection between demanding design problems, integrated hardware, and measured performance. I would bring hands-on fabrication and test experience, along with a willingness to question and revise my own designs."),
]

def p(text, style='body'):
    return Paragraph(escape(text), STYLES[style])

story = [p('Project Summary', 'title'), p('Alexander Tong | Argo Separation and Recovery Co-Lead', 'name'),
    Paragraph('<a href="mailto:alto335@bu.edu" color="#526171">alto335@bu.edu</a> | <a href="https://alexandertong.space" color="#526171">alexandertong.space</a> | Boston University Mechanical Engineering', STYLES['meta']),
    Spacer(1, 7)]
story.extend(p(text, style) for style, text in BLOCKS)
doc = SimpleDocTemplate(str(PDF), pagesize=(612, 792), leftMargin=42, rightMargin=42,
    topMargin=36, bottomMargin=36, title='Project Summary', author='Alexander Tong')
doc.build(story)
reader = PdfReader(str(PDF))
if len(reader.pages) != 1:
    raise RuntimeError(f'Expected one page; got {len(reader.pages)}')
plain = ['Project Summary', 'Alexander Tong | Argo Separation and Recovery Co-Lead',
    'alto335@bu.edu | alexandertong.space | Boston University Mechanical Engineering', '']
for _, text in BLOCKS:
    plain.extend([text, ''])
text_file = TEXT / 'Alexander_Tong_Stratolaunch_Project_Summary.txt'
text_file.write_text('\n'.join(plain), encoding='utf-8')
application = ROOT / 'applications/stratolaunch-2027'
application.mkdir(parents=True, exist_ok=True)
shutil.copy2(PDF, application / PDF.name)
shutil.copy2(text_file, application / 'Project_Summary.txt')
public = ROOT / 'public/Reports/Alexander_Tong_Project_Summary.pdf'
public.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(PDF, public)
print(f'Created {PDF} ({len(reader.pages)} page, {len(reader.pages[0].extract_text().split())} words)')
