"""Build the public PDF from the approved LaTeX content; separate PDF typesetting."""
from pathlib import Path
import re
import argparse
from html import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Flowable, KeepTogether
from reportlab.lib.styles import ParagraphStyle
import pdfplumber

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--source', default='resume-drafts/Alexander_Tong_Space_Hardware.tex')
parser.add_argument('--output', default='public/Resume/Alex_s_Resume.pdf')
options = parser.parse_args()
SOURCE = ROOT / options.source
OUTPUT = ROOT / options.output
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
for suffix, filename in [('', 'times.ttf'), ('-Bold', 'timesbd.ttf'), ('-Italic', 'timesi.ttf')]:
    pdfmetrics.registerFont(TTFont('Resume' + suffix, str(Path('C:/Windows/Fonts') / filename)))
pdfmetrics.registerFontFamily('Resume', normal='Resume', bold='Resume-Bold', italic='Resume-Italic')

def args(text, start, count):
    values = []
    pos = start
    for _ in range(count):
        while text[pos].isspace(): pos += 1
        assert text[pos] == '{'
        begin = pos + 1
        depth = 1
        pos += 1
        while depth:
            if text[pos] in '{}' and text[pos-1] != '\\':
                depth += 1 if text[pos] == '{' else -1
            pos += 1
        values.append(text[begin:pos-1])
    return values

def clean(s):
    # Keep the public PDF's text layer ASCII. Some extractors fail to map
    # ReportLab's subset glyphs for bullets, typographic punctuation and ±.
    s = s.replace(r'$\pm$', '+/-').replace(r'CO$_2$', 'CO2')
    s = s.replace(r'\%', '%').replace(r'\$', '$').replace(r'\&', '&').replace('--', '-')
    s = s.translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', '–': '-', '—': '-'}))
    return ' '.join(s.split())

class BulletParagraph(Paragraph):
    def draw(self):
        super().draw()
        # Vector dot preserves the round-bullet appearance without adding an
        # unmapped Unicode glyph to the text layer used by resume scanners.
        self.canv.circle(5, self.height - 7, 1.5, stroke=0, fill=1)

class Heading(Flowable):
    def __init__(self, title, date='', role='', location='', section=False):
        super().__init__()
        self.values = title, date, role, location
        self.section = section
        self.height = 19 if section else 24
        self.keepWithNext = True
    def wrap(self, width, height):
        self.width = width
        return width, self.height
    def draw(self):
        title, date, role, location = self.values
        c = self.canv
        if self.section:
            c.setFont('Resume', 11.5)
            c.drawString(0, 6, title.upper())
            c.setLineWidth(.55)
            c.line(0, 3, self.width, 3)
        else:
            c.setFont('Resume-Bold', 10)
            c.drawString(0, 14, title)
            c.setFont('Resume', 10)
            c.drawRightString(self.width, 14, date)
            c.setFont('Resume-Italic', 10)
            c.drawString(0, 2, role)
            c.drawRightString(self.width, 2, location)

body = ParagraphStyle('body', fontName='Resume', fontSize=10, leading=11.2,
                      leftIndent=12, firstLineIndent=0, bulletIndent=4,
                      bulletFontName='Resume', bulletFontSize=10, spaceAfter=1)
plain = ParagraphStyle('plain', fontName='Resume', fontSize=10, leading=11.2)
name = ParagraphStyle('name', fontName='Resume-Bold', fontSize=25, leading=27, alignment=1, spaceAfter=1)
contact = ParagraphStyle('contact', fontName='Resume', fontSize=9.5, leading=11, alignment=1, spaceAfter=3)
text = SOURCE.read_text(encoding='utf-8').split(r'\begin{document}', 1)[1]
education_heading = re.search(r'\\section\{(Professional Education|Education)\}', text)
assert education_heading, 'Missing education section in LaTeX source'
story = [Paragraph('ALEXANDER TONG', name), Paragraph(
    '860-706-3624 | <link href="mailto:alto335@bu.edu">alto335@bu.edu</link> | '
    '<link href="https://alexandertong.space">alexandertong.space</link> | '
    '<link href="https://www.linkedin.com/in/alto335/">linkedin.com/in/alto335</link>', contact),
    Heading(education_heading.group(1), section=True),
    Heading('Boston University', 'Expected May 2028',
            'B.S. Mechanical Engineering, Aerospace Concentration', 'GPA: 3.71/4.00')]
section_matches = list(re.finditer(r'\\section\{([^}]+)\}', text))
expected_bullets = 0
for i, section in enumerate(section_matches):
    title = section.group(1)
    if title in {'Education', 'Professional Education'}: continue
    end = section_matches[i+1].start() if i+1 < len(section_matches) else len(text)
    block = text[section.end():end]
    story.append(Heading(title, section=True))
    if title == 'Technical Skills':
        skills = block.split(r'{\small', 1)[1].split('}', 1)[0]
        story.append(Paragraph(escape(clean(skills)), plain))
        continue
    entries = list(re.finditer(r'\\resumeSubheading\s', block))
    for n, entry in enumerate(entries):
        values = [clean(x) for x in args(block, entry.end(), 4)]
        stop = entries[n+1].start() if n+1 < len(entries) else len(block)
        entry_text = block[entry.end():stop]
        group = [Heading(*values)]
        for item in re.finditer(r'\\resumeItem\s*\{', entry_text):
            value = clean(args(entry_text, item.end()-1, 1)[0])
            group.append(BulletParagraph(escape(value), body))
            expected_bullets += 1
        group.append(Spacer(1, 2.5))
        story.append(KeepTogether(group))

temp = OUTPUT.with_suffix('.candidate.pdf')
SimpleDocTemplate(str(temp), pagesize=(612,792), leftMargin=36, rightMargin=36,
                  topMargin=36, bottomMargin=36, title='Alexander Tong Resume',
                  author='Alexander Tong').build(story)
with pdfplumber.open(temp) as doc:
    result = '\n'.join(p.extract_text(x_tolerance=2) or '' for p in doc.pages)
    assert len(doc.pages) == 1, f'Unexpected page count: {len(doc.pages)}'
    assert '\ufffd' not in result, 'Unmapped glyph found in extracted resume text'
    assert 'set-based design' in result
    assert '(cid:' not in result
OUTPUT.write_bytes(temp.read_bytes())
temp.unlink()
print(f'Verified one page and {expected_bullets} vector round bullets; extracted text has no unmapped glyphs.')
