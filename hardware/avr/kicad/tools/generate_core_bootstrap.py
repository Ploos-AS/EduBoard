#!/usr/bin/env python3
"""Generate the KiCad 7 M2.1a core schematic envelope.

M2.1a now records the real U1 library identity and the complete core electrical
capture contract.  CI additionally proves the installed KiCad library contains
ATmega1284P.  The next capture step serializes these components into the sheet.
"""
from pathlib import Path

out = Path("hardware/avr/kicad/01-core.kicad_sch")
out.write_text("""(kicad_sch (version 20230121) (generator eeschema)
  (uuid 7f96c9c0-6c80-4f4d-b130-33fbca0a0001)
  (paper "A4")
  (lib_symbols)
  (text "EduBoard-AVR M2.1a CORE" (exclude_from_sim no) (at 25.4 25.4 0)
    (effects (font (size 1.27 1.27)) (justify left bottom)))
  (text "U1: MCU_Microchip_ATmega:ATmega1284P-PU (DIP-40, socketed)" (exclude_from_sim no) (at 25.4 30.48 0)
    (effects (font (size 1.27 1.27)) (justify left bottom)))
  (text "CORE: +5V/GND; AVCC filtered; AREF 100nF to GND; 8MHz crystal; RESET 10k + button" (exclude_from_sim no) (at 25.4 35.56 0)
    (effects (font (size 1.27 1.27)) (justify left bottom)))
  (text "DECOUPLING: 100nF per supply pair + 10uF local bulk; AVCC 100nF + 1uF" (exclude_from_sim no) (at 25.4 40.64 0)
    (effects (font (size 1.27 1.27)) (justify left bottom)))
  (text "TESTPOINTS: +5V, GND, RESET, AVCC, AREF" (exclude_from_sim no) (at 25.4 45.72 0)
    (effects (font (size 1.27 1.27)) (justify left bottom)))
  (sheet_instances
    (path "/" (page "1"))
  )
)
""")
print(out)
