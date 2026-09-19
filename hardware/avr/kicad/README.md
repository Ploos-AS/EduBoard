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

GitHub Actions now runs KiCad 9 and executes real `kicad-cli sch erc
--exit-code-violations` against `01-core.kicad_sch`.

The first real ERC run reported **0 errors and 73 warnings**. Those warnings are
dominated by library/footprint references inherited from the temporary external
seed schematic (including the custom `boards` library and unrelated circuitry).
This confirms that the seed must be replaced rather than warning-suppressed.

### Clean-capture acceptance gate

M2.1a remains open until `01-core.kicad_sch` is a native EduBoard capture that:

- contains only the ATmega1284P core, supply/decoupling, AVCC/AREF, 8 MHz clock,
  reset network, required test points, and intentional core net exports;
- uses standard KiCad symbols/footprints or repository-owned libraries only;
- contains no inherited USB, radio/CC1101, second oscillator, or other seed-board
  circuitry;
- passes KiCad 9 ERC with no undocumented warnings;
- exports successfully to PDF in CI.

Do not patch, exclude, or suppress the inherited seed warnings merely to obtain a
green run. The seed is a syntax/bootstrap aid, not an EduBoard design.
