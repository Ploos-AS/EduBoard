# EduBoard Peripheral Contract

The EduBoard family uses a common learner-facing hardware contract across CPU architectures.

The PCB implementations are electrically different, but a student moving between EduBoard-AVR, EduBoard-8051 and EduBoard-RP should recognize the board immediately and be able to repeat equivalent labs without relearning the lab platform.

## Reference variants

- **EduBoard-AVR:** ATmega1284P-PU, 5 V.
- **EduBoard-8051:** one selected 8051-compatible reference MCU; exact device is chosen before schematic work.
- **EduBoard-RP:** RP2040, 3.3 V logic.

## Required learner-facing peripherals

Every variant implements, where the MCU architecture permits:

- LED0..LED7 — eight individually controllable LEDs.
- SW0..SW3 — four momentary push-buttons.
- DIP0..DIP3 — four static switches.
- POT0 — analog potentiometer when ADC is available.
- RGB0 — individually controlled RGB LED.
- BUZZ0 — passive buzzer driven by firmware/timer output.
- DISP0 — four-digit seven-segment display suitable for firmware multiplexing.
- LCD0 — HD44780-compatible character LCD interface.
- UART0 — TTL serial interface.
- RS232 — DE-9 interface through a real RS-232 transceiver.
- SPI0 — labelled SPI interface when supported.
- I2C0 — labelled I2C/TWI interface when supported.
- GPIO — general expansion headers.
- RESET — accessible reset control.
- native programming/debug interface.
- labelled power, ground and useful test points.

## Physical-layout contract

As practical, all boards place equivalent learner-facing peripherals in the same regions and use the same names, orientation and visual conventions.

A learner should find LED3, SW1, POT0, UART0 or DISP0 in approximately the same physical place on every EduBoard.

Electrical necessities override cosmetic symmetry. 3.3 V and 5 V domains must never be made electrically unsafe merely to preserve layout.

## Peripheral ownership

On-board teaching peripherals must not permanently consume important MCU resources.

Use understandable isolation such as jumpers, shunts, resistor networks or solder bridges so native GPIO/peripheral pins can be reclaimed.

The board should be reducible to a near-bare MCU development platform without desoldering teaching peripherals.

## Lab portability

Courses should deliberately reuse equivalent experiments across architectures.

Examples:

- binary count on LED0..LED7;
- button polling and debounce;
- external interrupt;
- PWM fading on RGB0;
- timer-driven BUZZ0;
- UART echo;
- interrupt-driven UART/ring buffer;
- four-digit display multiplexing;
- ADC reading of POT0;
- SPI peripheral transaction;
- I2C peripheral transaction.

The *problem* and visible hardware behaviour remain comparable while the implementation exposes architectural differences.

## Architecture-specific teaching

The contract does not hide CPU differences.

Examples:
- AVR labs teach PORT registers, AVR timers, interrupt vectors and USART/SPI/TWI hardware.
- 8051 labs teach SFRs, classic port semantics, timers and the selected device's peripherals.
- RP2040 labs teach 32-bit MMIO, Cortex-M0+, NVIC, DMA, multicore and PIO where appropriate.

Course documentation must state when a feature is native, emulated, unavailable or materially different on a variant.

## Voltage contract

Connectors and silkscreen must identify logic voltage.

- AVR reference board: 5 V logic.
- 8051 board: determined by selected reference MCU.
- RP2040 board: 3.3 V logic.

Level translation is added where required. No common connector convention may imply that 5 V tolerance exists when it does not.

## Naming contract

Use stable learner-facing names in schematics, silkscreen and course material:

`LED0..7`, `SW0..3`, `DIP0..3`, `POT0`, `RGB0`, `BUZZ0`, `DISP0`, `LCD0`, `UART0`, `RS232`, `SPI0`, `I2C0`, `GPIO`, `RESET`.

MCU-native pin names remain visible alongside these aliases.

## Qualification

Each board is qualified independently.

A PASS on EduBoard-AVR does not qualify EduBoard-8051 or EduBoard-RP. Common labs may be reused as qualification scenarios, but electrical and physical Q2 evidence is variant-specific.

## Design rule

**Same lab platform, different architecture.**

That is a first-class requirement of the EduBoard family, not a cosmetic goal.
