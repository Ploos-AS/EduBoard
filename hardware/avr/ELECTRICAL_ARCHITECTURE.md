# EduBoard-AVR M1.2 electrical architecture

Target: ATmega1284P-PU, educational 5 V configuration, 8 MHz reference clock.

## Power

- Primary board rail: regulated 5 V.
- Provide reverse-polarity/input protection appropriate to the selected connector.
- Place 100 nF ceramic decoupling at each MCU supply pair, physically close to pins.
- Add local bulk capacitance at board power entry and near display/serial loads.
- Expose labelled +5V and GND test points.
- Power LED must not be confused with LED0..LED7.
- Do not power high-current display loads directly through MCU pins.

## AVCC and AREF

AVCC must be powered even when ADC is not used. Route it from +5 V through a documented analog-supply filtering option and decouple locally.

AREF gets its own test point and decoupling footprint. Do not hard-wire AREF to +5 V: firmware may select internal references. Any external-reference option must be explicit and protected against accidental contention.

## Clock

Course reference: 8 MHz external crystal.

Provide:
- crystal footprint at XTAL1/XTAL2;
- load-capacitor footprints selected from the crystal specification;
- short, symmetric traces;
- optional clock test point that does not unnecessarily load the oscillator.

Fuse settings are documentation, not assumptions embedded in hardware. Recovery/programming procedure must be written before fuse presets are published.

## Reset, ISP and JTAG

RESET:
- pull-up network;
- momentary reset button;
- labelled test point;
- routed to programming connector.

ISP:
- keyed 2x3 AVR ISP header;
- MOSI PB5, MISO PB6, SCK PB7, RESET, +5V, GND;
- SPI peripherals must not prevent programming.

JTAG:
- expose PC2/TCK, PC3/TMS, PC4/TDO, PC5/TDI plus power/ground on a documented header;
- switch circuitry on PC2..PC5 must disconnect cleanly.

## USART0 — TTL teaching interface

PD0/RXD0 and PD1/TXD0 go to a clearly labelled TTL header with GND and reference voltage. This is the default early-course serial interface.

Do not place RS-232 voltages on this header.

## USART1 — RS-232 / DE-9

PD2/RXD1 and PD3/TXD1 feed a selectable MAX232-class transceiver stage.

Baseline:
- 5 V transceiver compatible with the selected baud-rate range;
- required charge-pump capacitors per the chosen device datasheet;
- DE-9 connector;
- default DTE convention documented on schematic and silkscreen;
- TXD, RXD and GND mandatory;
- hardware handshaking not required for v1 unless cost/pin budget remains attractive;
- jumpers isolate the transceiver so PD2/PD3 remain usable as INT0/INT1.

A null-modem requirement must be documented rather than hidden in lab instructions.

## LED0..LED7

PA0..PA7 drive the educational LED bank through current-limiting resistors and a single obvious isolation mechanism.

Design goal: low enough LED current for eight simultaneous outputs without stressing MCU/package current limits. Exact resistor values are selected only after LED Vf and current-budget calculation.

The entire LED bank must disconnect for ADC use. PA0 potentiometer is independently disconnectable.

## RGB LED

PD4/OC1B, PD5/OC1A and PD7/OC2A provide real hardware-PWM channels.

Prefer transistor/MOSFET drive if the selected RGB device/current would make direct MCU loading pedagogically or electrically undesirable. Each channel gets explicit current limiting.

## Buzzer

PB3/OC0A drives a passive piezo path. Prefer a small transistor driver so timer labs exercise OC0A without placing an unnecessary load on the MCU pin. Make the path disconnectable.

## Four-digit seven-segment display

Do not consume twelve MCU pins permanently.

Preferred architecture:
- segment lines through a current-limited driver/buffer stage;
- digit commons through suitable transistor drivers;
- multiplexing remains firmware-controlled so timer/ISR labs stay educational;
- all display connections can be isolated from shared GPIO.

Avoid a smart display controller that hides multiplexing from the learner.

## HD44780 LCD

Provide a standard character-LCD header supporting 4-bit mode. Use selectable/shared GPIO rather than permanently reserving an entire port. Include contrast provision/header and document 5 V logic assumptions.

## Bus headers

SPI: dedicated labelled header on PB4..PB7 plus power/GND as appropriate.
TWI: PC0/SCL and PC1/SDA with removable pull-ups.
UART: TTL USART0 header as above.
All headers must state voltage domain on silkscreen.

## Protection and testability

- series/current limiting where educational peripherals require it;
- no hidden auto-direction circuitry on teaching buses;
- test points for +5V, GND, RESET, AREF and important serial/clock nodes;
- polarity/orientation markings for every connector and polarized part;
- optional peripheral sections should fail disconnected rather than monopolize MCU pins.

## Cost / maker target

Use common, inexpensive parts and through-hole packages where practical. Socket the ATmega1284P-PU. Prefer parts available from multiple suppliers. Avoid adding convenience ICs that obscure hardware concepts unless they solve a real electrical/current/pin-count problem.

## M1.2 result

**Electrical architecture: defined, pending component selection and current-budget calculation.**

Next gate: M1.3 selects concrete components/values and produces a preliminary BOM plus power/current budget before schematic capture.
