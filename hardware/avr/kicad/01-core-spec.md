# EduBoard-AVR M2.1 — Core schematic specification

This document is the reviewed net-level specification used to capture the first KiCad schematic sheet. It intentionally precedes hand-authored `.kicad_sch` syntax so the electrical design can be reviewed independently of the CAD serialization.

## U1 — ATmega1284P-PU

- Device: ATmega1284P-PU
- Package: PDIP-40
- Socket: DIP-40
- Logic supply: +5V
- Reference clock: 8 MHz external crystal

All VCC/GND pins and the analog supply are connected explicitly. Port signals retain their MCU names for the downstream functional sheets.

## Digital supply

Each U1 digital supply connection receives local 100 nF ceramic decoupling to GND. Place capacitors physically adjacent to the corresponding supply pins during PCB layout.

A local 10 µF bulk capacitor is provided near U1 in addition to board-entry bulk capacitance.

## AVCC

AVCC is not left floating.

Baseline network:

`+5V -> FB1/ferrite-bead option -> AVCC`

with:
- C_AVCC1 = 100 nF ceramic from AVCC to GND;
- C_AVCC2 = 1 µF ceramic from AVCC to GND.

FB1 may initially be populated with a 0 Ω link during bring-up. This gives a visible, measurable boundary between digital and analog supply without making an unverified filter mandatory.

## AREF

AREF is routed as a dedicated net and test point.

Baseline:
- C_AREF = 100 nF from AREF to GND;
- no permanent resistor or trace from AREF to +5V;
- external-reference access, if exposed, must be clearly labelled and must not allow casual shorting against an internally selected reference.

This permits firmware-selected internal/reference modes without a hard-wired +5V conflict.

## Clock

Y1 is an 8 MHz fundamental-mode crystal between XTAL1 and XTAL2.

C_XTAL1 and C_XTAL2 are capacitor footprints to GND. Their value is marked **TBD from selected crystal CL**, not guessed in the schematic.

Placement rule:
- Y1 and both capacitors immediately adjacent to U1;
- short traces;
- no unrelated signals routed through oscillator area.

The board may expose a buffered/test-friendly clock observation point later, but no large raw test pad is placed directly on the oscillator node by default.

## Reset

RESET network:

`+5V -> R_RESET 10 kΩ -> RESET`

and:

`RESET -> SW_RESET momentary -> GND`

RESET also routes to:
- ISP sheet;
- labelled RESET test point.

An optional small capacitor footprint may be reserved but remains DNP unless a concrete requirement is established. Programming reliability takes priority over unnecessary reset delay.

## Core net contract

Outputs to other sheets:

- PA0..PA7
- PB0..PB7
- PC0..PC7
- PD0..PD7
- RESET
- AREF
- +5V
- GND

Functional aliases are assigned on downstream sheets so students can still correlate peripherals with physical ports.

## Assembly/test points

Required core test points:
- TP_5V
- TP_GND
- TP_RESET
- TP_AVCC
- TP_AREF

XTAL nodes are intentionally excluded from large/general-purpose test points to reduce oscillator loading.

## M2.1 review checklist

- [x] MCU/package identified.
- [x] 5 V supply architecture defined.
- [x] local digital decoupling defined.
- [x] AVCC explicitly powered and decoupled.
- [x] AREF not hard-wired to +5V.
- [x] 8 MHz crystal architecture defined.
- [x] crystal capacitor values deferred to actual crystal CL.
- [x] RESET pull-up/button/ISP path defined.
- [x] core test points defined.
- [x] downstream port-net contract defined.
- [x] exact U1 KiCad symbol/footprint resolved (`MCU_Microchip_ATmega:ATmega1284P-P`, value `ATmega1284P-PU`, `Package_DIP:DIP-40_W15.24mm`).
- [x] remaining passive/test-point KiCad symbols resolved and instantiated with standard KiCad library identities.
- [x] canonical schematic captured and qualified by KiCad 9 Hardware CI.
- [ ] physical values verified against selected manufacturer parts.

## Result

**M2.1 electrical core definition: PASS for KiCad capture.**

**M2.1a CAD capture: PASS.** The canonical schematic loads/renders and passes the repository Hardware CI under the official KiCad 9 container. Physical manufacturer-part/value verification remains an M2/Q0 activity.


## Course-gap requirements

The M2.1 core capture MUST implement the requirements from `hardware/avr/COURSE_GAP_REVIEW.md` that belong to the core/analog domain:

- labelled AREF, AVCC, GND/AGND and POT0/ADC0 observation points where practical;
- AREF/reference strategy explicit in schematic documentation;
- POT0/ADC0 isolation and external analog-input access are mandatory in the GPIO/analog sheet;
- retain +5V/GND test points;
- reserve a practical board-current measurement link/jumper if it does not complicate normal operation.

Later M2 sheets MUST preserve the review requirements for raw PWM observation/isolation, an interrupt-capable button path without sacrificing USART1, seven-segment segment/digit observation, TTL-vs-RS232 boundary visibility, and SPI/TWI test access.

The schematic freeze gate is course-driven: every BOARD or SIM → BOARD exercise must map to a documented MCU pin/peripheral, learner-visible connection, safe isolation mechanism for shared pins, and a practical observation point.


## Seed audit before clean capture

The temporary bootstrap sheet has now been inspected at symbol-instance level.
It must **not** be repaired in place:

- U1 is the one reusable semantic choice: standard KiCad
  `MCU_Microchip_ATmega:ATmega1284P-P`, value `ATmega1284P-PU`, with
  `Package_DIP:DIP-40_W15.24mm`.
- the current object labelled `R_RESET=10k` is actually a
  `Switch:SW_DIP_x02` instance;
- the current object labelled `FB1` is actually a `Device:C` instance with a
  capacitor footprint;
- the sheet still contains unrelated donor-board circuitry.

Therefore the clean capture must instantiate fresh standard-library resistor,
ferrite/link, capacitor, crystal, pushbutton and test-point symbols. Renaming
existing donor instances is explicitly rejected.
