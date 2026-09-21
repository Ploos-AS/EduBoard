# KiCad 9 capture implementation note

M2.1a is qualified with the official KiCad 9 container used by Hardware CI.
The canonical `01-core.kicad_sch` must load, render, and pass ERC in that
environment; hand-waved text-only capture is not accepted.

## Required real capture set

- U1: `MCU_Microchip_ATmega:ATmega1284P-PU`
- decoupling/bulk capacitors using `Device:C`
- RESET pull-up using `Device:R`
- Y1 8 MHz using `Device:Crystal`
- AVCC filtering and AREF capacitor
- +5V/GND/RESET/AVCC/AREF test access
- explicit electrical nets, not descriptive text

## Canonical capture rule

`01-core.kicad_sch` is the canonical native capture. The old bootstrap generator
is a parser/load fixture only and MUST NOT overwrite the canonical schematic.
All instantiated M2.1a parts must use the standard KiCad library identities
validated by `tools/capture_core.py`; donor-board instances are not accepted.

## Qualification

A capture is not M2.1a PASS merely because strings occur in the file. The
generated sheet must load through `kicad-cli`, export to PDF, contain actual
placed symbols and connectivity, and later pass the applicable ERC gate.
