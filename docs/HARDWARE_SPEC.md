# EduBoard Common Hardware Specification v0.1

This document defines the common educational hardware contract for the EduBoard family.

## Variants

| Board | Primary MCU | Course |
| --- | --- | --- |
| EduBoard-AVR | ATmega1284P-PU | EduAVR |
| EduBoard-8051 | TBD classic 8051-compatible part | Edu8051 |
| EduBoard-RP | RP2040 | EduRP |

## Common peripheral contract

Each board should implement, or provide a directly usable equivalent for:

1. **Digital output bank** — eight individually controllable LEDs named LED0..LED7.
2. **Digital input bank** — four momentary pushbuttons named SW0..SW3.
3. **Configuration switches** — at least four static switch inputs, preferably a DIP switch block.
4. **Analog source** — potentiometer routed to a documented ADC input when the target MCU provides ADC.
5. **PWM/audio** — passive piezo buzzer on a PWM/timer-capable pin.
6. **RGB output** — one RGB LED with channels individually accessible.
7. **Numeric display** — four-digit seven-segment display, preferably multiplexed so timer labs can drive it directly.
8. **Character display** — standard header suitable for HD44780-compatible character LCD modules.
9. **UART** — clearly labelled TTL-level serial header; expose additional UARTs where the MCU provides them.
10. **RS-232 / DE-9 bonus interface** — where board area and cost permit, provide a true RS-232 interface using a documented level-transceiver stage between an MCU UART and a DE-9 connector. Keep a TTL UART header available in parallel or via explicit routing selection. The RS-232 section must be disconnectable so it cannot monopolize the UART. On multi-UART MCUs, prefer dedicating one UART to TTL/USB-terminal work and another to RS-232.
11. **SPI** — dedicated labelled SPI header.
12. **I2C/TWI** — dedicated labelled bus header with configurable pull-ups.
13. **GPIO expansion** — expose unused and shared GPIO on headers.
14. **Programming/debug** — native programming/debug connector for the target architecture.
15. **Reset** — physical reset control and test point.
16. **Power** — clearly labelled power input and rails with test points.

## Educational disconnectability

On-board peripherals must not permanently hide important MCU pins. Shared peripherals should be separable with jumpers, removable shunts, DIP switches, solder bridges, or similarly obvious mechanisms.

The schematic and silkscreen must make pin sharing visible to the learner.

## Electrical design principles

- Protect MCU pins with appropriate LED resistors and driver stages where loads demand them.
- Do not connect true RS-232 voltage levels directly to TTL UART pins.
- A DE-9 serial connector, when fitted, must use a proper RS-232 transceiver (MAX232-class or equivalent) and clearly document DTE/DCE role, TX/RX/GND pins, handshake support, and any null-modem requirement.
- Prefer jumpers or similarly obvious routing controls between MCU UART, TTL header and RS-232 transceiver so students can inspect and change the signal path.
- Include local decoupling at every IC and sensible bulk capacitance at board power entry.
- I2C/TWI pull-ups should be removable/configurable.
- Prefer 5 V tolerant educational interfaces only where supported by the chosen MCU; otherwise label voltage domains prominently.
- Avoid opaque support MCUs unless their function is optional and documented.

## Mechanical and maker requirements

- Prefer 2-layer PCB.
- Prefer large footprints and through-hole parts when this does not materially reduce capability.
- Use socketed DIP packages for ATmega1284P-PU and the 8051 target if available in suitable DIP form.
- RP2040 implementation may use a replaceable Pico-compatible module for the first revision if that significantly improves assembly and repairability.
- Large silkscreen labels, functional grouping, pin names, polarity marks, and connector orientation are mandatory.
- Include mounting holes and test points.

## Manufacturing deliverables

Each board variant should eventually ship with:

- editable KiCad source
- schematic PDF
- Gerber set
- drill files
- BOM
- pick-and-place/CPL where applicable
- assembly drawing
- interactive BOM if practical
- fabrication notes
- hand-assembly notes
- bring-up checklist
- electrical test procedure

Outputs should be usable with common PCB fabrication services without vendor lock-in.

## Arduino compatibility

Arduino compatibility is a bonus, not a design requirement. Where practical, provide a documented Arduino-compatible pin mapping or shield/header compatibility without compromising the register-level teaching goals.

## Qualification levels

- **Q0:** schematic/ERC/design-rule/static checks and manufacturing-output validation.
- **Q1:** simulated or bench-modelled functional verification where useful.
- **Q2:** assembled physical board qualification, including power, clock/reset, programming, GPIO, serial buses, displays, and representative peripherals.

No simulated result should be described as physical/electrical qualification.
