# EduBoard-AVR course-driven gap review

This review feeds the current EduAVR exercises back into the board design before schematic freeze.

## Result

No fundamental missing peripheral has been found. The current peripheral contract supports the planned introductory EduAVR path, but the course review exposes several **requirements that must be made explicit before PCB freeze**.

## Requirements exposed by the labs

### 1. ADC/reference observability — required
ADC labs need more than POT0.

- Provide labelled **AREF, AVCC, AGND/GND and POT0/ADC0 test points** where practical.
- Make the selected reference strategy explicit in schematic/silkscreen/documentation.
- POT0 must remain disconnectable so ADC0 can accept an external source.
- Provide at least one convenient labelled analog-input point/header after POT0 is disconnected.

### 2. Timer/PWM observability — required
PWM, buzzer and timer labs need direct measurement.

- Provide labelled test points for the PWM outputs used by RGB0 and BUZZ0.
- A learner must be able to probe the **raw MCU timer output before/independent of the load driver** where practical.
- Preserve disconnect links so RGB/buzzer loads do not prevent timer-output experiments.

### 3. Interrupt-capable button path — required
The debounce/external-interrupt lab should not require improvised wiring.

- Ensure at least one normal learner button can be routed to a documented interrupt-capable input, or provide an obvious jumper path from a button to one.
- Do not permanently sacrifice USART1/RS232 merely to run the interrupt lesson.
- Label the interrupt-capable path in the course pin map.

### 4. Seven-segment measurement points — required
The multiplexing lab benefits from observing what the eye hides.

- Provide accessible/labelled segment and digit-select signals, at least through headers/test pads.
- The display driver must remain simple enough that students can correlate GPIO writes with segment/digit current paths.
- Keep the existing rule forbidding a smart display controller in the primary teaching path.

### 5. Serial visibility — required
USART labs should expose the distinction between MCU UART and RS-232 clearly.

- Keep TTL UART headers.
- Add/retain labelled probe points on MCU-side TX/RX and, for the RS-232 section, make the transceiver boundary obvious.
- Silkscreen/documentation must identify TTL logic versus true RS-232 levels.

### 6. Bus experiments — required
SPI and TWI labs should be easy to instrument.

- SPI0 and I2C0 headers must include convenient GND and reference power.
- TWI pull-ups remain removable.
- Prefer test access to SCK/MOSI/MISO/SS and SDA/SCL without requiring probes directly on MCU pins.

### 7. Power/current experiments — recommended
A board that teaches hardware/software relationships benefits from observable supply behavior.

- Retain +5V/GND test points.
- Consider a removable current-measurement link/jumper in the MCU/board supply path if it can be added without complicating normal use.
- This is recommended, not a v1 blocker.

### 8. External analog experiments — recommended
POT0 is sufficient for the first ADC lab, but later sensor/data-acquisition labs benefit from a small analog expansion area.

- Expose ADC-capable pins, +5V and GND together on a clearly labelled header.
- Do not require an on-board sensor for v1; external sensors are more flexible pedagogically.

## Not currently missing

The current design already provides the core facilities demanded by the reviewed labs:

- LED bank and buttons
- DIP switches
- POT0/ADC
- RGB PWM output
- passive timer-driven buzzer
- firmware-multiplexed four-digit seven-segment display
- HD44780 LCD header
- TTL UART and true RS-232/DE-9
- SPI and TWI/I2C
- GPIO expansion
- ISP/JTAG, reset, clock and power/test infrastructure

## Freeze rule

Before EduBoard-AVR schematic freeze, each EduAVR BOARD or SIM → BOARD exercise must map to:

1. a documented MCU peripheral/pin;
2. a learner-visible board connection;
3. a safe isolation/routing mechanism where the pin is shared;
4. a practical observation point for the phenomenon being taught.

A board feature is not course-ready merely because the MCU can perform it.
