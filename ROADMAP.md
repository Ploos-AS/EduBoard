# EduBoard Roadmap

## M0 — Family specification
- Define EduBoard goals and common peripheral contract.
- Establish naming and functional-block conventions.
- Establish licensing: CERN-OHL-P-2.0 hardware, MIT software/firmware.
- Define manufacturing and qualification deliverables.

## M1 — EduBoard-AVR architecture
- ATmega1284P-PU, socketed DIP-40.
- Map common peripherals to pins/timers/USART/SPI/TWI/ADC.
- Define power, clock, reset, ISP and expansion architecture.
- Produce first KiCad schematic and pin-allocation document.

## M2 — EduBoard-AVR PCB
- Complete PCB layout and DRC.
- Generate fabrication files, BOM and assembly documentation.
- Add Q0 manufacturing-output checks.

## M3 — EduBoard-AVR physical qualification
- Assemble prototype.
- Validate rails, clock/reset and ISP.
- Qualify LED/switch, ADC, PWM/buzzer, RGB, seven-segment, LCD, USART0/1, SPI and TWI.
- Feed lessons learned back into EduAVR course labs.

## M4 — EduBoard-8051 MCU selection and architecture
- Select one classic 8051-compatible MCU with strong open-toolchain support and sufficient course peripherals.
- Prefer socketed DIP and in-system programming.
- Map the same common teaching peripheral contract.
- Document differences where the architecture lacks an AVR/RP equivalent.

## M5 — EduBoard-8051 implementation
- Schematic, PCB, manufacturing outputs and Q0.
- Physical Q2 qualification.
- Feed board into Edu8051 course development.

## M6 — EduBoard-RP architecture
- RP2040 as the sole primary target.
- Decide module-based versus chip-on-board first revision based on maker friendliness, cost and educational visibility.
- Map common teaching peripherals plus RP2040-specific PIO/DMA/debug opportunities.

## M7 — EduBoard-RP implementation
- Schematic, PCB, manufacturing outputs and Q0.
- Physical Q2 qualification.
- Feed board into the shorter EduRP transition course.

## M8 — Family convergence
- Align connector placement, silkscreen, lab names and peripheral behaviour across all three boards.
- Publish side-by-side architecture comparison labs.
- Produce family documentation and manufacturing packs.

## M9 — Production and distribution
- Validate multiple PCB manufacturers where practical.
- Document costed BOM alternatives.
- Add clearly disclosed optional affiliate/order links without restricting access to source/manufacturing files.
- Define revisioning and compatibility policy for course material.
