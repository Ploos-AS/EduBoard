#!/usr/bin/env python3
"""Generate the real EduBoard-AVR M2.1a core schematic.

Circuit Synth is used only as a deterministic KiCad serializer.  The circuit
definition here is the reviewable source of truth.
"""
from pathlib import Path
import shutil
raise SystemExit('Retired: canonical KiCad schematic is maintained directly and validated by kicad-cli.')\n# Historical Circuit Synth implementation retained below for reference only.\nfrom circuit_synth import circuit, Component, Net

@circuit(name="edu_board_avr_core")
def core():
    u1=Component(symbol="MCU_Microchip_ATmega:ATmega1284P-PU",ref="U1",value="ATmega1284P-PU",footprint="Package_DIP:DIP-40_W15.24mm")
    r1=Component(symbol="Device:R",ref="R1",value="10k",footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal")
    y1=Component(symbol="Device:Crystal",ref="Y1",value="8MHz",footprint="Crystal:Crystal_HC49-U_Vertical")
    c1=Component(symbol="Device:C",ref="C1",value="100nF",footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm")
    c2=Component(symbol="Device:C",ref="C2",value="100nF",footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm")
    c3=Component(symbol="Device:C",ref="C3",value="100nF",footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm")
    c4=Component(symbol="Device:C",ref="C4",value="1uF",footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm")
    c5=Component(symbol="Device:C",ref="C5",value="10uF",footprint="Capacitor_THT:C_Radial_D5.0mm_H5.0mm_P2.00mm")
    c6=Component(symbol="Device:C",ref="C6",value="22pF",footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm")
    c7=Component(symbol="Device:C",ref="C7",value="22pF",footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm")
    c8=Component(symbol="Device:C",ref="C8",value="100nF",footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm")

    vcc=Net(name="+5V"); gnd=Net(name="GND"); reset=Net(name="RESET")
    xtal1=Net(name="XTAL1"); xtal2=Net(name="XTAL2"); avcc=Net(name="AVCC"); aref=Net(name="AREF")

    # ATmega1284P-PU DIP-40: VCC=10, GND=11/31, XTAL2=12,
    # XTAL1=13, AVCC=30, AREF=32, RESET=9.
    vcc += u1[10]; gnd += u1[11]; gnd += u1[31]
    reset += u1[9]; xtal2 += u1[12]; xtal1 += u1[13]
    avcc += u1[30]; aref += u1[32]

    # RESET pull-up.
    vcc += r1[1]; reset += r1[2]

    # 8 MHz crystal and load capacitors.
    xtal1 += y1[1]; xtal2 += y1[2]
    xtal1 += c6[1]; gnd += c6[2]
    xtal2 += c7[1]; gnd += c7[2]

    # Core VCC decoupling + local bulk.
    vcc += c1[1]; gnd += c1[2]
    vcc += c2[1]; gnd += c2[2]
    vcc += c5[1]; gnd += c5[2]

    # AVCC filter placeholder for M2.1a: explicit AVCC net with local bypass.
    # Series ferrite/0R selection is finalized with the exact component in M2.1b.
    vcc += c3[1]; gnd += c3[2]
    avcc += c4[1]; gnd += c4[2]

    # AREF is never hard-wired to +5V.
    aref += c8[1]; gnd += c8[2]

if __name__=="__main__":
    out=Path("build/m2_1a")
    if out.exists(): shutil.rmtree(out)
    out.mkdir(parents=True)
    obj=core()
    obj.generate_kicad_project(project_name="edu_board_avr_core",output_dir=str(out),placement_algorithm="simple",generate_pcb=False)
    candidates=list(out.rglob("*.kicad_sch"))
    if not candidates:
        raise SystemExit("Circuit Synth produced no .kicad_sch")
    dst=Path("hardware/avr/kicad/01-core.kicad_sch")
    shutil.copyfile(candidates[0],dst)
    sch=dst.read_text()
    required=['ATmega1284P-PU','Device:C','Device:R','Device:Crystal','(symbol','(wire']
    missing=[x for x in required if x not in sch]
    if missing: raise SystemExit("M2.1a generated capture missing: "+", ".join(missing))
    print("PASS: generated real M2.1a KiCad capture:",dst)
