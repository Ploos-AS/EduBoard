# KiCad 7 capture implementation note

M2.1a must use the KiCad 7 schematic grammar rather than hand-waving a text-only
capture. The authoritative format reference is KiCad's schematic file-format
documentation, and KiCad 7's own 7.0.9 demo schematics are the compatibility
fixtures for the `20230121` grammar.

## Required real capture set

- U1: `MCU_Microchip_ATmega:ATmega1284P-PU`
- decoupling/bulk capacitors using `Device:C`
- RESET pull-up using `Device:R`
- Y1 8 MHz using `Device:Crystal`
- AVCC filtering and AREF capacitor
- +5V/GND/RESET/AVCC/AREF test access
- explicit electrical nets, not descriptive text

## Generator rule

Generated schematics use `eduboard_ci` as their generator identifier. KiCad's
format documentation explicitly asks third-party writers not to identify
themselves as `eeschema`.

## Qualification

A capture is not M2.1a PASS merely because strings occur in the file. The
generated sheet must load through `kicad-cli`, export to PDF, contain actual
placed symbols and connectivity, and later pass the applicable ERC gate.
