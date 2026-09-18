# EduBoard-AVR M1 pin allocation

Target: **ATmega1284P-PU (DIP-40)**. This is the reference MCU for EduAVR.

## Design rule

Native peripheral pins win over cosmetic convenience. On-board teaching peripherals must be disconnectable so the same pins can be reused in register-level labs.

## Reserved native interfaces

| Function | ATmega1284P signals | EduBoard use |
| --- | --- | --- |
| USART0 | PD0 RXD0, PD1 TXD0 | TTL serial / terminal header |
| USART1 | PD2 RXD1, PD3 TXD1 | optional MAX232-class RS-232 + DE-9 |
| TWI/I2C | PC0 SCL, PC1 SDA | labelled I2C header, removable pull-ups |
| SPI | PB4 SS, PB5 MOSI, PB6 MISO, PB7 SCK | SPI header and ISP where applicable |
| ADC | PA0..PA7 | analog header; PA0 potentiometer by default |
| RESET | RESET | reset button, programming and test point |
| clock | XTAL1/XTAL2 | socket-friendly crystal/resonator footprint |

## Teaching peripherals

Proposed default mapping for schematic capture:

| Peripheral | Default signals | Notes |
| --- | --- | --- |
| LED0..LED7 | PA0..PA7 through selectable links | LED bank must disconnect completely for ADC labs |
| SW0..SW3 | PC2..PC5 | active-low with documented pull-up strategy |
| DIP0..DIP3 | PC4..PC7 | overlaps SW2/SW3 intentionally; individually disconnectable |
| potentiometer | PA0 | removable/selectable connection |
| RGB LED | PB0..PB2 | choose timer/PWM-capable channels where practical after timer cross-check |
| buzzer | PB3 | disconnectable; timer-capable mapping to be verified before schematic freeze |
| 4-digit 7-segment | shared GPIO through driver stage | do not consume native serial/SPI/TWI permanently |
| HD44780 LCD | expansion/header mapping | 4-bit mode preferred; selectable/shared GPIO |
| TTL UART | PD0/PD1 | USART0 |
| RS-232 DE-9 | PD2/PD3 | USART1 via transceiver, disconnectable |
| SPI | PB4..PB7 | native SPI |
| TWI | PC0/PC1 | native TWI |
| GPIO expansion | all practical port signals | shared use labelled on silkscreen |

## Important M1 constraint

The LED bank on Port A is intentionally selectable rather than permanently attached. This lets early GPIO labs use an intuitive full 8-bit port while later ADC labs reclaim PA0..PA7 without LED loads affecting measurements.

Likewise, serial, display, switch and audio sections must use jumpers, resistor networks, DIP isolation or similarly understandable mechanisms. The learner should be able to turn EduBoard-AVR into a nearly bare ATmega1284P system without desoldering components.

## Power and clock direction

- Support a clearly documented 5 V educational configuration.
- Decouple every VCC/AVCC supply pin locally.
- AVCC and AREF require an explicitly documented analog-power/reference network.
- External clock footprint should support the course reference frequency; EduAVR currently uses 8 MHz in qualified examples.
- Do not freeze fuse recommendations until the clock/programming recovery procedure is documented.

## Programming

Expose the standard AVR ISP signals and RESET in a keyed, clearly labelled connector. Preserve compatibility with common AVR programmers and the user's STK500 workflow. Programming must remain possible with all teaching peripherals fitted.

## M1 schematic-freeze checks

Before drawing the production schematic:

1. verify every proposed mapping against the ATmega1284P datasheet;
2. cross-check OC/timer functions for RGB LED, buzzer and display multiplexing;
3. verify SPI/ISP coexistence;
4. verify AVCC/AREF requirements;
5. decide DTE/DCE role and DE-9 pinout;
6. choose the RS-232 transceiver;
7. choose display driver strategy;
8. confirm that isolation links leave native peripherals electrically usable;
9. estimate GPIO/current budget;
10. produce a pin-conflict matrix.

This document is an M1 allocation proposal, not yet a frozen schematic or electrically qualified design.
