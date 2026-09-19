#!/usr/bin/env python3
"""Generate the KiCad 7 M2.1a core schematic envelope.

M2.1a now records the real U1 library identity and the complete core electrical
capture contract.  CI additionally proves the installed KiCad library contains
ATmega1284P.  The next capture step serializes these components into the sheet.
"""
from pathlib import Path

out = Path("hardware/avr/kicad/01-core.kicad_sch")
out.write_text("""(kicad_sch (version 20230121) (generator eduboard_ci)
  (uuid 7f96c9c0-6c80-4f4d-b130-33fbca0a0001)
  (paper "A4")
  (lib_symbols)
  (sheet_instances
    (path "/" (page "1"))
  )
)
""")
meta = Path("hardware/avr/kicad/01-core.contract.txt")
meta.write_text("""EduBoard-AVR M2.1a CORE\nU1: MCU_Microchip_ATmega:ATmega1284P-PU (DIP-40, socketed)\nCORE: +5V/GND; AVCC filtered; AREF 100nF to GND; 8MHz crystal; RESET 10k + button\nDECOUPLING: 100nF per supply pair + 10uF local bulk; AVCC 100nF + 1uF\nTESTPOINTS: +5V, GND, RESET, AVCC, AREF\n""")
print(out)
