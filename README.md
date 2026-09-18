# EduBoard

EduBoard is a family of maker-friendly open-hardware teaching boards for learning microcontrollers from the silicon up.

The family is designed around three reference targets:

- **EduBoard-AVR** — ATmega1284P-PU
- **EduBoard-8051** — classic 8051-compatible MCU (final reference part to be selected)
- **EduBoard-RP** — RP2040

All three boards should expose as close to the same pedagogical peripheral set and physical conventions as practical, so students can focus on architectural differences instead of relearning the trainer hardware.

## Design goals

- Beginner-friendly and maker-friendly first; cost second.
- Open hardware suitable for fabrication by services such as PCBWay/JLCPCB and for local assembly.
- Two-layer PCB where practical.
- Through-hole parts where they materially improve learning, repairability, or hand assembly.
- Socketed DIP MCU where the target device permits it.
- Large, readable silkscreen labels and clearly grouped functional blocks.
- Test points for important power, clock, reset, serial, and bus signals.
- Common naming and connector conventions across AVR, 8051, and RP variants.
- Hardware should support the majority of GPIO, timer/PWM, interrupt, UART, SPI, I2C/TWI, ADC, display, and basic embedded-systems labs used by the associated courses.
- Arduino compatibility is desirable where it does not compromise the educational design.

## Common teaching peripherals

The target common set is:

- 8 user LEDs
- 4 user pushbuttons
- configurable DIP switches
- one potentiometer / analog source where the MCU supports ADC
- piezo buzzer
- RGB LED
- 4-digit 7-segment display
- character LCD header
- UART header(s)
- SPI header
- I2C/TWI header
- general-purpose expansion GPIO
- programming/debug connector appropriate to the target MCU
- reset and target-specific boot/program controls
- small prototyping/expansion area where practical

Peripheral blocks should be disconnectable by jumper, solder bridge, or equivalent when they would otherwise consume pins needed for a lesson.

## Course relationship

- **EduAVR** uses ATmega1284P-PU as its single primary MCU. Other AVR devices belong in a porting/application appendix.
- **Edu8051** will use one selected classic 8051-compatible MCU as its single primary MCU. Other derivatives belong in an appendix.
- **EduRP** is intended as a shorter transition course for students who already understand MCU fundamentals from EduAVR or Edu8051, using RP2040 as the primary MCU.

## Licensing

EduBoard follows the Ploos-AS hardware licensing standard:

- hardware, PCB design files and HDL/gateware: **CERN-OHL-P-2.0**
- software, firmware, scripts and tooling: **MIT**
- course/documentation content may use **CC BY-SA 4.0** where appropriate

Each component directory must clearly state the applicable license.

## Status

M0 — family specification and architecture definition is in progress.
