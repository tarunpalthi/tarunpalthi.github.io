"""Convert TeX Gyre Pagella OTFs to TrueType for ReportLab. Usage: python3 otf2ttf.py <WORK_DIR>/fonts
Needs: apt-get install -y fonts-texgyre; pip install fonttools"""
import sys
from fontTools.ttLib import TTFont, newTable
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
def conv(i,o):
    f=TTFont(i); gs=f.getGlyphSet(); glyf={}
    for n in f.getGlyphOrder():
        p=TTGlyphPen(gs); gs[n].draw(Cu2QuPen(p,1.0,reverse_direction=True)); glyf[n]=p.glyph()
    del f["CFF "]
    if "VORG" in f: del f["VORG"]
    g=newTable("glyf"); g.glyphOrder=f.getGlyphOrder(); g.glyphs=glyf; f["glyf"]=g
    f["loca"]=newTable("loca"); f["maxp"].tableVersion=0x00010000
    for k in ("maxZones","maxTwilightPoints","maxStorage","maxFunctionDefs","maxInstructionDefs","maxStackElements","maxSizeOfInstructions","maxComponentElements"):
        setattr(f["maxp"],k,0)
    f["maxp"].maxZones=1; f["head"].indexToLocFormat=0; f["head"].glyphDataFormat=0
    f["post"].formatType=2.0; f["post"].extraNames=[]; f["post"].mapping={}
    f.sfntVersion="\x00\x01\x00\x00"; f.save(o)
for s in ["regular","bold","italic","bolditalic"]:
    conv(f"/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella-{s}.otf", f"{sys.argv[1]}/PagellaTG-{s}.ttf")
