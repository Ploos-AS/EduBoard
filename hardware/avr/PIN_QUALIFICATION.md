# EduBoard-AVR M1.1 pin qualification

Source of truth: Microchip ATmega1284P datasheet, PDIP-40 pinout and alternate-function tables.

## Native-function cross-check

| Signal | Verified pin/function | Decision |
| --- | --- | --- |
| USART0 | PD0/RXD0, PD1/TXD0 | reserve for TTL terminal |
| USART1 | PD2/RXD1, PD3/TXD1 | reserve for RS-232/DE-9 |
| TWI | PC0/SCL, PC1/SDA | reserve for I2C/TWI |
| SPI | PB4/SS/OC0B, PB5/MOSI/ICP3, PB6/MISO/OC3A, PB7/SCK/OC3B | reserve as native SPI; shared timer functions documented |
| ADC | PA0..PA7 = ADC0..ADC7 | selectable LED bank only; PA0 also potentiometer |
| Timer0 PWM | PB3/OC0A, PB4/OC0B | PB3 suitable buzzer; PB4 conflicts with SPI SS |
| Timer1 PWM | PD5/OC1A, PD4/OC1B | keep available for timer/PWM labs |
| Timer2 PWM | PD7/OC2A, PD6/OC2B | keep available for timer/PWM/display experiments |
| Timer3 PWM | PB6/OC3A, PB7/OC3B | conflicts with SPI MISO/SCK |
| JTAG | PC2/TCK, PC3/TMS, PC4/TDO, PC5/TDI | switch bank must be disconnectable; preserve JTAG teaching/debug option |

## Corrections to initial allocation

The initial proposal placed the RGB LED on PB0..PB2. Those pins are not hardware PWM outputs on ATmega1284P. For a course board intended to teach hardware PWM, RGB should instead use real OC outputs.

Proposed RGB mapping:
- R = PD4 / OC1B
- G = PD5 / OC1A
- B = PD7 / OC2A

Proposed buzzer:
- PB3 / OC0A

PD6 / OC2B remains available for another timer/PWM lab and can be considered for display support.

This mapping deliberately avoids PB4/PB6/PB7 timer outputs because those pins are also the native SPI bus.

## Port C / JTAG conflict

PC2..PC5 are JTAG pins as alternate functions. Buttons or DIP switches may use them only through explicit isolation. The board must permit a learner to use JTAG without attached switch circuitry changing signal behaviour.

A likely layout is:
- PC0/PC1: TWI only, with removable pull-ups
- PC2..PC5: SW0..SW3 through isolation
- PC6/PC7: DIP/static inputs or expansion, while preserving TOSC1/TOSC2 documentation

Do not permanently load PC2..PC5.

## Port A dual use

PA0..PA7 form the cleanest full 8-bit GPIO bank and all eight are ADC inputs. Keep LED0..LED7 on this port only if the complete LED network can be disconnected as one obvious operation. PA0 potentiometer must be separately disconnectable.

This creates useful course progression:
1. early lab: PORTA as an 8-bit LED register;
2. later lab: disconnect LEDs;
3. ADC labs: PORTA becomes analog input bank.

## UART allocation

USART0 remains the simple TTL UART used by early serial labs.

USART1 is the preferred RS-232 path:
MCU PD2/PD3 <-> selectable routing <-> RS-232 transceiver <-> DE-9.

Both PD2 and PD3 also provide INT0/INT1 respectively, so the RS-232 section must disconnect cleanly for external-interrupt labs.

## Remaining schematic decisions

Before schematic freeze:
- choose RGB LED drive topology/current so OC outputs are not overloaded;
- choose seven-segment driver/multiplex topology rather than spending a large raw GPIO bank;
- choose MAX232-class transceiver and DTE/DCE DE-9 convention;
- choose AVCC filtering and AREF arrangement;
- verify ISP header/reset wiring and SPI loading;
- decide whether JTAG gets a dedicated header;
- calculate worst-case MCU/LED/display current;
- define isolation parts/jumpers consistently.

## Result

**M1.1 pin-function cross-check: PASS with corrections.**

The critical correction is RGB PWM relocation from PB0..PB2 to actual Output Compare pins. No production schematic is frozen by this document.
