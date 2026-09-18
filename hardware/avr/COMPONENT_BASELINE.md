# EduBoard-AVR M1.4 component baseline

Status: concrete baseline for schematic capture. Equivalent parts may be substituted only when electrical behaviour and teaching visibility remain equivalent.

## Core

- **U1:** ATmega1284P-PU, PDIP-40, socketed.
- **Y1:** 8 MHz fundamental-mode crystal, HC49/S-class THT footprint.
- **CXT1/CXT2:** load-capacitor footprints; final value calculated from selected crystal CL and PCB stray capacitance.
- **MCU decoupling:** 100 nF ceramic at each supply pair plus local bulk capacitor.
- **RESET:** 10 kΩ pull-up baseline + momentary pushbutton to GND.
- **ISP:** keyed 2x3 2.54 mm AVR ISP header.
- **JTAG:** 2.54 mm labelled header for PC2..PC5 plus reference power/GND.

## Power/input

v1 deliberately accepts a **regulated 5 V input** rather than hiding regulator design inside the first teaching board.

Baseline:
- 5 V input via clearly labelled connector/header;
- resettable polyfuse in the board-input path;
- reverse-polarity protection using a low-loss P-channel MOSFET topology or equivalent;
- TVS footprint optional/DNP for harsh-use experiments;
- 47 µF bulk + 100 nF local input bypass;
- power LED with low-current resistor;
- +5V and GND test points.

USB power/data is not required for v1. This keeps the board architecture understandable and avoids an unnecessary USB bridge MCU.

## RS-232

- **U_RS232:** MAX232A-compatible, 5 V, DIP-16 preferred.
- Use the capacitor network required by the exact selected device; do not assume legacy 1 µF values when an A-grade device specifies smaller capacitors.
- **J_RS232:** DE-9 male, default **DTE** convention.
- Minimum signals: TXD, RXD, GND.
- RTS/CTS footprints may be reserved only if routing/cost is low; they are not a v1 requirement.
- PD2/PD3 routing uses removable shunts so USART1/INT0/INT1 can be reclaimed.

## LED bank

- Eight diffused THT LEDs.
- 1 kΩ baseline series resistors, subject to selected LED Vf/current review.
- Prefer a removable SIP resistor network or jumper-isolated common path so the complete bank can be disconnected from PA0..PA7.

## RGB PWM section

Use a common-anode or common-cathode diffused THT RGB LED with three discrete small-signal transistor stages.

Baseline driver class:
- 2N7000-class small N-channel MOSFETs where suitable, or common NPN parts if BOM availability is better;
- per-channel LED resistor;
- optional gate/base pulldown as required.

MCU PWM outputs remain PD4/OC1B, PD5/OC1A, PD7/OC2A.

## Buzzer

- passive piezo element, not an active fixed-frequency buzzer;
- small NPN or N-MOSFET low-side driver;
- PB3/OC0A input;
- disconnect jumper.

The firmware must generate the tone.

## Four-digit seven-segment display

Use a common-cathode four-digit multiplexed display.

Educational topology:
- MCU controls seven segment lines plus decimal point through current-limiting resistor network;
- a simple logic buffer/driver may protect GPIO if required by current analysis;
- each digit common gets a transistor driver;
- firmware performs multiplex scanning.

Do **not** use MAX7219/TM1637 or another smart display controller in the primary teaching path because that would hide multiplexing and timer/ISR behaviour.

Exact display part is selected during footprint/layout review to avoid vendor lock-in; use a common 12-pin through-hole footprint where possible.

## Character LCD

Standard HD44780-compatible 16x2 module header:
- 1x16, 2.54 mm;
- 4-bit mode taught by default;
- 10 kΩ contrast potentiometer footprint;
- backlight current path explicitly limited/switched as needed;
- shared GPIO isolated with jumpers.

## Switches and analog

- SW0..SW3: common THT tactile switches.
- DIP0..DIP3: 4-position THT DIP switch.
- ADC potentiometer: 10 kΩ linear THT potentiometer, PA0 connection disconnectable.
- TWI pull-ups: two 4.7 kΩ baseline resistors with removable enable links; final value remains bus/capacitance dependent.

## Headers and jumpers

Use 2.54 mm headers/shunts for educational signal selection. They are intentionally large and visible.

Every jumper must have a functional silkscreen label; avoid anonymous JP numbers as the only user-facing information.

## Procurement rule

Before release, every non-generic IC/module should have:
1. at least one primary manufacturer part;
2. at least one electrically compatible alternative where practical;
3. documented package/footprint constraints;
4. no dependence on a single PCB assembler's private parts catalogue.

## M1.4 result

**Component architecture: PASS for schematic start.**

Items intentionally deferred to schematic/layout review:
- exact crystal and calculated load capacitors;
- exact MAX232A-family manufacturer;
- exact RGB/display manufacturer part numbers;
- final transistor choices after worst-case current calculation;
- exact input connector/mechanical choice.

These are controlled substitutions, not unresolved architecture.
