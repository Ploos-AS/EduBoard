# EduBoard-AVR M1.3 preliminary BOM and current budget

Status: engineering baseline for schematic capture, not a purchasing release.

## Component direction

| Function | Baseline part / class | Package direction | Rationale |
| --- | --- | --- | --- |
| MCU | ATmega1284P-PU | DIP-40 + socket | reference course MCU; replaceable |
| clock | 8 MHz crystal | HC49/S or similar THT | visible, inexpensive, easy to replace |
| RS-232 | MAX232-compatible 5 V transceiver | DIP-16 preferred | understandable charge-pump interface |
| LED bank | 8 standard low-current LEDs | 3/5 mm THT | visible GPIO teaching |
| LED resistors | 1 kΩ baseline at 5 V | resistor network or THT | roughly 2–3 mA/LED depending Vf |
| switches | 4 momentary buttons | THT | GPIO/interrupt labs |
| config | 4-position DIP switch | THT | static input labs |
| analog | 10 kΩ potentiometer | THT | ADC source |
| RGB | common-anode/cathode LED + drivers | THT | timer/PWM labs |
| buzzer | passive piezo + transistor | THT | timer/audio without MCU loading |
| numeric display | 4-digit 7-segment | THT | multiplexing lab |
| segment drive | resistor network + transistor/buffer stage | mixed/THT preferred | control display current |
| LCD | 1x16/2x8-style header as required by selected module | 2.54 mm | HD44780 4-bit lab |
| ISP | AVR 2x3 keyed header | 2.54 mm | standard programming |
| JTAG | labelled header | 2.54 mm | optional debugging |
| buses | UART/SPI/TWI/GPIO headers | 2.54 mm | breadboard/logic-analyzer friendly |
| isolation | jumpers + removable shunts | 2.54 mm | visible peripheral ownership |
| decoupling | 100 nF per IC supply pair | ceramic | local HF decoupling |
| bulk | 10–47 µF class | electrolytic | local rail buffering |

Exact manufacturer part numbers remain open until availability/cost comparison and schematic footprint review.

## LED current baseline

At 5 V with a typical red LED around 2 V and 1 kΩ series resistance:

I ≈ (5 V - 2 V) / 1000 Ω ≈ 3 mA.

Eight LEDs simultaneously: approximately 24 mA.

This is deliberately a low-current educational target. Exact values must be recalculated for the selected LEDs and checked against ATmega1284P per-pin, port-group and total-current limits from the current datasheet.

## Preliminary load budget

This is a design budget, not a measured result.

| Load | Planning allowance |
| --- | ---: |
| ATmega1284P + oscillator | 20 mA |
| 8 user LEDs | 24 mA |
| power/status LEDs | 5 mA |
| RGB LED | 15 mA |
| MAX232-class section | 15 mA |
| LCD logic/backlight | 30 mA |
| 4-digit display, multiplexed average | 80 mA |
| buzzer driver | 10 mA |
| pull-ups/miscellaneous | 10 mA |
| external-header reserve | 100 mA |
| **planning total** | **309 mA** |

The display and external header dominate uncertainty. A **500 mA minimum board supply design target** is therefore sensible; a higher input rating may be selected to provide margin. MCU GPIO must never be treated as the source for the whole board load.

## Power architecture consequence

The board should accept a regulated 5 V input as the simplest guaranteed path. If USB or higher-voltage input is added later, its regulator/protection path must comfortably meet the selected design current with thermal margin.

External peripherals should have an explicit current limit/budget in the user documentation.

## Cost discipline

Target inexpensive generic components available from multiple distributors. The first cost goal is **maker-friendly and educational**, not minimum PCB area or minimum assembly count.

Cost tracking should separate:
- bare PCB;
- core MCU/power/clock/programming BOM;
- teaching peripherals;
- optional RS-232 section;
- connectors/socket/mechanical parts.

This allows a future Base and Full kit without changing the learning architecture.

## BOM tiers

**Core:** MCU/socket, clock, power/decoupling, reset, ISP, essential headers.

**Teaching:** LEDs, switches, DIP switch, potentiometer, RGB, buzzer, display interfaces.

**Full:** four-digit display, RS-232 transceiver + DE-9, all isolation jumpers and optional debug connectors.

The PCB should support the Full configuration while allowing Core/Teaching builds to leave optional footprints unpopulated.

## M1.3 gate

PASS as a preliminary architecture budget.

Before manufacturing release:
1. choose exact display and RGB topology;
2. choose exact MAX232-compatible device and capacitor values;
3. calculate MCU absolute/current-group limits against every directly driven load;
4. select input protection/power connector;
5. select exact footprints;
6. price BOM from at least two practical supply channels;
7. verify all optional-unpopulated configurations are electrically sane.
