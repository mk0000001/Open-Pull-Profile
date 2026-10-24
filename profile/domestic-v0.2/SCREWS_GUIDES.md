# Screws, fixed/floating supports and guides: domestic sourcing

Checked 2026-10-24. This is component selection research for a nominal 2 kN experiment; it is not a certified machine or assembly load rating. No purchasing, seller messages, FreeCAD changes or Git changes were made.

## Strongest concrete CAD/BOM combination

| Qty | Exact item | Korean purchase page | Observed price/status |
|---:|---|---|---|
| 2 | MISUMI **C-TBSE1505-861**, right hand, actual shaft Ø16, lead 5, overall 861 | [Configured screw](https://kr.misumi-ec.com/vona2/detail/110310435959/?HissuCode=C-TBSE1505-861) | **Live confirmed exact SKU:** totalCount1 / completeFlag1 / order-stop flag0. Variable-price field is 0 because no public quote was returned, **not a zero-won price**. Family lead time 8 days onward. Exact price unresolved. |
| 2 | MISUMI **C-TFK12** fixed round support | [C-TFK12](https://kr.misumi-ec.com/vona2/detail/110310392219/?HissuCode=C-TFK12) | Live page embedded product data: **₩20,364 excluding VAT**, recognized complete, order-stop flag 0. |
| 2 | MISUMI **C-TFF12** floating/support round unit | [C-TFF12](https://kr.misumi-ec.com/vona2/detail/110310392309/?HissuCode=C-TFF12) | Live embedded data: **₩5,726 excluding VAT**, recognized complete, order-stop flag 0. |
| 2 | MISUMI **E-HLGH15-700-B2**, each rail supplied with two standard blocks | [Configured rail + 2 blocks](https://kr.misumi-ec.com/vona2/detail/110311122029/?HissuCode=E-HLGH15-700-B2) | Recognized complete SKU, order-stop flag 0; exact configured price unresolved. Spare block **E-HLGH15B ₩9,234 excluding VAT** in family data. |

The C-TBSE end is explicitly catalogued for C-TFK/C-TFF. The similarly named **C-TBSB** uses the different BK/BF end and must not be substituted. Supports alone total ₩52,180 excluding VAT / ₩57,398 including VAT. The older Korean marketing design case shows ₩43,640 / ₩14,940 per support; those are not the current captured SKU prices. [MISUMI Korean design case](https://kr.misumi-ec.com/pr/vona/eco_design/info77/).

## Screw machining and nut: source dimensions

Primary drawing: [MISUMI original screw drawing, Taiwan PDF](https://tw.misumi-ec.com/pdf/fa/2023/0041-0042.pdf); corroborated by [current OEM catalog, printed page 03-023](https://my.misumi-ec.com/pr/vona/free_download_misumi_economy_catalog/pdf/index_003_ball_screws_lead_screws.pdf). Local rendered detail: `misumi-screw-detail.png`; high resolution support-end crop: `shaft-left-journal.png`.

Set datum **s=0 at the lower/support tip**, positive toward the upper/driven tip. Final length **L861** preserves the proposed frame; the initial L900 alternative is also a valid configured SKU but moves the support planes. Nominal dimensions in millimetres:

| Axial station | Feature |
|---|---|
| 0–11 | Ø10 journal, tolerance 0/−0.015 |
| **1.85–3.00** | Retaining-ring groove: root Ø9.6, 0/−0.2; width 1.15 +0.14/0 |
| 11–810 | Ø16 screw/thread interval; Y=L−62=799 |
| 810–835 | Ø12 bearing seat, 0/−0.018; length 25 |
| 835–846 | M12×1 locknut thread, U=11 |
| 846–861 | Ø10 driven tail, 0/−0.015; length 15 |

**Important correction:** the drawing's 9.15 +0.2/0 is measured backward from the s=11 shoulder to the groove's far edge. It is not measured from the end tip. The nominal groove therefore begins at 11−9.15=1.85. Do not use an s=8–9.15 groove.

Nut: axial length 42; body Ø28 0/−0.02; flange thickness 10, nominal Ø48 with 40 across its side flats; 6×Ø5.5 through on PCD38; M6 lubrication port. Hole layout follows the X-X drawing (top/bottom and four diagonal holes, excluding the two horizontal extremes). The 22.5° callout is the oil-port orientation; 45° is the flange-hole increment in the drawing. The screw/nut OEM basic ratings are dynamic 3.6 kN and static 7.4 kN; axial clearance ≤0.1 mm.

Suggested custom housing interface: a **metal** plate or block with an axial Ø28 pilot/clearance bore and six M5 fasteners through the existing nut flange. This is a custom design, not a catalog housing. Keep the M6 oil port reachable. Do not remove the nut from its screw without a transfer sleeve. Thread interval less nut length gives 757 mm geometric span before end margins; this is ample for the requested 100 mm, but the assembled grip/frame geometry still defines actual usable travel.

## Fixed and floating supports: source dimensions and derived seating

Primary section drawings: [OEM catalog, printed page 03-053](https://my.misumi-ec.com/pr/vona/free_download_misumi_economy_catalog/pdf/index_003_ball_screws_lead_screws.pdf). Local `misumi-fk-detail.png` and `misumi-ff-detail.png` were visually checked. [OEM fixed-support collar/locknut table](https://th.misumi-ec.com/en/vona2/detail/110310392219/?HissuCode=C-TFK12) supplies the accessory dimensions.

| Dimension | C-TFK12 | C-TFF12 |
|---|---:|---:|
| Shaft bore d | 12 | 10 |
| Total axial L | 27 | 15 |
| Rear boss projection F | 17 | 8 |
| Flange axial H | 10 | 7 |
| Pilot boss D | 36 g6 | 34 |
| Flange across flats B | 44 | 42 |
| Maximum diagonal/circular envelope A | 54 | 52 |
| Bolt circle PCD | 44 | 42 |
| Mounting holes | 4×Ø4.5 | 4×Ø4.5 |
| Counterbores | Ø8×4 deep | Ø8×4 deep |

A is not a square width and B is not a bolt pitch. With square sides axis-aligned, mounting holes are at 45/135/225/315° on the PCD: FK offsets (±15.556, ±15.556), FF offsets (±14.849, ±14.849). FK bearing setback T1=5; locknut outer projection L1=7.5. FK collars: 2×(OD15.5, ID12, length5.5); locknut M12×1, thickness8, OD22, wrench flats19, M4 retaining screw.

**Derived assembly placement; verify against downloaded assembly CAD or actual parts before machining the frame:**

* FK for L861: first collar against screw shoulder s810 occupies810–815.5. Bearing rear face=815.5. With T1=5, housing rear=810.5; boss/flange mounting plane **s827.5**; flange front=837.5; overall nut envelope ends845.0. The M12 thread continues to846. This result follows the published collar length, T1, F, H and L1; it has not been independently checked in a STEP assembly. Allow assembly shimming and retain the datum as a parameter.
* FF: [MISUMI-hosted CAD parameter record](https://misumi.partcommunity.com/3d-cad-models/c-tff-%E7%B5%8C%E6%B8%88%E5%9E%8B-%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%83%A6%E3%83%8B%E3%83%83%E3%83%88-%E6%94%AF%E6%8C%81%E5%81%B4-%E6%A8%99%E6%BA%96%E4%B8%B8%E5%9E%8B-misumi?info=misumi%2Fmetric%2F09_ball_screws%2Fc_tff_asmtab.prj) gives C=3.5 and BL=8. Interpreting C as the centred bearing end offset: bearing s3–11, housing −0.5–14.5; boss/flange mounting plane **s7.5**. The ring sits below the bearing, and the Ø16 shoulder is at its upper end. Maintain the intended axial float in the outer bearing fit; do not clamp both supports axially as fixed ends.

Thus final L861 mounting-plane separation is **827.5−7.5=820.0**. Place lower shaft tip at world **Z164.5**: FF mounting planeZ172; threadZ175.5–974.5; fixed collarZ974.5–980; FK housing rearZ975; FK mounting planeZ992; flange frontZ1002; driven tailZ1010.5–1025.5. General fixed mounting station is **s=L−33.5**, so plane separation is **L−41**. For comparison, L900 gives plane spacing859: retaining FFZ172 would put FKZ1031. The old900 placeholder cannot keep the original support spacing.

### Axial-load limitation

[MISUMI's C-TFK table](https://th.misumi-ec.com/en/vona2/detail/110310392219/?HissuCode=C-TFK10) lists No.12 basic dynamic3640 N / static1790 N, but does **not** clearly label these as axial permissible loads, nor supply an allowable axial working-load limit. Treat allowable axial force as **unresolved**. [Actual HIWIN FK12-C5 OEM data](https://www.hiwin.de/en/Products/Bearings/Bearings-FK-FF/FK/FK12-C5/p/18-000447) states 2200 N allowable axial force, but that applies to HIWIN article18-000447, not the MISUMI economy unit or a generic BK/FK clone. At the nominal two-screw split, 2 kN gives 1 kN per screw before weight, imbalance and shock; that division does not establish capacity.

## Actual guide interfaces

Choose the exact MISUMI family above, not a generically named HGR/HGH copy. [Korean OEM cross-reference drawing table](https://kr.misumi-ec.com/pdf/el/E_LG%EC%8B%9C%EC%A4%91%EA%B7%9C%EA%B2%A9%ED%91%9C.pdf) and [OEM detailed family table](https://id.misumi-ec.com/vona2/detail/110311122029/?HissuCode=E-HLGH15):

* E-HLGH15 block: installed height28; width34; total length58.4; metal/body length39.4; four M4×5 tapped holes, **26×26 pattern**. This differs from both the placeholder and HIWIN HGH15CA's length61.4.
* Rail: width15, height15; pitch60; holes Ø4.5 through / Ø7.5 counterbore depth5.3; OEM recommended rail bolt M4×16. A 700 rail with symmetric E20 has **12 holes** at20,80,…,680. In this table **H1=15 is rail height** and **H2=4.3 is the block underside clearance from rail base**. Physical block height=28−4.3=23.7. If rail base is globalY−40, front block mounting surface isY−68 and its rear/underside isY−44.3.
* E-HLGH15's own ratings in the Korean comparison are C10.73 kN / C0 17.13 kN. Do not copy HIWIN's different ratings. Rail-length tolerance is ±2 mm in the OEM family page. Actual alignment, end distance option and mounting-surface requirements remain assembly checks.

## Cheaper domestic routes and Coupang comparison

| Route / exact listing | Observed offer | Decision |
|---|---|---|
| [Mizo SFU1605, product109](https://mizo.kr/product/detail.html?product_no=109) | ₩50,000 base, 200–1000 options, domestic delivery; 900 shown as a length option | Live HTML explicitly `is_soldout_icon='T'`, sold-out map. Reject as current buy-now selection. |
| [Mizo set, product96](https://mizo.kr/product/detail.html?product_no=96) | ₩82,000 base screw/support set, domestic delivery; 900 option; drawings show overall900, actual thread835 | **Sold out**; only support option disabled. FK12/FF12 narrative and contradictory FK10/FF12 line are another reason not to copy its interface blindly. |
| [E-bearing genuine HIWIN block/rail selector, goods1000001012](https://www.ebearing.co.kr/goods/goods_view.php?goodsNo=1000001012) | HGH15CA block ₩30,000; HGR15-640L add-on ₩58,500; HGR15-820L add-on ₩73,500. Seller states Korean delivery1–3 days and Korean pickup address. VAT basis not explicitly confirmed. | A concrete domestic alternative: four blocks + two820 rails = **₩267,000 before shipping**, but would change guide length. 700 is not among the listed standard add-ons. |
| [Coupang HIWIN/HGR15 listing8471506860](https://www.coupang.com/vp/products/8471506860) | Cached ₩207,200; title includes700, but chosen quantity/length set and domestic stock cannot be verified; return cost₩100,000 | **Not selected.** Marketplace presence does not establish domestic stocked shipping or genuine OEM identity. |
| [Coupang SFU1605 listing7944681592](https://www.coupang.com/vp/products/7944681592) | Long multi-length title; search content did not establish Korean-stock shipment, exact900 option price or manufacturer | **Not selected.** No overseas purchasing-agent or Ali route was adopted. |

MISUMI economy supports and blocks are much cheaper than its older promotional examples suggest, so do not assume Coupang is cheaper without a matching configured quote. The domestic Mizo products are useful drawing evidence but presently unavailable; the real HIWIN retailer alternative has clear Korean fulfillment evidence but a different rail length.

## Unresolved before final manufacturing/purchase release

1. Exact C-TBSE1505-861 and E-HLGH15-700-B2 price/lead-time quote; published public zero fields are placeholders.
2. C-TFK12 permissible axial working load with the actual bearing/retention arrangement. Do not certify2 kN using its ambiguous basic-load table.
3. Independent STEP/physical confirmation of the derived FK collar/plate axial seating and FF C/BL interpretation. Shaft stations, flange patterns and outer dimensions above are source-backed; complete assembly coordinates are explicitly derived.
4. Custom metal nut-housing/frame attachment design, lubrication access and alignment tolerance stack. The 100mm movement requirement alone is satisfied geometrically; grip clearances/limits still need integration.

The 5mm lead preserves the proposed torque/speed relation. Two screws carrying total2kN at assumed efficiency0.9 need ideal total screw torque Fp/(2π η)=**1.77N·m**, about0.884N·m per screw, excluding preload/friction/imbalance. Ballscrews can backdrive; the separate motor/brake design must hold the vertical crosshead. No TR16×4 substitution is recommended here because a domestic stocked, machined, rated assembly was not verified more convincingly.
