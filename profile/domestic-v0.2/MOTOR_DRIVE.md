# Motor / driver / timing transmission — domestic Korea sourcing

Checked 2026-10-24 KST. No purchases or supplier messages. “Domestic seller” and “confirmed domestic inventory” are distinguished below. Coupang currently returns 403 for direct live fetch; its indexed prices and delivery dates are not live stock confirmations.

## Recommendation and procurement status

Use **Leadshine 57CM23-3A** as the dimensional design reference. It has a real manufacturer drawing and an exact Korean retail option. A genuine **Leadshine EM542S V3.0** is a documented electrical match, offered through domestic industrial distributors, but its price and domestic inventory remain quote-only. The lowest-priced Coupang motor/driver pair found is genuine domestic seller JNK Global/Scipia stock marketing, but both products are OEM and the motor shaft-length information conflicts; it is unsuitable as the released CAD reference.

| Candidate | Domestic sale / price evidence | Verified status / unresolved |
|---|---|---|
| Leadshine **57CM23-3A**, MotionGearOn option `P0000CGZ000D` | [Exact retail page](https://motiongearon.com/product/detail.html?product_no=1533), option “57CM23-3A(전류3A)”: **₩42,900**, delivery **₩3,500**. VAT treatment not separately stated. Korean business address and nationwide parcel delivery. Live HTML offer is InStock and option is selling-enabled. | Inventory tracking is disabled (`use_stock=false`); `stock_number=0` is not an out-of-stock statement and is not proof of domestic physical stock. Confirm current local dispatch before procurement. Standard 5A/4A/dual-shaft variants share this page: select the 3A option exactly. |
| Genuine Leadshine **EM542S** | [WITHFA domestic product table](https://www.withfa.co.kr/stepper-motor/leadshine) explicitly lists EM542S; [Motor114 Korean official-dealer EM-S page](https://leadshine.co.kr/product/view.php?pcode=PROD00000000051) offers quote/data requests. | Exact manufacturer SKU offered domestically; **price, stocked quantity, lead time and supplied revision unverified / quotation required**. No enquiry sent. DM542E is another manufacturer-listed match but likewise lacks verified Korean ready-stock price. |
| Scipia OEM **CIC 57100**, 2.5 Nm / 2.8A | [Exact Coupang offer](https://www.coupang.com/vp/products/8550726815?itemId=603332816&vendorItemId=4581242864): indexed base **₩44,700**, temporary indexed discount ₩43,200; delivery ₩2,900, JNK Global / Lotte. [Seller’s current product page](https://scipia.com/product/detail.html?product_no=698) option `P0000BAW000C` is ₩44,700 including VAT, Domestic Delivery, InStock. | Manufacturer is stated only **OEM**. Text says this 100mm model has **20mm** shaft, shared drawing says **23±1mm**. Do not resolve the discrepancy by assumption. No manufacturer CAD or torque curve found. |
| Scipia OEM **A7Q DM542** | [Exact Coupang offer](https://www.coupang.com/vp/products/1432305817?itemId=2473811862&vendorItemId=70467187979): indexed **₩29,800** + ₩2,900 shipping, JNK Global. [Current seller page](https://scipia.com/product/detail.html?product_no=978): ₩29,800 including VAT, domestic delivery; purchase-enabled. | Economical domestic-source candidate; not identified as genuine Leadshine. Do not apply genuine Leadshine dimensions, firmware or current-setting table solely because “DM542” matches. |
| MISUMI **C-57STM04** | [Exact Korean page](https://kr.misumi-ec.com/vona2/detail/110310526859/?HissuCode=C-57STM04): **₩38,579 ex VAT / ₩42,437 incl VAT**, 1.89Nm, 2.8A, body75mm, paired C-DR57A. | **Order suspended**, restart date unknown, owing to China export issue. This explicit banner overrides the stale table’s “1 day / same-day possible” label. 60-series alternatives are also shown order-suspended. Exclude from available procurement. |

The Coupang OEM pair totals **₩74,500 before shipping** at base prices, but it does not close the manufacturer/drawing requirement. No overseas StepperOnline, AliExpress, or purchasing-agent candidate is selected. Korean-language StepperOnline pages explicitly dispatch from China/US/Germany/UK/Australia and are excluded.

## 57CM23-3A exact interface

Source: [manufacturer 2021-04-28 MS30 drawing](https://www.leadshine.com/upfiles/downloads/d42e3b7c2b223a4e1e4c103cc7aa6304_1651824123970.pdf), visually inspected. “MS30” does **not** mean a 30mm exposed shaft.

| Feature | Verified dimension / specification |
|---|---|
| Front square / body depth | **57.2mm maximum square; 76.5±1mm** body depth |
| Mounting holes | **47.14±0.2mm square pattern; 4 × Ø5(+0.3/0) through holes** |
| Pilot | **Ø38.1±0.05mm; 1.6mm projection** |
| Shaft | **Ø8(0/−0.012)mm; exposed length21±0.5mm** from mounting face |
| Shaft flat | Flat dimension **7.5±0.1mm** from opposite circumference; flat length **15±0.2mm** from tip |
| Cable outlet / cable | Outlet near rear, **19mm** from rear face, **12.3mm** projection below square; 400mm minimum cable on 2021 drawing |
| Electrical | 2 phase / 4 leads; **3.0A per phase**, 1.8°, **2.3Nm holding torque**, 1.2Ω, 4.3mH, 1.1kg; A/black, A-bar/green, B/red, B-bar/blue |

[Current manufacturer product page](https://www.leadshine.com/product-detail/57CM23-3A.html) confirms 3A / 2.3Nm / Ø8 / 76mm nominal / Ø38.1 pilot. [Older 2017 manufacturer drawing](https://www.leisaishop.com/uploadfiles/2102201708_18764.pdf) uses body56.4 square ×76±1mm, Ø8(0/−0.013), 300mm leads and4mH; mounting/shaft positions agree. Use the **2021 maximum envelope**, not an invented 57×57×112 envelope.

**CAD identity caveat:** the manufacturer page advertises [57CM23-3A_MS30_3D ZIP](https://www.leadshine.com/upfiles/downloads/b1208c3eac5d9daeb13f459fb87e6b3b_1651830619229.zip), but the downloaded archive contains only `57CM23-4A_MS30_3D.STEP` (4,175,350 bytes). It is a manufacturer-supplied sibling reference, not an exact 3A STEP. Do not silently rename it. The 3A PDF is the verified dimensional authority.

## Genuine EM542S compatibility

[Manufacturer V3 manual](https://www.leadshine.com/upfiles/downloads/38ca2ca53b17e368fe8406e9d8b1b426_1650880166787.pdf): supply20–50VDC; output4.2A **peak** =3.0A RMS; selectable5/24V optoisolated STEP/DIR; pulse ≥2.5µs, direction setup ≥5µs. The motor’s factory marketplace recommends36V; low-speed use can start at24V within the driver range.

Manual §7.1 recommends peak ≤1.2× the phase-current rating for four-lead motors to limit heating. For3A, an initial **3.3A peak /2.4A RMS** setting (SW1/2/3 OFF/ON/OFF) satisfies this;4.2A peak/3A RMS is available but is not the manual’s conservative thermal recommendation. Motor torque at chosen current/speed, cable routing and supply regeneration remain bench-validation items. Holding torque does not prove the 2kN working load. The existing ideal ~0.9Nm motor estimate assumes the two screws together carry2kN,5mm lead and2:1 reduction; friction, acceleration and belt losses add demand.

## Timing transmission: documented domestic alternative to HTD5M

No finished-bore **HTD5M 20/40T,15mm** set with both domestic physical stock and a complete primary interface drawing was verified. Generic Coupang HTD listings found have unclear stock origin/manufacturer and are excluded. Use a **complete S5M system**, with matching S5M pulleys and belt; do not mix S5M and HTD5M.

Verified primary drawing: [MISUMI Korean S5M catalogue, pages1487–1488](https://kr.misumi-ec.com/pdf/fa/2018/p1_1487_002_1_087_2020.pdf). The drawing and current Korea URLs support:

| Exact configurable SKU | Teeth / bore | Verified outer geometry |
|---|---|---|
| [**HTPA20S5M150-A-P8**](https://kr.misumi-ec.com/vona2/detail/110300406030/?HissuCode=HTPA20S5M150-A-P8) |20T / Ø8H7 round + two radial set screws | PitchØ31.83, toothOD30.87, hubD19, flangeF36, referenceE24mm |
| [**HTPA40S5M150-A-P10**](https://kr.misumi-ec.com/vona2/detail/110300406030/?HissuCode=HTPA40S5M150-A-P10) |40T / Ø10H7 round + two radial set screws | PitchØ63.66, toothOD62.70, hubD47, flangeF67, referenceE50mm |

For both: belt tooth face **A17mm**, overall flange width **W22mm**, total axial length **L34mm**, hub extension **L−W=12mm**, flange sheet1.5mm. For Ø8 andØ10, radial screws are **M4** (supplied M4×3 for aluminium). Shape-A screws are placed120° apart for20T. Aluminium2000-series, clear anodized. **Exact Korean price and delivery require price calculation; do not interpret `standardUnitPrice=0` as a free part.** The current N8 and N10 URLs were checked live: valid configurable part number, salesOrderStopFlag0, price not calculated. P8/P10 are within the same primary configuration table.

Requested keyway variants [HTPA20S5M150-A-N8](https://kr.misumi-ec.com/vona2/detail/110300406030/?HissuCode=HTPA20S5M150-A-N8) and [HTPA40S5M150-A-N10](https://kr.misumi-ec.com/vona2/detail/110300406030/?HissuCode=HTPA40S5M150-A-N10) are valid catalogue configurations but do not create a keyed coupling to a D-flat motor shaft or an unkeyed ball-screw tail. Prefer P8/P10 for the current geometry study. **Torque transfer is HOLD:** with a15mm screw tail, only the12mm hub can be fully engaged while the belt face overhangs; no rated set-screw slip torque or pulley-overhang allowance was established. Manufacturer-approved clamping hubs / a supported intermediate shaft / a longer machined screw tail are potential resolutions, not approved substitutions.

**920mm belt exists:** [**C-HTBN920S5M-150** Korean exact page](https://kr.misumi-ec.com/vona2/detail/110310459629/?HissuCode=C-HTBN920S5M-150), live HTML: price **₩7,812 ex VAT / ₩8,593 incl VAT**, offer InStock, salesOrderStopFlag0. This is S5M,15mm wide,920mm pitch length, **184 teeth**, closed-end chloroprene/fibreglass. Its page description says economy belts can be ordered from4pcs; exact minimum/order quantity and dispatch date need checkout/quotation confirmation. The family’s stock badge is not a counted physical-inventory confirmation. Do not substitute the standard `HTBN920...` without separately verifying it.

Avoid old **C-HTPA** economy pulleys: the Korean family announces discontinuation after stock depletion from2025-04-15. Use the standard HTPA configurable family above. [Sungil’s primary S5M table](https://www.sungilfa.co.kr/en/products/timing-pulley/satp-s5m/) is a domestic clamping alternative, but SC starts at24T; its20T SPAA version does not support Ø8/15mm-belt in the shown table. Therefore it does not close the present20T/40T interface without redesign.

## Outstanding procurement/design gates

1. Confirm local physical stock / dispatch for exact57CM23-3A; obtain genuineEM542S V3 domestic quote and revision.
2. Calculate MISUMI exact P8/P10 prices and delivery; confirm920 belt minimum quantity.
3. Close shaft-to-pulley torque transfer, engagement and overhung radial loading before fabrication. Current P8/P10 CAD represents sourced shape, not a validated connection.
4. Verify loaded torque, temperature and lost-step behaviour at intended speed/current. No manufacturer2kN system rating is claimed.
