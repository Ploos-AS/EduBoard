#!/usr/bin/env python3
"""Truthful M2.1a capture gate.

The committed KiCad sheet, not generated prose, is the source of truth.
Require placed component identities plus electrical primitives before allowing
KiCad syntax/PDF qualification to proceed.
"""
from pathlib import Path
import re

p=Path("hardware/avr/kicad/01-core.kicad_sch")
sch=p.read_text()
required=[
    'lib_id "MCU_Microchip_ATmega:ATmega1284P-PU"',
    'lib_id "Device:C"',
    'lib_id "Device:R"',
    'lib_id "Device:Crystal"',
    "(wire", "(junction", "(label",
]
missing=[x for x in required if x not in sch]
if missing:
    raise SystemExit("M2.1a real capture incomplete; missing: "+", ".join(missing))

# Reject a capture that only embeds library definitions but never places parts.
placed=re.findall(r'\(symbol\s+\n?\s*\(lib_id "([^"]+)"\)',sch)
for lib in ("MCU_Microchip_ATmega:ATmega1284P-PU","Device:C","Device:R","Device:Crystal"):
    if lib not in placed:
        raise SystemExit("M2.1a symbol is embedded but not placed: "+lib)

print("PASS: real M2.1a placed symbols and electrical primitives are present")
