#!/usr/bin/env python3
"""Generate self-contained, theme-aware README banners (standard library only)."""
from __future__ import annotations
import argparse
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    'light': dict(bg='#f1f7f7', panel='#ffffff', ink='#18343c', muted='#506974',
                  line='#c5d9dc', accent='#087f83', tint='#e3f1ef', core='#163f46', coretext='#f1fffb'),
    'dark': dict(bg='#0e1c24', panel='#182c35', ink='#edf7f8', muted='#b2c9d2',
                 line='#35545e', accent='#70d9c4', tint='#203e43', core='#214b50', coretext='#f1fffb'),
}


def banner(theme: str, compact: bool = False) -> str:
    p = PALETTES[theme]
    width, height = (420, 150) if compact else (1120, 168)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
             '<title id="title">Inference specialization</title>',
             '<desc id="desc">Known models, hardware and workloads guide construction, optimization and validation of a purpose-built execution stack. A conceptual map, not a measured performance claim.</desc>',
             f'<rect width="{width}" height="{height}" rx="16" fill="{p["bg"]}"/>',
             '<g font-family="Arial, Helvetica, sans-serif">']

    def rect(x, y, w, h, fill='panel', stroke='line', radius=8):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{p[fill]}" stroke="{p[stroke]}"/>')

    def text(x, y, value, size=14, color='ink', weight=400, anchor='middle', spacing=None):
        extra = f' letter-spacing="{spacing}"' if spacing is not None else ''
        parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{p[color]}"{extra}>{escape(value)}</text>')

    def path(d, color='line', width=1.5):
        parts.append(f'<path d="{d}" fill="none" stroke="{p[color]}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>')

    # A quiet dot field suggests a design space without adding a third-party asset.
    parts.append(f'<defs><pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="18" cy="12" r="0.7" fill="{p["line"]}" opacity="0.48"/></pattern></defs>')
    parts.append(f'<rect width="{width}" height="{height}" rx="16" fill="url(#dots)"/>')

    if compact:
        for x, label in zip((16, 153, 290), ('MODEL', 'HARDWARE', 'WORKLOAD')):
            rect(x, 15, 114, 30)
            text(x+57, 35, label, 12, 'muted', 700, spacing=0.6)
        rect(61, 88, 298, 45, 'core', 'core', 10)
        text(210, 117, 'Specialized execution', 20, 'coretext', 700)
        text(210, 77, 'build · optimize · verify', 11, 'muted', 400)
        # The input bus leaves a gap for the construction caption.
        path('M73 45 V56 H347 V45 M210 45 V56 M210 79 V88', 'accent')
    else:
        for y, label, kind in ((19,'MODEL','graph'),(69,'HARDWARE','chip'),(119,'WORKLOAD','bars')):
            rect(34, y, 192, 30)
            text(138, y+20, label, 12, 'muted', 700, spacing=1)
            if kind == 'graph':
                path(f'M51 {y+20} L57 {y+9} L66 {y+20} M51 {y+20} H66', 'accent')
                for x, yy in ((51,y+20),(57,y+9),(66,y+20)):
                    parts.append(f'<circle cx="{x}" cy="{yy}" r="2.2" fill="{p["accent"]}"/>')
            elif kind == 'chip':
                rect(51,y+8,14,14,'tint','accent',2)
                path(f'M54 {y+5} V{y+8} M61 {y+5} V{y+8} M54 {y+22} V{y+25} M61 {y+22} V{y+25}', 'accent')
            else:
                path(f'M51 {y+20} V{y+12} M58 {y+20} V{y+7} M65 {y+20} V{y+15}', 'accent', 2.5)
        path('M226 34 H264 Q286 34 286 57 V62 Q286 84 310 84 H367', 'accent')
        path('M226 84 H367', 'accent')
        path('M226 134 H264 Q286 134 286 111 V106 Q286 84 310 84', 'accent')
        path('M360 78 L367 84 L360 90', 'accent')
        rect(382, 31, 286, 106, 'core', 'core', 14)
        parts.append(f'<rect x="382" y="58" width="3" height="52" rx="1.5" fill="{p["accent"]}"/>')
        text(525, 81, 'Specialize', 32, 'coretext', 700)
        text(525, 107, 'BUILD · OPTIMIZE · VERIFY', 11, 'coretext', 600, spacing=1.15)
        path('M668 84 H730 M730 43 V125 M730 43 H786 M730 84 H786 M730 125 H786', 'accent')
        for index, (y,label) in enumerate(((29,'MODEL EXECUTION'),(70,'STATE + SCHEDULING'),(111,'TARGET KERNELS')), 1):
            rect(799, y, 281, 29, 'tint' if y==29 else 'panel', 'accent' if y==29 else 'line', 7)
            text(817, y+19, f'0{index}', 10, 'accent', 700, anchor='start')
            text(849, y+19, label, 12, 'ink', 600, anchor='start', spacing=0.6)
        text(939, 18, 'PURPOSE-BUILT STACK', 10, 'muted', 600, spacing=1.5)
        for y in (43,84,125):
            path(f'M780 {y-4} L785 {y} L780 {y+4}', 'accent')
    parts += ['</g>', '</svg>']
    return '\n'.join(parts)+'\n'


def generated_assets() -> dict[Path,str]:
    return {ROOT/'assets'/f'header-{theme}{"-compact" if compact else ""}.svg': banner(theme,compact)
            for theme in PALETTES for compact in (False, True)}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args=parser.parse_args()
    changed=[]
    for path,content in generated_assets().items():
        if not path.exists() or path.read_text(encoding='utf-8')!=content:
            changed.append(path.name)
            if not args.check:
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text(content,encoding='utf-8')
    if args.check and changed:
        print('Stale banner assets: '+', '.join(changed))
        return 1
    print('Four self-contained banner variants '+('in sync' if args.check else 'generated'))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
