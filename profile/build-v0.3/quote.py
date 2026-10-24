"""Reproducible planning quote. Allowances are not seller quotations."""
import json
from pathlib import Path
OUT=Path(__file__).resolve().parent

rows=[
 ['MOTOR','17HS19-1684S-PG14, 2 motors',88889,'PUBLIC_PRICE_ROUNDED','https://www.omc-stepperonline.com/nema-17-stepper-motor-bipolar-l-48mm-w-gear-ratio-14-1-planetary-gearbox-17hs19-1684s-pg14','Official KR display44444.40 each; foreign freight/import charges excluded'],
 ['SCREW','TR10 lead2 x500 + brass flange nut, 2 sets',19600,'PUBLIC_PRICE','https://nasspop.com/product/detail.html?product_no=616','P00000XS000K; unquoted thrust rating and shaft end machining'],
 ['COUPLING','8/10 rigid D20L20, 2 pieces',4800,'PUBLIC_PRICE_UNRATED','https://nasspop.com/product/detail.html?product_no=854','Budget comparison only; torque/slip rating absent, not frozen2kN selection'],
 ['FRAME','4080:780x2,260x2,250x1',79750,'PUBLIC_PRICE','https://www.yjprofile.co.kr/goods/goods_view.php?goodsNo=1000000051','VAT included,201–300mm bands9570 each and701–800mm25520; nominal section in CAD'],
 ['ELECTRONICS','Uno3190+shield/A4988 kit23650+HX7111870+24V3A26070+EStop26015+switches4840+relays2772+5Vreg7216',95623,'PUBLIC_PRICE_MIXED_SELLERS','https://vctec.co.kr/product/detail.html?product_no=10229','Detailed seller links in SOURCING; 3A supply is a priced baseline, not approved original5A replacement'],
 ['PSU_UPGRADE','Replace3A baseline with documented24V5A supply',20000,'ALLOWANCE','','Extra cost allowance above26070 baseline; exact model/quote pending'],
 ['WIRING','Fuse, reset/start, wiring, terminals, USB, capacitors',22000,'ALLOWANCE','','Unfinished electrical drawing and quantity'],
 ['BEARINGS','3200x2,6202x2,608x4',40000,'ALLOWANCE','','Identifiable bearing maker and exact grade/fit to be frozen'],
 ['HARDWARE_MACHINING','Bolts, nuts, spacers, bearing inserts, grip adapters and shaft-end work',70000,'ALLOWANCE','','Custom parts not quoted; includes provisional small fabrication budget, may be exceeded'],
 ['PRINT','PETG4kg common carriers/feet/covers and provisional original-grip allowance',60000,'PUBLIC_PRICE_BUDGET_QUANTITY','https://3dprinterstore.co.kr/product/detail.html?product_no=737&item_code=P0000BCJ000B','15000/kg; CAD candidate volume recorded inVALIDATION; original-grip print eligibility/slicer use, supports, failures, electricity and labour not qualified'],
 ['GUARD','PC3mm400x600 front panel',16800,'PUBLIC_PRICE_VAT_UNCONFIRMED','https://www.akobigs.com/goods/goods_view.php?goodsNo=34765','Only one panel; mount/side containment detail pending; tax treatment to confirm'],
 ['KR_SHIP','Domestic combined shipping allowance',26000,'ALLOWANCE','','YJ3000; Nasspop~7000; remaining multi-vendor parcels16000 assumption'],
 ['INTL_SHIP_IMPORT','Motor freight40000 + import/payment allowance20000',60000,'ALLOWANCE','','No Korean checkout freight or customs quotation obtained']
]

if __name__=='__main__':
    common=sum(r[2] for r in rows)
    subtotal_public=sum(r[2] for r in rows if r[3].startswith('PUBLIC'))
    report={'version':'0.3.0-costdown-layout','checked_date':'2026-10-24','currency':'KRW',
        'quote_type':'PLANNING_ESTIMATE_NOT_VENDOR_OFFER','physical_rating_guaranteed':False,
        'original_BOM_total_known':False,'earlier_2160000_KRW_was_original_BOM':False,
        'common_machine_without_load_cell_KRW':common,'public_display_rows_KRW':subtotal_public,
        'allowances_KRW':common-subtotal_public,'rows':[dict(zip(['id','description','line_total_KRW','basis','url','note'],r)) for r in rows],
        'sensor_options':[
          {'id':'AEP_original','part':'TC4 5kN CTC41005KNI15','price_type':'FOREIGN_REFERENCE_NOT_KOREA_QUOTE',
           'EUR_ex_VAT':635,'reference_EURKRW':1482.46,'sensor_only_KRW_ex_VAT':941362,
           'sensor_plus_simple10pct_KRW':1035498,'machine_planning_total_KRW':common+1035498,
           'excludes':'Sensor shipping/import fees, OEM tension kit, force calibration and physical proof tests'},
          {'id':'Zemic_candidate','part':'H3-C3-500kg-3B','price_type':'UNQUOTED_ALLOWANCE',
           'sensor_allowance_KRW':250000,'machine_planning_total_KRW':common+250000,
           'budget_target_KRW':500000,'gap_to_budget_KRW':common+250000-500000,
           'excludes':'Force calibration, physical proof tests, labour and failed prints; adapter design not complete'}],
        'unresolved_costs':['supplier final freight/taxes','coupling upgrade if unrated part rejected','final shaft and sensor machining quote','calibration/proof-loading services','labour and electricity'],
        'AliExpress_status':'Manufacturer-authorised seller and live Korea checkout not verified; no Ali listing is represented as authenticated or final-priced'}
    (OUT/'COST_SUMMARY.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:report[k] for k in ('common_machine_without_load_cell_KRW','public_display_rows_KRW','allowances_KRW','sensor_options')},indent=2))
