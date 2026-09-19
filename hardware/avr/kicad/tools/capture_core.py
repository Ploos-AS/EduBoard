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


# M2.1a clean-capture inventory.  This is deliberately machine-readable so the
# CI/capture work has one explicit source of truth while the native KiCad sheet
# is rebuilt.
CORE_CAPTURE = {
    "mcu": {"ref": "U1", "value": "ATmega1284P-PU", "footprint": "Package_DIP:DIP-40_W15.24mm"},
    "clock": {"ref": "Y1", "value": "8MHz", "load_caps": "TBD_FROM_SELECTED_CRYSTAL_CL"},
    "reset": {"resistor": ("R_RESET", "10k"), "switch": "SW_RESET"},
    "analog_supply": {"link": "FB1", "decoupling": [("C_AVCC1", "100nF"), ("C_AVCC2", "1uF")]},
    "aref": {"decoupling": ("C_AREF", "100nF"), "hardwired_to_5v": False},
    "digital_decoupling": [("C_VCC1", "100nF"), ("C_VCC2", "100nF"), ("C_BULK", "10uF")],
    "testpoints": ["TP_5V", "TP_GND", "TP_RESET", "TP_AVCC", "TP_AREF"],
    "forbidden_seed_content": ["CC1101", "USB_B_Mini", "Y2", "boards:"],
}

print("M2.1a clean-capture inventory:")
for key, value in CORE_CAPTURE.items():
    print(f"{key}: {value}")
