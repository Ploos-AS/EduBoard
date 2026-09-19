# EduBoard Roadmap

## Delivery priority

**Boards first, lessons second.** Course development should be limited to material needed to validate hardware until the three reference boards have stable, qualified revisions. Avoid building a large lesson catalogue against moving hardware targets.

The critical path is:
1. EduBoard-AVR schematic → PCB → Q0 → prototype/Q2.
2. EduBoard-8051 architecture → schematic → PCB → Q0 → prototype/Q2.
3. EduBoard-RP architecture → schematic → PCB → Q0 → prototype/Q2.
4. Freeze the common peripheral/layout contract.
5. Resume broad course/lab production against the qualified boards.

Work may overlap where it shortens this path, but course expansion is not the priority.

## M0 — Family specification
- Define EduBoard goals and common peripheral contract.
- Establish naming and functional-block conventions.
- Establish licensing: CERN-OHL-P-2.0 hardware, MIT software/firmware.
- Define manufacturing and qualification deliverables.

## M1 — EduBoard-AVR architecture
- ATmega1284P-PU, socketed DIP-40.
- Map common peripherals to pins/timers/USART/SPI/TWI/ADC.
- Define power, clock, reset, ISP and expansion architecture.
- Produce pin allocation, electrical architecture and component baseline.
- **Status: architecture defined; CAD capture in progress.**

## M2 — EduBoard-AVR schematic and PCB
- Complete real KiCad schematic capture for all functional sheets.
- Run ERC in Hardware CI; no undocumented violations.
- Assign and validate footprints.
- Complete PCB layout and DRC.
- Generate fabrication files, BOM and assembly documentation.
- Add Q0 manufacturing-output checks.
- Produce schematic PDF and manufacturing artifacts in CI.

### M2 execution order
- M2.1a core CAD: MCU, power, AVCC/AREF, clock, reset.
- M2.2 programming/debug: ISP + JTAG.
- M2.3 GPIO/inputs: LEDs, buttons, DIP switches, potentiometer.
- M2.4 communications: TTL UART, MAX232/DE-9, SPI, TWI.
- M2.5 outputs: RGB, buzzer, 4-digit seven-segment, LCD, expansion.
- Course-gap freeze gate: `hardware/avr/COURSE_GAP_REVIEW.md` requirements must be mapped into the schematic before freeze.\n\nM2.6 whole-schematic ERC + footprint review.
- M2.7 PCB placement/routing + DRC.
- M2.8 fabrication pack + Q0 qualification.

## M3 — EduBoard-AVR physical qualification
- Assemble prototype.
- Validate rails, clock/reset and ISP.
- Qualify LED/switch, ADC, PWM/buzzer, RGB, seven-segment, LCD, USART0/1, SPI and TWI.
- Feed only hardware-stabilizing lessons learned back into EduAVR until board revision is frozen.
- Freeze a course-supported AVR board revision after Q2.

## M4 — EduBoard-8051 MCU selection and architecture
- Select one classic 8051-compatible MCU with strong open-toolchain support and sufficient course peripherals.
- Prefer socketed DIP and in-system programming.
- Map the common EduBoard Peripheral Contract.
- Preserve the family physical-layout language.
- Document differences where the architecture lacks an AVR/RP equivalent.

## M5 — EduBoard-8051 implementation
- Real KiCad schematic and ERC.
- PCB layout and DRC.
- Manufacturing outputs and Q0.
- Physical prototype and Q2 qualification.
- Freeze a course-supported 8051 board revision before broad Edu8051 lesson production.

## M6 — EduBoard-RP architecture
- RP2040 as the sole primary target.
- Decide module-based versus chip-on-board first revision based on maker friendliness, cost and educational visibility.
- Map common teaching peripherals plus RP2040-specific PIO/DMA/debug opportunities.
- Preserve family layout while making 3.3 V boundaries explicit.

## M7 — EduBoard-RP implementation
- Real KiCad schematic and ERC.
- PCB layout and DRC.
- Manufacturing outputs and Q0.
- Physical prototype and Q2 qualification.
- Freeze a course-supported RP board revision before broad EduRP lesson production.

## M8 — Family convergence
- Align connector placement, silkscreen, lab names and peripheral behaviour across all three boards.
- Verify the same representative labs can be expressed on all applicable variants.
- Freeze Peripheral Contract v1.
- Publish family documentation and manufacturing packs.

## M9 — Course expansion
Only after stable board revisions:
- expand EduAVR lessons against EduBoard-AVR;
- build the full Edu8051 beginner course against EduBoard-8051;
- build the shorter EduRP transition course against EduBoard-RP;
- publish side-by-side architecture comparison labs.

## M10 — Production and distribution
- Validate multiple PCB manufacturers where practical.
- Document costed BOM alternatives.
- Add clearly disclosed optional affiliate/order links without restricting access to source/manufacturing files.
- Define revisioning and compatibility policy for course material.
