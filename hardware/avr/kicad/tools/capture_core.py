#!/usr/bin/env python3
"""M2.1a capture helper.

Run in an environment with KiCad installed. It deliberately discovers the
installed KiCad symbol library rather than embedding an assumed symbol
serialization. The generated schematic is then qualified by kicad-cli ERC.
"""
from pathlib import Path
import glob, sys

roots = [
    "/usr/share/kicad/symbols",
    "/usr/share/kicad-nightly/symbols",
]
libs = []
for root in roots:
    libs += glob.glob(root + "/*.kicad_sym")

if not libs:
    raise SystemExit("KiCad symbol libraries not found")

needle = "ATmega1284P"
hits = []
for p in libs:
    try:
        text = Path(p).read_text(errors="ignore")
    except OSError:
        continue
    if needle in text:
        hits.append(p)

if not hits:
    raise SystemExit(f"{needle} not found in installed KiCad symbol libraries")

print("ATmega1284P symbol library candidates:")
for h in hits:
    print(h)
print("PASS: installed KiCad library contains the target MCU symbol.")
