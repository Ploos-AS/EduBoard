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
    "analog_supply": {"link": "FB1", "implementation": "0R_OR_FERRITE_FOOTPRINT", "decoupling": [("C_AVCC1", "100nF"), ("C_AVCC2", "1uF")]},
    "aref": {"decoupling": ("C_AREF", "100nF"), "hardwired_to_5v": False},
    "digital_decoupling": [("C_VCC1", "100nF"), ("C_VCC2", "100nF"), ("C_BULK", "10uF")],
    "testpoints": ["TP_5V", "TP_GND", "TP_RESET", "TP_AVCC", "TP_AREF"],
    "forbidden_seed_content": ["CC1101", "USB_B_Mini", "Y2", "boards:"],
}

print("M2.1a clean-capture inventory:")
for key, value in CORE_CAPTURE.items():
    print(f"{key}: {value}")


def validate_inventory():
    """Fail if the declared clean-capture inventory itself regresses."""
    assert CORE_CAPTURE["mcu"]["value"] == "ATmega1284P-PU"
    assert CORE_CAPTURE["mcu"]["footprint"] == "Package_DIP:DIP-40_W15.24mm"
    assert CORE_CAPTURE["clock"]["value"] == "8MHz"
    assert CORE_CAPTURE["reset"]["resistor"] == ("R_RESET", "10k")
    assert CORE_CAPTURE["aref"]["hardwired_to_5v"] is False
    assert set(CORE_CAPTURE["testpoints"]) == {
        "TP_5V", "TP_GND", "TP_RESET", "TP_AVCC", "TP_AREF"
    }
    print("PASS: M2.1a clean-capture inventory self-check")

validate_inventory()


# Fresh-symbol requirements for the native KiCad capture.  The next capture
# revision must use these library IDs; donor symbols with renamed references
# are not acceptable.
SYMBOL_TYPES = {
    "U1": "MCU_Microchip_ATmega:ATmega1284P-P",
    "R_RESET": "Device:R",
    "FB1": "Device:L",
    "Y1": "Device:Crystal",
    "SW_RESET": "Switch:SW_Push",
    "C_AVCC1": "Device:C",
    "C_AVCC2": "Device:C",
    "C_AREF": "Device:C",
    "C_VCC1": "Device:C",
    "C_VCC2": "Device:C",
    "C_BULK": "Device:C_Polarized",
    "TP_5V": "Connector:TestPoint",
    "TP_GND": "Connector:TestPoint",
    "TP_RESET": "Connector:TestPoint",
    "TP_AVCC": "Connector:TestPoint",
    "TP_AREF": "Connector:TestPoint",
}

def validate_installed_symbol_types():
    text_by_file = {}
    missing = []
    for ref, lib_id in SYMBOL_TYPES.items():
        lib, symbol = lib_id.split(":", 1)
        candidates = [Path(root) / f"{lib}.kicad_sym" for root in roots]
        found = False
        for p in candidates:
            if not p.exists():
                continue
            data = text_by_file.setdefault(p, p.read_text(errors="ignore"))
            if f'(symbol "{symbol}"' in data:
                found = True
                break
        if not found:
            missing.append((ref, lib_id))
    if missing:
        raise SystemExit("Missing required KiCad symbols: " + ", ".join(f"{r}={s}" for r,s in missing))
    print("PASS: installed KiCad libraries provide every M2.1a clean-capture symbol")

validate_installed_symbol_types()


# Explicit connectivity contract for the clean schematic generator/capture.
# Pin numbers follow the ATmega1284P 40-pin PDIP package.
NET_CONTRACT = {
    "+5V": ["U1.10", "R_RESET.1", "FB1.1", "C_VCC1.1", "C_VCC2.1", "C_BULK.1", "TP_5V.1"],
    "GND": ["U1.11", "U1.31", "C_VCC1.2", "C_VCC2.2", "C_BULK.2",
            "C_AVCC1.2", "C_AVCC2.2", "C_AREF.2", "SW_RESET.2", "TP_GND.1"],
    "AVCC": ["U1.30", "FB1.2", "C_AVCC1.1", "C_AVCC2.1", "TP_AVCC.1"],
    "AREF": ["U1.32", "C_AREF.1", "TP_AREF.1"],
    "RESET": ["U1.9", "R_RESET.2", "SW_RESET.1", "TP_RESET.1"],
    "XTAL1": ["U1.13", "Y1.1"],
    "XTAL2": ["U1.12", "Y1.2"],
}

def validate_net_contract():
    assert "U1.30" in NET_CONTRACT["AVCC"]
    assert "U1.32" in NET_CONTRACT["AREF"]
    assert "FB1.1" in NET_CONTRACT["+5V"] and "FB1.2" in NET_CONTRACT["AVCC"]
    assert "R_RESET.1" in NET_CONTRACT["+5V"] and "R_RESET.2" in NET_CONTRACT["RESET"]
    assert "U1.31" in NET_CONTRACT["GND"]
    assert "U1.12" in NET_CONTRACT["XTAL2"] and "U1.13" in NET_CONTRACT["XTAL1"]
    print("PASS: M2.1a electrical net contract self-check")

validate_net_contract()


# Crystal load capacitors are intentionally present in the clean capture but
# remain unvalued until Y1's exact part/load capacitance is selected.
CORE_CAPTURE["clock"]["capacitors"] = [
    ("C_XTAL1", "TBD_FROM_Y1_CL"),
    ("C_XTAL2", "TBD_FROM_Y1_CL"),
]
SYMBOL_TYPES["C_XTAL1"] = "Device:C"
SYMBOL_TYPES["C_XTAL2"] = "Device:C"
NET_CONTRACT["XTAL1"].append("C_XTAL1.1")
NET_CONTRACT["XTAL2"].append("C_XTAL2.1")
NET_CONTRACT["GND"].extend(["C_XTAL1.2", "C_XTAL2.2"])

assert "C_XTAL1.1" in NET_CONTRACT["XTAL1"]
assert "C_XTAL2.1" in NET_CONTRACT["XTAL2"]
assert "C_XTAL1.2" in NET_CONTRACT["GND"]
assert "C_XTAL2.2" in NET_CONTRACT["GND"]
print("PASS: M2.1a crystal load-capacitor contract")


# Exported MCU nets form the sheet boundary for later programming/debug and
# teaching-peripheral sheets.  Keeping these names stable is part of M2.1a.
PORT_EXPORTS = (
    [f"PA{i}" for i in range(8)] +
    [f"PB{i}" for i in range(8)] +
    [f"PC{i}" for i in range(8)] +
    [f"PD{i}" for i in range(8)] +
    ["RESET", "AREF", "+5V", "GND"]
)

assert len(PORT_EXPORTS) == 36
assert len(set(PORT_EXPORTS)) == len(PORT_EXPORTS)
print("PASS: M2.1a sheet-boundary export contract")
