# Schematic sheet plan

## Top level

Board-wide nets:
- +5V
- GND
- RESET
- AREF
- USART0_RX / USART0_TX
- USART1_RX / USART1_TX
- SPI_SS / SPI_MOSI / SPI_MISO / SPI_SCK
- TWI_SCL / TWI_SDA

Port-oriented labels remain visible where useful: PA0..PA7, PB0..PB7, PC0..PC7, PD0..PD7.

## 01 Core

Contains U1 ATmega1284P-PU, decoupling, AVCC/AREF network, 8 MHz crystal and reset network. Keep the MCU symbol central and readable rather than optimizing for minimum sheet area.

## 02 Programming/debug

Contains keyed AVR ISP and JTAG headers. Shared SPI and PC2..PC5/JTAG ownership is explicitly annotated.

## 03 GPIO/inputs

Contains disconnectable PORTA LED bank, SW0..SW3, DIP0..DIP3 and PA0 ADC potentiometer.

## 04 Serial

USART0 exposes TTL logic directly. USART1 feeds an isolatable MAX232A-class stage and DE-9 DTE connector.

## 05 Buses

Dedicated SPI header and TWI header. TWI pull-ups are removable.

## 06 Output

Hardware-PWM RGB, passive buzzer driver and firmware-multiplexed four-digit seven-segment display.

## 07 LCD/expansion

HD44780-compatible 4-bit interface and general GPIO expansion.

## Qualification gates

M2.1: core sheet.
M2.2: programming/debug.
M2.3: GPIO/inputs.
M2.4: serial/buses.
M2.5: output/display/LCD.
M2.6: whole-schematic ERC and peer-readable review.
