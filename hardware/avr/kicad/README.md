# EduBoard-AVR KiCad design

This directory is the canonical editable hardware source for EduBoard-AVR.

## M2 schematic structure

The design is split by function so learners can read it progressively:

1. `01-core.kicad_sch` — ATmega1284P, power pins, clock and reset.
2. `02-programming-debug.kicad_sch` — ISP and JTAG.
3. `03-gpio-inputs.kicad_sch` — LED bank, buttons, DIP switches and ADC potentiometer.
4. `04-serial.kicad_sch` — TTL UART and RS-232/DE-9.
5. `05-buses.kicad_sch` — SPI and TWI.
6. `06-output.kicad_sch` — RGB, buzzer and four-digit display.
7. `07-lcd-expansion.kicad_sch` — HD44780 and GPIO expansion.

The top-level sheet documents functional boundaries and board-wide nets.

## Rules

- KiCad source is canonical; generated PDFs/Gerbers are release artifacts.
- Use standard KiCad libraries where practical.
- Custom symbols/footprints must live in this repository.
- Do not hide educational signal ownership behind opaque net names.
- Every disconnectable teaching peripheral must be obvious in both schematic and silkscreen.
- ERC warnings require an explicit fix or documented justification.


## M2.1a CI qualification status

The canonical `01-core.kicad_sch` is currently validated on GitHub Actions by
KiCad parse/export, netlist generation, PDF export, and the EduBoard-specific
component/observability contract.

The Ubuntu runner package currently exposes `kicad-cli sch export` but not
`kicad-cli sch erc`. Therefore a green CI run is **not** an ERC qualification.
M2.1a remains open until the canonical schematic has passed ERC using a KiCad
CLI/runtime that supports schematic ERC. Do not waive or reinterpret this gate.
