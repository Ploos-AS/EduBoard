#!/usr/bin/env python3
"""M2.1a real-capture gate.

This gate prevents the project from calling M2.1a complete while the generated
KiCad sheet is still only an envelope.  It also records the exact component
set that must be serialized next.  Exit non-zero until real KiCad symbols are
present, so CI truthfully remains red during capture.
"""
from pathlib import Path

sch=Path("hardware/avr/kicad/01-core.kicad_sch").read_text()
required=["ATmega1284P", "Device:C", "Device:R", "Device:Crystal"]
missing=[x for x in required if x not in sch]
if missing:
    raise SystemExit("M2.1a real capture incomplete; missing KiCad symbols: "+", ".join(missing))
print("PASS: real M2.1a component identities are present")
