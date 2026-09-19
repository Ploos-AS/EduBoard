#!/usr/bin/env python3
"""Generate the minimal KiCad 7 schematic envelope used for M2.1a.

This intentionally contains no electrical symbols yet. Its purpose is to
establish a syntax-valid canonical sheet before component capture.
"""
from pathlib import Path

out = Path("hardware/avr/kicad/01-core.kicad_sch")
out.write_text("""(kicad_sch (version 20230121) (generator eeschema)
  (uuid 7f96c9c0-6c80-4f4d-b130-33fbca0a0001)
  (paper "A4")
  (lib_symbols)
  (sheet_instances
    (path "/" (page "1"))
  )
)
""")
print(out)
