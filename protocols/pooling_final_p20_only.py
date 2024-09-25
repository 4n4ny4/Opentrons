import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def get_values(*names):
    import json
    _all_values = json.loads("""{"protocol":"pooling","csv_samp":"DNA Index pooling Plate #0139964_Set3,,,,\\nSource Plate location: DNA,SampleID,Conc. (ng/ul),Volume Needed for pooling,Pooling Plate location should be a 1.5mL tube\\nA1,T00010734_Auto_A01_0139964_21435904T1_Saliva_A01_Set3,24,1.2,\\nB1,T00010734_Auto_B01_0139964_21363223T1_Saliva_B01_Set3,20,1.5,\\nC1,T00010734_Auto_C01_0139964_21488156T1_Saliva_C01_Set3,17,1.7,\\nD1,T00010734_Auto_D01_0139964_21449091T1_Saliva_D01_Set3,20,1.5,\\nE1,T00010734_Auto_E01_0139964_21491328T1_Saliva_E01_Set3,2,13.5,\\nF1,T00010734_Auto_F01_0139964_21365742T1_Saliva_F01_Set3,17,1.8,\\nG1,T00010734_Auto_G01_0139964_21365717T1_Saliva_G01_Set3,15,2.1,\\nH1,T00010734_Auto_H01_0139964_21287078T1_Saliva_H01_Set3,4,7.8,\\nA2,T00010734_Auto_A02_0139964_21363161T1_Saliva_A02_Set3,5,5.7,\\nB2,T00010734_Auto_B02_0139964_21310637T1_Saliva_B02_Set3,3,9.5,\\nC2,T00010734_Auto_C02_0139964_21365730T1_Saliva_C02_Set3,5,6.5,\\nD2,T00010734_Auto_D02_0139964_21453532T1_Saliva_D02_Set3,4,7.0,\\nE2,T00010734_Auto_E02_0139964_21341771T1_Saliva_E02_Set3,17,1.8,\\nF2,T00010734_Auto_F02_0139964_21324008T1_Saliva_F02_Set3,12,2.4,\\nG2,T00010734_Auto_G02_0139964_21311564T1_Saliva_G02_Set3,24,1.2,\\nH2,T00010734_Auto_H02_0139964_21323775T1_Saliva_H02_Set3,5,6.1,\\nA3,T00010734_Auto_A03_0139964_21435929T1_Saliva_A03_Set3,19,1.6,\\nB3,T00010734_Auto_B03_0139964_21448635T1_Saliva_B03_Set3,14,2.2,\\nC3,T00010734_Auto_C03_0139964_21124490T1_Saliva_C03_Set3,8,3.6,\\nD3,T00010734_Auto_D03_0139964_21296423T1_Saliva_D03_Set3,3,11.7,\\nE3,T00010734_Auto_E03_0139964_21484617T1_Saliva_E03_Set3,9,3.4,\\nF3,T00010734_Auto_F03_0139964_21351045T1_Saliva_F03_Set3,7,4.1,\\nG3,T00010734_Auto_G03_0139964_21451996T1_Saliva_G03_Set3,1,27,\\nH3,T00010734_Auto_H03_0139964_21321949T1_Saliva_H03_Set3,3,11.6,\\nA4,T00010734_Auto_A04_0139964_21323015T1_Saliva_A04_Set3,18,1.7,\\nB4,T00010734_Auto_B04_0139964_21493387T1_Saliva_B04_Set3,20,1.5,\\nC4,T00010734_Auto_C04_0139964_21365738T1_Saliva_C04_Set3,6,5.4,\\nD4,T00010734_Auto_D04_0139964_21199983T1_Saliva_D04_Set3,10,2.9,\\nE4,T00010734_Auto_E04_0139964_21363157T1_Saliva_E04_Set3,16,1.9,\\nF4,T00010734_Auto_F04_0139964_21365757T1_Saliva_F04_Set3,11,2.7,\\nG4,T00010734_Auto_G04_0139964_21155259T1_Saliva_G04_Set3,15,1.9,\\nH4,T00010734_Auto_H04_0139964_21488152T1_Saliva_H04_Set3,5,6.5,\\nA5,T00010734_Auto_A05_0139964_21446396T1_Saliva_A05_Set3,3,9.6,\\nB5,T00010734_Auto_B05_0139964_21349375T1_Saliva_B05_Set3,7,4.2,\\nC5,T00010734_Auto_C05_0139964_21351027T1_Saliva_C05_Set3,6,5.4,\\nD5,T00010734_Auto_D05_0139964_21476302T1_Saliva_D05_Set3,2,18.4,\\nE5,T00010734_Auto_E05_0139964_21116069T1_Saliva_E05_Set3,5,5.8,\\nF5,T00010734_Auto_F05_0139964_21435992T1_Saliva_F05_Set3,13,2.3,\\nG5,T00010734_Auto_G05_0139964_21480379T1_Saliva_G05_Set3,3,9.4,\\nH5,T00010734_Auto_H05_0139964_21365734T1_Saliva_H05_Set3,22,1.4,\\nA6,T00010734_Auto_A06_0139964_20023912T1_Saliva_A06_Set3,23,1.3,\\nB6,T00010734_Auto_B06_0139964_21491407T1_Saliva_B06_Set3,11,2.9,\\nC6,T00010734_Auto_C06_0139964_21491506T1_Saliva_C06_Set3,5,6.4,\\nD6,T00010734_Auto_D06_0139964_21363176T1_Saliva_D06_Set3,9,3.4,\\nE6,T00010734_Auto_E06_0139964_21449268T1_Saliva_E06_Set3,13,2.3,\\nF6,T00010734_Auto_F06_0139964_21437064T1_Saliva_F06_Set3,5,5.8,\\nG6,T00010734_Auto_G06_0139964_21428077T1_Saliva_G06_Set3,5,5.7,\\nH6,T00010734_Auto_H06_0139964_21458747T1_Saliva_H06_Set3,17,1.7,\\nA7,T00010734_Auto_A07_0139964_21364116T1_Saliva_A07_Set3,17,1.8,\\nB7,T00010734_Auto_B07_0139964_21363162T1_Saliva_B07_Set3,22,1.3,\\nC7,T00010734_Auto_C07_0139964_21363167T1_Saliva_C07_Set3,6,5.2,\\nD7,T00010734_Auto_D07_0139964_21323548T1_Saliva_D07_Set3,6,4.9,\\nE7,T00010734_Auto_E07_0139964_21491470T1_Saliva_E07_Set3,3,11.9,\\nF7,T00010734_Auto_F07_0139964_21491504T1_Saliva_F07_Set3,9,3.4,\\nG7,T00010734_Auto_G07_0139964_21230060T1_Saliva_G07_Set3,3,8.9,\\nH7,T00010734_Auto_H07_0139964_21320013T1_Saliva_H07_Set3,9,3.2,\\nA8,T00010734_Auto_A08_0139964_21316031T1_Saliva_A08_Set3,20,1.5,\\nB8,T00010734_Auto_B08_0139964_21323152T1_Saliva_B08_Set3,1,22.1,\\nC8,T00010734_Auto_C08_0139964_21320056T1_Saliva_C08_Set3,2,14.9,\\nD8,T00010734_Auto_D08_0139964_21320131T1_Saliva_D08_Set3,19,1.6,\\nE8,T00010734_Auto_E08_0139964_21439051T1_Saliva_E08_Set3,4,6.7,\\nF8,T00010734_Auto_F08_0139964_21362458T1_Saliva_F08_Set3,17,1.8,\\nG8,T00010734_Auto_G08_0139964_21488183T1_Saliva_G08_Set3,2,15.7,\\nH8,T00010734_Auto_H08_0139964_21351030T1_Saliva_H08_Set3,14,2.1,\\nA9,T00010734_Auto_A09_0139964_21435958T1_Saliva_A09_Set3,12,2.5,\\nB9,T00010734_Auto_B09_0139964_21319936T1_Saliva_B09_Set3,9,3.4,\\nC9,T00010734_Auto_C09_0139964_21321108T1_Saliva_C09_Set3,4,6.8,\\nD9,T00010734_Auto_D09_0139964_21486160T1_Saliva_D09_Set3,13,2.3,\\nE9,T00010734_Auto_E09_0139964_21363423T1_Saliva_E09_Set3,19,1.6,\\nF9,T00010734_Auto_F09_0139964_21493647T1_Saliva_F09_Set3,11,2.7,\\nG9,T00010734_Auto_G09_0139964_21437397T1_Saliva_G09_Set3,19,1.6,\\nH9,T00010734_Auto_H09_0139964_21386927T1_Saliva_H09_Set3,7,4.3,\\nA10,T00010734_Auto_A10_0139964_21364163T1_Saliva_A10_Set3,24,1.2,\\nB10,T00010734_Auto_B10_0139964_21364207T1_Saliva_B10_Set3,15,2.0,\\nC10,T00010734_Auto_C10_0139964_21296284T1_Saliva_C10_Set3,18,1.7,\\nD10,T00010734_Auto_D10_0139964_21351183T1_Saliva_D10_Set3,21,1.5,\\nE10,T00010734_Auto_E10_0139964_21488159T1_Saliva_E10_Set3,6,5.1,\\nF10,T00010734_Auto_F10_0139964_21365692T1_Saliva_F10_Set3,13,2.3,\\nG10,T00010734_Auto_G10_0139964_21320057T1_Saliva_G10_Set3,21,1.5,\\nH10,T00010734_Auto_H10_0139964_21364118T1_Saliva_H10_Set3,14,2.2,\\nA11,T00010734_Auto_A11_0139964_21322745T1_Saliva_A11_Set3,7,4.4,\\nB11,T00010734_Auto_B11_0139964_21316188T1_Saliva_B11_Set3,19,1.6,\\nC11,T00010734_Auto_C11_0139964_21382433T1_Saliva_C11_Set3,1,30.1,\\nD11,T00010734_Auto_D11_0139964_21314439T1_Saliva_D11_Set3,6,5.1,\\nE11,T00010734_Auto_E11_0139964_21482291T1_Saliva_E11_Set3,4,7.6,\\nF11,T00010734_Auto_F11_0139964_21453529T1_Saliva_F11_Set3,8,3.9,\\nG11,T00010734_Auto_G11_0139964_21365708T1_Saliva_G11_Set3,12,2.5,\\nH11,T00010734_Auto_H11_0139964_21319787T1_Saliva_H11_Set3,23,1.3,\\nA12,T00010734_Auto_A12_0139964_21296438T1_Saliva_A12_Set3,25,1.2,\\nB12,T00010734_Auto_B12_0139964_21477474T1_Saliva_B12_Set3,1,27.3,\\nC12,T00010734_Auto_C12_0139964_21322327T1_Saliva_C12_Set3,18,1.7,\\nD12,T00010734_Auto_D12_0139964_21437454T1_Saliva_D12_Set3,21,1.4,\\nE12,T00010734_Auto_E12_0139964_21323029T1_Saliva_E12_Set3,10,3.0,\\nF12,T00010734_Auto_F12_0139964_21448040T1_Saliva_F12_Set3,18,1.7,\\nG12,T00010734_Auto_G12_0139964_21431228T1_Saliva_G12_Set3,17,1.8,\\nH12,T00010734_Auto_H12_0139964_21448521T1_Saliva_H12_Set3,7,4.6,\\n","p20_mount":"right","p300_mount":"left"}""")
    return [_all_values[n] for n in names]


metadata = {
    'protocolName': 'Pooling via CSV',
    'author': 'Eleazar Lab',
    'source': 'Protocol Templates',
    'apiLevel': '2.13'
}

# Destination tube dimensions, given in mm
cone_radius = 5
cone_height = 3.76
cylinder_radius = 5
cylinder_height = 39.85
tube_height = 43.61

# Volume function for the conical part (in cubic mm)
def volume_cone(height):
    # Using the volume formula for a cone, V = 1/3 * pi * r^2 * h
    return (1/3) * np.pi * cone_radius**2 * height

# Function to calculate height from the bottom given volume for the conical part of the tube
def height_from_volume_cone(volume):
    # The equation to solve is 1/3 * pi * r^2 * h - volume = 0
    # We solve for h
    result = fsolve(lambda h: (1/3) * np.pi * cone_radius**2 * h - volume, x0=0)
    return result[0]

# Function to calculate height given volume for the cylindrical part
def height_from_volume_cylinder(volume):
    cone_vol = volume_cone(cone_height)
    if volume < cone_vol:
        return 0
    volume -= cone_vol
    return volume / (np.pi * cylinder_radius**2)
    
# The maximum volume for the conical section
max_volume_cone = volume_cone(cone_height)


def height_from_volume(volume):
    # Check if the volume is within the conical section or the cylindrical section
    if volume <= max_volume_cone:
        return height_from_volume_cone(volume)
    else:
        return cone_height + height_from_volume_cylinder(volume)

def run(ctx):

    [protocol, csv_samp, p20_mount, p300_mount] = get_values(  # noqa: F821
        "protocol", "csv_samp", "p20_mount", "p300_mount")

    csv_lines = [[val.strip() for val in line.split(',')]
                 for line in csv_samp.splitlines()
                 if line.split(',')[0].strip()][2:]

    # labware

    if protocol == "pooling":
        source_plate = ctx.load_labware('olympus_96_wellplate_200ul_pcr', 2)
        dest_tube_rack = ctx.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 3)
        tips = [ctx.load_labware('opentrons_96_filtertiprack_20ul', slot)
                for slot in [5]]
        tips3 = [ctx.load_labware('opentrons_96_filtertiprack_200ul', slot)
                 for slot in [6]]

    # pipettes
    p20 = ctx.load_instrument('p20_single_gen2', p20_mount, tip_racks=tips)
    p300 = ctx.load_instrument('p300_single_gen2', p300_mount, tip_racks=tips3)

    if protocol == "pooling":

        # dna
        ctx.comment('\n ------------- POOLING DNA ------------ \n\n')

        ctx.max_speeds['X'] = 60
        ctx.max_speeds['Y'] = 60
        ctx.max_speeds['Z'] = 30

        p20.flow_rate.aspirate = 50
        p20.flow_rate.dispense = 100
        p20.flow_rate.blow_out = 75

        p300.flow_rate.aspirate = 50
        p300.flow_rate.dispense = 75
        p300.flow_rate.blow_out = 75

        tube_liquid_level = tube_height - 1
        for line in csv_lines:

            dna_vol = float(line[3])
            source_well = source_plate.wells_by_name()[line[0]]

            runs = int(dna_vol/20)

            for i in range(runs):
                p20.pick_up_tip()
                p20.aspirate(20, source_well.top(z = -19.5))
                p20.dispense(20, dest_wells[0].top(z = -tube_liquid_level))
                p20.blow_out()
                p20.drop_tip()

            p20.pick_up_tip()
            p20.aspirate( (dna_vol - (runs*20)), source_well.top(z = -19.5) )
            p20.dispense( (dna_vol - (runs*20)), dest_wells[0].top(z = -tube_liquid_level) )
            p20.blow_out()  
            p20.drop_tip()

            total_liquid_vol = total_liquid_vol + dna_vol
            tube_liquid_level = tube_height - height_from_volume(total_liquid_vol)
