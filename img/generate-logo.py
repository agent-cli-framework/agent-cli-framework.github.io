# aclif logo: the Prompt One button, widened, with "aclif" in place of the bar.
# Needs fontTools and Inter-Bold.ttf (Google Fonts, OFL) next to this script.
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

font = TTFont('Inter-Bold.ttf')
gs = font.getGlyphSet(); cmap = font.getBestCmap(); upm = font['head'].unitsPerEm
def glyph(ch): return gs[cmap[ord(ch)]]

H = 160.0                       # button height
s = H/300.0                     # scale of the original 300-unit button
RX = 66*s                       # corner radius (button proportion)
STROKE = 22.5*s                 # outline width (button proportion)
MARK = 2.8302*s                 # scale of the original 96-unit mark group
PAD = 34.0
GAP = 24.0
TRACK = -0.01

# chevron: original polyline 26,28 44,48 26,68 in mark units, stroke 8
chev_w = (44-26)*MARK; chev_h = (68-28)*MARK
chev_x = PAD; chev_y = H/2 - chev_h/2
chev_tf = f"translate({chev_x - 26*MARK:.3f},{chev_y - 28*MARK:.3f}) scale({MARK:.4f})"

# letters: x-height equals the chevron height, band centred on the chevron
bp = BoundsPen(gs); glyph('x').draw(bp); xh = bp.bounds[3]
scale = chev_h/xh
baseline = H/2 + chev_h/2
x = chev_x + chev_w + GAP
letters = []
for ch in 'aclif':
    g = glyph(ch); pen = SVGPathPen(gs)
    g.draw(TransformPen(pen, (scale, 0, 0, -scale, x, baseline)))
    letters.append(pen.getCommands())
    x += (g.width + TRACK*upm)*scale
word_end = x - TRACK*upm*scale
W = word_end + PAD
inset = STROKE/2

def svg(outline, ink, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.2f} {H:.0f}" role="img" aria-label="aclif">\n'
            f'  <title>{title}</title>\n'
            f'  <rect x="{inset:.2f}" y="{inset:.2f}" width="{W-STROKE:.2f}" height="{H-STROKE:.2f}" rx="{RX:.2f}" fill="none" stroke="{outline}" stroke-width="{STROKE:.2f}"/>\n'
            f'  <polyline transform="{chev_tf}" points="26,28 44,48 26,68" fill="none" stroke="{ink}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>\n'
            f'  <path fill="{ink}" d="{" ".join(letters)}"/>\n</svg>\n')

open('aclif-logo.svg','w').write(svg('#14b4fa', '#501ee6', 'aclif, the Agent CLI Framework'))
open('aclif-logo-rev.svg','w').write(svg('#501ee6', '#14b4fa', 'aclif, the Agent CLI Framework'))
print(f"size {W:.0f}x{H:.0f}")
