---
name: "tarun-cover-letter-builder"
description: "Build a tailored one-page branded cover letter PDF for Tarun Palthi from a job posting, using the established ReportLab template, brand-color rules, gap protocol, and resume-merge rules."
---

# Tarun Palthi Cover Letter Builder

Use whenever Tarun uploads a job posting (PDF, .txt, screenshots, or URL), with or without a tailored resume. Each upload is a request for a finished cover letter. Do not wait for extra instructions. Anything Tarun corrects once becomes a permanent rule; never make him repeat himself.

## Locations (pick by environment)

- **claude.ai chat:** `WORK_DIR=/home/claude/coverletter`, `OUT_DIR=/mnt/user-data/outputs`.
- **Claude Code (CLI or cloud session):** `WORK_DIR=<session scratchpad>/coverletter` (or `${TMPDIR:-/tmp}/coverletter` if no scratchpad is listed), and `OUT_DIR` = the same scratchpad folder. Never write letters, resumes or job postings into this repository: it is a public GitHub Pages site. Deliver with SendUserFile.

## Workflow

1. **Read inputs.** `pdftotext -layout` the JD (Read tool for images/screenshots) and the resume if attached.
2. **Gap check against confirmed skills (see below).** If any meaningful gap exists, ask upfront with AskUserQuestion BEFORE drafting (batch up to 4 questions). Standard options: "Frame as transferable" / "Light, honest mention" / "I have real experience with this" / "Don't address it". Follow the chosen framing exactly. If there are no real gaps (strong natural fit), skip questions and say so.
3. **Brand colors.** Research and assign colors (rules below).
4. **Build** a `build_letter_<company>.py` in `WORK_DIR` from the template below. Output to `OUT_DIR/Tarun_Palthi_CoverLetter_<Company>.pdf`.
5. **Verify**: exactly 1 page (pypdf), no em dashes (`grep -nP "—"` on pdftotext output), no Python overclaim (`grep -i python`), plus targeted greps proving gap framings were honored (e.g. no "dbt", no "product owner", no "direct reports" claim). Then render with `pdftoppm -png -r 120` and LOOK at it.
6. **Deliver** with SendUserFile. Standalone letter always. If a tailored resume was attached this turn, also deliver a merged PDF: **resume pages first, cover letter last**. No resume attached = standalone letter only (master resume is the implicit content basis).
7. Finish with 2-3 sentences: what it is, brand colors used, how gaps were handled, verification result. No recap of steps.

If the letter overflows to page 2: trim lead-in paragraph, a bullet, or the closing sentence; as a last resort tighten the Spacer after the box (8 to 5) and before the signature (6 to 3). Never shrink fonts.

## Tarun's background (for tailoring)

- Analytics Lead (Engr III, Data Science) at Verizon since Jul 2022; at Verizon since Jan 2020 (via Datawin Systems and AgreeYa Solutions, staff augmentation, single client, NOT multi-account consulting). 8+ years. MBA (New England College, 3.9) and MS CIS (NJIT, 3.9).
- Signature achievements: Digital Semantic Layer (BigQuery to Looker/LookML data products, GenAI via Claude Code and Gemini), 150+ A/B and multivariate experiments contributing to $500M+ business impact, 150+ executive dashboards, AI-enabled MCP integrations (BigQuery, Teradata, Jira), KPI governance, mentoring analysts.
- **Confirmed hands-on:** Adobe Analytics, Tableau, Looker (certified), SQL, R, ContentSquare, Quantum Metric, Claude Code, Gemini, MCP automation, Tealium, AEM, HTML/CSS/JS, Adobe Target, A/B/MVT testing, Power BI, Alteryx, mobile app analytics, BigQuery, Teradata.
- **Python is NOT a strength.** Never claim hands-on/strong Python. Omit it (or at most "comfortable with SQL-driven Python and R" when truly needed).
- 150+ tests = real hypothesis testing/experimental design. Never list as a gap.
- Prior roles: Healthcare Data Analyst (pharmacy/PrimeRx, 2015-16), Financial Data Analyst (PwC engagement), ADP, Integra.
- **Genuine gaps (ask before assuming):** formal predictive/statistical modeling terminology (regression, causal inference, power analysis); Salesforce Marketing Cloud; role-specific tools (Amplitude, Pendo, Segment = exposure only; dbt, Omni, GA4 by name, Slate/CRM admin); formal people management (no direct reports; frame as mentoring / ready to grow into it, or lean on cross-functional influence if the JD frames it as influence); B2B pipeline, paid-media/agency management, marketplace, pharma commercial domains; formal product-owner title.
- Required-but-unconfirmed items: handle per Tarun's chosen framing. "Preferred/plus" items are simply omitted.

## Letter structure (gold standard = ZoomInfo letter)

Three paragraphs before the box, then the Core Alignment box, then close:

1. **Hook:** punchy, often contrarian one-line thesis tied to the role. NEVER "I'm writing to apply for...". Ends with the "discipline I've built my career around" idea.
2. **Company paragraph:** bold company name; restate what the role/team owns using the JD's own language; vary the closing phrase from the hook so it isn't verbatim repetition.
3. **Verizon achievements paragraph:** bold **Verizon**, key metrics (**150+ ...**, **$500M+ in business impact**, **Digital Semantic Layer**). Gap framings live here when integrated naturally.
4. **Core Alignment box:** heading exactly `CORE ALIGNMENT WITH THE [EXACT ROLE TITLE] ROLE` in caps (escape & as `&amp;`). 4 bullets: `<b>Bolded Label:</b> achievement, direct experience with [X] this role calls for/owns/delivers` (a callback to the JD's language, not a skill list). Never write "direct experience with" for something Tarun lacks; pick an X he genuinely has.
5. **Closing:** one sentence bolding the key theme phrase, then "Thank you for your time and consideration.", then "Sincerely," / "Tarun Palthi".

Optional separate italic "One honest note:" paragraph only for combined/multiple gaps where integrated framing would be awkward; the gap must be clearly named.

Hard rules: NO em dashes anywhere (use periods, commas, colons, "and", "which"). Always exactly one page. Greeting is "Dear Hiring Team,".

## Brand colors

Palette variables: BRAND (header/footer fill), DUNE (box heading text), BONJOUR (pale strip/box background), SULU (thin horizontal accent line under header AND vertical bar on the box), MID_GRAY, BLACK.

- **Research:** `pdftoppm -png -r 200 -f 1 -l 1 jd.pdf page`, PIL crop of the top region, `Counter` of RGB values ignoring near-white/gray to pixel-sample the logo/banner; cross-reference official brand guidelines (company identity site, brandcolorcode.com, brandpalettes.com, GitHub brand repos). Smaller/private companies with no listing: pixel-sampled color is the answer; note it in a code comment.
- **Design judgment (do this by default, never wait to be told):** mirror how the company itself uses its palette: which color is the large-surface color, which is the pop/accent, which is for small text. Sanity-check as a reader: white text legible on the header, accent actually reads as an accent (thin lines/borders/small text), overall looks like their own brand team made it. Only ask Tarun about colors if the brand truly has no precedent.
- **Multi-color brands:** never collapse to one color. Dominant color = large fills (header/footer). Secondary brand color = the horizontal strip, vertical box bar, and box heading text. (Lyft: Pink #FF00BF header/footer; dark purple #352384 strip, bar, heading.) If Tarun says "make X dominant", X leads the large fills and the other brand colors stay as visible accents.
- **Verizon internal roles:** Verizon Red #D52B1E with Ecru White #F3EDE0 for strip/box background and accent (not a light red/pink tint).
- **Gradient brands:** soft pale gradient box background via custom `GradientBox` Flowable (canvas.linearGradient + clipPath); only bold gradients for consumer/design-forward/startup brands, pale for conservative/financial.
- **Multi-color stripe brands:** segmented stripe under header: Google (4-color), Adobe (#FF0000, #FBB034, #FFDD00, #C1D82F, #00A4E4, #8A7967, #6A737B), Comcast (6-color peacock).
- Past examples: Invesco #000AD2/#000078; Zendesk #213423/#CAEC6C; Meta #0081FB; AbbVie #071D49 + #009EC2; Dollar Shave Club #051024 + #FF5500; T-Mobile #E20074; Anthropic #141413 + #D97757 + cream #FAF9F5; Stanford Cardinal #8C1515 (neutrals #2E2D29, #7F7776, Fog #DAD7CB).

## Template (reuse unmodified; change only colors, text, and content)

Font: TeX Gyre Pagella TTFs at `WORK_DIR/fonts/PagellaTG-{regular,bold,italic,bolditalic}.ttf`. If missing, get the OTFs (`apt-get install -y fonts-texgyre`, or the CTAN tex-gyre zip) and convert to TrueType, since ReportLab cannot load CFF OTFs: `fontforge -lang=ff -c "Open('in.otf'); Generate('out.ttf');"`, or without fontforge use fontTools (`pip install fonttools`) and its otf2ttf recipe (`fontTools.pens.cu2quPen`). `registerFontFamily` must immediately follow the four `registerFont` calls or bold silently falls back.

```python
import os; WORK_DIR=os.environ.get('WORK_DIR','/home/claude/coverletter'); os.chdir(WORK_DIR)
output_path=os.path.join(os.environ.get('OUT_DIR','/mnt/user-data/outputs'),'Tarun_Palthi_CoverLetter_<Company>.pdf')
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
for n,f in [('Pagella','regular'),('Pagella-Bold','bold'),('Pagella-Italic','italic'),('Pagella-BoldItalic','bolditalic')]:
    pdfmetrics.registerFont(TTFont(n, f'fonts/PagellaTG-{f}.ttf'))
pdfmetrics.registerFontFamily('Pagella', normal='Pagella', bold='Pagella-Bold', italic='Pagella-Italic', boldItalic='Pagella-BoldItalic')

BRAND=colors.HexColor("#......"); DUNE=colors.HexColor("#......"); BONJOUR=colors.HexColor("#......")
MID_GRAY=colors.HexColor("#5A6B70"); BLACK=colors.HexColor("#1A1A1A"); WHITE=colors.white; SULU=colors.HexColor("#......")
PAGE_W,PAGE_H=letter; MARGIN=0.65*inch; CONTENT_W=PAGE_W-2*MARGIN
NAME="TARUN PALTHI"; SUBTITLE="ROLE TITLE IN CAPS"
CONTACT_LINE="Avenel, NJ 07001  |  201.744.4259  |  palthitarun@gmail.com  |  linkedin.com/in/tarunpalthi  |  tarunpalthi.github.io"
TARGET_ORG="Company | Team"; POSITION_APPLIED="Role Title"; TAGLINE="THEME ONE  |  THEME TWO  |  THEME THREE"
HEADER_H=0.95*inch; STRIP_H=0.62*inch; FOOTER_H=0.34*inch

def draw_header_footer(c, doc):
    c.saveState()
    c.setFillColor(BRAND); c.rect(0, PAGE_H-HEADER_H, PAGE_W, HEADER_H, fill=1, stroke=0)
    c.setFillColor(WHITE); c.setFont("Pagella-Bold",20); c.drawString(MARGIN, PAGE_H-0.40*inch, NAME)
    sub=10.5
    if c.stringWidth(SUBTITLE,"Pagella-Bold",sub) > (PAGE_W-2*MARGIN): sub=9
    c.setFont("Pagella-Bold",sub); c.drawString(MARGIN, PAGE_H-0.60*inch, SUBTITLE)
    c.setFont("Pagella",8.3); c.drawString(MARGIN, PAGE_H-0.80*inch, CONTACT_LINE)
    c.setFillColor(SULU); c.rect(0, PAGE_H-HEADER_H-0.035*inch, PAGE_W, 0.035*inch, fill=1, stroke=0)
    strip_top=PAGE_H-HEADER_H-0.035*inch
    c.setFillColor(BONJOUR); c.rect(0, strip_top-STRIP_H, PAGE_W, STRIP_H, fill=1, stroke=0)
    c.setFont("Pagella",7.6); c.setFillColor(MID_GRAY)
    c.drawString(MARGIN, strip_top-0.24*inch, "TARGET ORGANIZATION")
    c.drawRightString(PAGE_W-MARGIN, strip_top-0.24*inch, "POSITION APPLIED")
    c.setFont("Pagella-Bold",10); c.setFillColor(BLACK)
    if c.stringWidth(TARGET_ORG,"Pagella-Bold",10)+c.stringWidth(POSITION_APPLIED,"Pagella-Bold",10) > PAGE_W-2*MARGIN-0.3*inch:
        c.setFont("Pagella-Bold",8.5)
    c.drawString(MARGIN, strip_top-0.42*inch, TARGET_ORG)
    c.drawRightString(PAGE_W-MARGIN, strip_top-0.42*inch, POSITION_APPLIED)
    c.setFillColor(BRAND); c.rect(0,0,PAGE_W,FOOTER_H,fill=1,stroke=0)
    c.setFont("Pagella-Bold",8.3); c.setFillColor(WHITE); c.drawCentredString(PAGE_W/2, FOOTER_H/2-3, TAGLINE)
    c.restoreState()

body_style=ParagraphStyle('body',fontName='Pagella',fontSize=10.2,leading=14.2,alignment=TA_JUSTIFY,textColor=BLACK,spaceAfter=8)
box_head_style=ParagraphStyle('boxhead',fontName='Pagella-Bold',fontSize=10.4,leading=13,textColor=DUNE,spaceAfter=5)
bullet_style=ParagraphStyle('bullet',fontName='Pagella',fontSize=9.6,leading=13.2,textColor=BLACK,leftIndent=10,spaceAfter=3)
sig_style=ParagraphStyle('sig',fontName='Pagella-Bold',fontSize=10.5,leading=13,textColor=BLACK)
greet_style=ParagraphStyle('greet',fontName='Pagella',fontSize=10.2,leading=14.2,textColor=BLACK,spaceAfter=8)

story=[Spacer(1,4), Paragraph("Dear Hiring Team,", greet_style)]
# story += hook, company_para, lead_in (body_style Paragraphs)
box_flow=[Paragraph("CORE ALIGNMENT WITH THE ... ROLE", box_head_style)]
# for b in bullets: box_flow.append(Paragraph("&bull;  "+b, bullet_style))
box=Table([[box_flow]], colWidths=[CONTENT_W])
box.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),BONJOUR),('LINEBEFORE',(0,0),(0,0),3,SULU),
    ('LEFTPADDING',(0,0),(-1,-1),14),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
story += [box, Spacer(1,8)]
# closing paragraph (body_style), "Thank you for your time and consideration.", Spacer(1,6), "Sincerely,", "Tarun Palthi"

top=HEADER_H+STRIP_H+0.18*inch; bottom=FOOTER_H+0.15*inch
doc=BaseDocTemplate(output_path, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=top, bottomMargin=bottom)
doc.addPageTemplates([PageTemplate(id="letter", frames=[Frame(MARGIN,bottom,CONTENT_W,PAGE_H-top-bottom,id="main")], onPage=draw_header_footer)])
doc.build(story)
```

Merge (resume first, letter last):

```python
from pypdf import PdfReader, PdfWriter
w=PdfWriter()
for p in PdfReader(resume).pages: w.add_page(p)
for p in PdfReader(letter_pdf).pages: w.add_page(p)
w.write(open(out,'wb'))
```

## Resume rules

Never alter the resume's format or font (Times New Roman, gray section headers) unless asked. Represent AgreeYa/Datawin accurately as staff augmentation. A role-specific resume, when provided, is used for that role; otherwise the latest master resume is the default.