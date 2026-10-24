"""Analytical screening of ideal continuous members; NOT FEA or a load rating."""
import json
import math
from pathlib import Path

OUT=Path(__file__).resolve().parent

def screen(E=800.0):
    # 80X x60Y column; continuous closed shell6, no bosses counted in ideal model.
    A=80*60-68*48
    Iweak=(80*60**3-68*48**3)/12
    Istrong=(60*80**3-48*68**3)/12
    p=1000.0; length=780.0
    column_delta=p*length/(E*A)
    pcr=math.pi**2*E*Iweak/length**2
    bottom_delta=2000*340**3/(48*E*Istrong)
    top_delta=1000*70*(3*340**2-4*70**2)/(24*E*Istrong)
    Imoving=(80*40**3-68*28**3)/12
    moving_delta=2000*200**3/(48*E*Imoving)
    rod_root=6.47;rod_A=math.pi*rod_root**2/4;rod_I=math.pi*rod_root**4/64
    parallel_delta=1000*length/(E*A+2*200000*rod_A)
    return dict(E_effective_assumption_MPa=E,column_area_mm2=A,column_Iweak_mm4=Iweak,
        column_Istrong_mm4=Istrong,column_axial_shortening_mm=column_delta,
        ideal_column_Euler_pinned_N=pcr,printed_top_beam_deflection_mm=top_delta,
        printed_bottom_beam_deflection_mm=bottom_delta,printed_moving_beam_deflection_mm=moving_delta,
        ideal_total_frame_opening_compliance_mm=column_delta+top_delta+bottom_delta+moving_delta,
        moving_beam_nominal_stress_MPa=(2000*200/4)*20/Imoving,
        M8_root_assumption_mm=rod_root,M8_unbraced_780_Euler_N=math.pi**2*200000*rod_I/780**2,
        M8_195_braced_Euler_N=math.pi**2*200000*rod_I/195**2,
        hybrid_ideal_parallel_column_shortening_mm=parallel_delta,
        hybrid_ideal_force_per_M8_rod_N=parallel_delta*200000*rod_A/length)

if __name__=='__main__':
    result={'load_N':2000,'method':'Euler / linear elastic beam formulas; ideal continuous members',
        'physical_test_performed':False,'FEA_performed':False,'rating_established':False,
        'exclusions':['joint slip','centre beam butt joints','hole stress concentration','layer anisotropy',
                      'creep','eccentric load','bearing/coupling/grip deformation','rod end-transfer and bracing qualification'],
        'sensitivity':[screen(E) for E in (800,1000,1500)]}
    (OUT/'SCREENING.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
