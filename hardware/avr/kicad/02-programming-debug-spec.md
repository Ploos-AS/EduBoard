# EduBoard-AVR M2.2 — Programming/debug schematic specification

Target: **ATmega1284P-PU**, 5 V EduBoard-AVR.

This sheet exposes the MCU's native ISP and JTAG interfaces without hiding the
signals behind convenience circuitry. Programming/debug must remain usable with
the teaching peripherals fitted, and shared peripherals must be disconnectable.

## AVR ISP

Use the standard keyed **2x3 AVR ISP** connector.

| ISP signal | MCU signal | DIP-40 pin |
| --- | --- | ---: |
| MISO | PB6/MISO | 7 |
| +5V / VTG | +5V | — |
| SCK | PB7/SCK | 8 |
| MOSI | PB5/MOSI | 6 |
| RESET | RESET | 9 |
| GND | GND | — |

Requirements:
- keyed/shrouded 2x3 header where practical;
- pin 1 clearly marked on schematic and silkscreen;
- +5V is target/reference voltage, not an undocumented alternate board supply;
- RESET is the same net as the M2.1a reset network;
- PB5/PB6/PB7 remain visible as native SPI signals;
- downstream SPI loads must be isolatable or electrically benign during ISP;
- compatible with common AVR programmers and the STK500 workflow.

## JTAG

Expose the ATmega1284P JTAG signals on a clearly labelled header.

| JTAG function | MCU signal | DIP-40 pin |
| --- | --- | ---: |
| TCK | PC2/TCK | 24 |
| TMS | PC3/TMS | 25 |
| TDO | PC4/TDO | 26 |
| TDI | PC5/TDI | 27 |
| VTREF | +5V | — |
| GND | GND | — |

Use a simple **2x3 JTAG teaching header** for v1 rather than introducing a
proprietary/debug-adapter dependency. Label both JTAG function and MCU port
signal in documentation/silkscreen.

Requirements:
- PC2..PC5 go directly to the header;
- SW/DIP circuitry that later shares PC2..PC5 must disconnect cleanly;
- no fixed pull network on this sheet that compromises GPIO/JTAG teaching;
- +5V is explicitly VTREF/reference power;
- GND is provided adjacent/clearly identifiable;
- pin 1/orientation is unambiguous.

## Sheet-boundary net contract

Inputs/shared nets:
- +5V
- GND
- RESET
- PB5 / MOSI
- PB6 / MISO
- PB7 / SCK
- PC2 / TCK
- PC3 / TMS
- PC4 / TDO
- PC5 / TDI

No signal is renamed in a way that hides its physical MCU port identity.

## Course/testability requirements

- ISP and JTAG connector pinouts must be printable in course material without a
  board-specific abstraction layer.
- Learners must be able to probe RESET, SCK, MOSI and MISO during programming.
- JTAG sharing with SW0..SW3/DIP circuitry is documented before M2.3 freeze.
- Programming remains possible with all normal board peripherals installed.
- Connector orientation and 5 V voltage domain must be obvious on silkscreen.

## M2.2 qualification gate

M2.2 is PASS when:
- the ISP and JTAG connectors are captured with standard KiCad symbols and
  assigned practical footprints;
- every connector pin maps to the documented ATmega1284P signal;
- shared-pin/isolation constraints are represented in the downstream contract;
- KiCad 9 loads/renders the sheet;
- ERC has no undocumented violations;
- Hardware CI validates the M2.2 net/pin contract.

