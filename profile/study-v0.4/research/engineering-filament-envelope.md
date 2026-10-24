# 엔지니어링 FFF 필라멘트 인장시험기의 하중 범위

2026-10-25 조사. 사용자 조건: **23°C 상온 인장시험만**, PPS-CF/PA6-CF/PPA-CF/PC계 및 고성능 PAEK계까지 폭넓게 취급. 구매·판매자 연락·CAD·Git 변경 없음. 이 보고서는 시험기 요구 하중을 정하는 자료 조사이며 완성 시험기의 정격 증명이 아니다.

**결론: 10 kN 작업 등급을 다음 설계의 합리적인 목표로 삼는다. 단면 40 mm² 및 인장강도 250 MPa 이하라는 명시적인 범위에서다.** 검토한 현재 연결 제조사 TDS의 방향별 최고 대표값은 Bambu PPA-CF XY168±4 MPa로, 40 mm²에서6.72 kN이다. 10 kN는 이 대표값보다 약1.49배 높다. 이번 자료만으로 20 kN를 필수로 올릴 근거는 없지만, “모든 엔지니어링 필라멘트”를 재료명만으로 무제한 보장할 수는 없다.

기존2 kN는 목표 하향 없이 재평가해야 한다. 40 mm²에서50 MPa에 해당하므로 Bambu PA6-CF XY(4.08 kN), PPA-CF XY(6.72 kN), PPS-CF XY(3.48 kN)를 파단하기에 부족하다. 소재의 내열 등급이 높다는 이유만으로 상온 인장강도도 항상 높지는 않다.

## 제조사 인장값과 단면별 계산

계산식은 **F[N] = σ[MPa] × A[mm²]**다. 표의 힘은 평균/대표 인장값에 단면을 곱한 예상값이며, 실제 파단하중이나 최대 로트 강도 보증이 아니다. ±표기는 제조사 표기 그대로이며 통계적 상한 또는 보증 공차로 재해석하지 않았다. **40/10/4 mm²는 계산 사례이며 ISO 승인 시편 지정이 아니다.**

| 재료·상태 | 인장 XY MPa | 인장 Z MPa | 40 mm² XY / Z, N | 10 mm² XY / Z, N | 4 mm² XY / Z, N |
|---|---:|---:|---:|---:|---:|
| [1] Bambu PPS-CF | 87 ± 5 | 24 ± 3 | 3480 / 960 | 870 / 240 | 348 / 96 |
| [2] Bambu PA6-CF | 102 ± 7 | 48 ± 6 | 4080 / 1920 | 1020 / 480 | 408 / 192 |
| [3] Bambu PPA-CF | 168 ± 4 | 57 ± 5 | 6720 / 2280 | 1680 / 570 | 672 / 228 |
| [4] Polymaker Fiberon PA6-CF20 dry | 109.3 ± 2.4 | 54 ± 5.2 | 4372 / 2160 | 1093 / 540 | 437.2 / 216 |
| [5] Polymaker Fiberon PA6-CF20 wet | 54.7 ± 1.1 | 25.5 ± 1.2 | 2188 / 1020 | 547 / 255 | 218.8 / 102 |
| [6] Bambu PC | 55 ± 4 | 34 ± 3 | 2200 / 1360 | 550 / 340 | 220 / 136 |
| [7] 3DXTECH CarbonX PC+CF | 70 | 미공개 | 2800 / — | 700 / — | 280 / — |
| [8] 3DXTECH CarbonX PEEK+CF10 | 105 | 미공개 | 4200 / — | 1050 / — | 420 / — |
| [9] 3DXTECH CarbonX PEKK-A+CF15 | 126 | 미공개 | 5040 / — | 1260 / — | 504 / — |
| [10] INTAMSYS PEEK-CF | 미공개 | 미공개 | — / — | — / — | — / — |


INTAMSYS 행의 빈 칸은 누락이 아니라 방향별 수치가 원문에 없다는 뜻이다. 제조사 작성 TDS의 방향 미지정 인장87.4 MPa는40/10/4 mm²에서 각각 **3,496/874/349.6 N**이다. 이를 XY 또는 Z로 임의 배정하지 않는다. 현재 공식 페이지의 Tech Sheet는 연락처 폼 뒤에 있어 제출하지 않았으며, 제조사가 작성한©2021 문서를 유통사 서버에서 확인했다. 최신 revision 동일 여부는 미확정이다.

## 시험법·방향·상태를 섞지 않는 조건

- **[1] Bambu PPS-CF:** ISO 527 / GB/T 1040; Printed X1E; 320°C nozzle /110°C bed /60°C chamber /60mm/s /100% infill; not annealed. Specimen moisture/test temperature not explicitly quantified in this TDS.
- **[2] Bambu PA6-CF:** ISO 527 / GB/T 1040; Printed280°C nozzle /100°C bed /100mm/s /100% infill; annealed and dried80°C12h. Dry-condition values, not wet-conditioned equivalents.
- **[3] Bambu PPA-CF:** ISO 527 / GB/T 1040; Printed X1C;290°C nozzle /110°C bed /52°C chamber /80mm/s /100% infill; not annealed. Specimen moisture/test temperature not explicitly quantified.
- **[4] Polymaker Fiberon PA6-CF20 dry:** ISO 527 / GB/T 1040; specimen drawing also bears ASTM D638 label; Printed300°C nozzle /50°C bed /100% infill; annealed100°C16h; DRY STATUS. Do not call ASTM/ISO tests equivalent based on drawing label.
- **[5] Polymaker Fiberon PA6-CF20 wet:** ISO 527 / GB/T 1040; Annealed100°C16h then immersed in water60°C48h; average specimen moisture5.30%. Not equivalent to23°C/50%RH equilibrium conditioning.
- **[6] Bambu PC:** ISO 527 / GB/T 1040; Printed270°C nozzle /100°C bed /100% infill; annealed and dried80°C12h. Table speed200mm/s contradicts footnote100mm/s; retain uncertainty.
- **[7] 3DXTECH CarbonX PC+CF:** ISO 527; XY Flat; open-sourceFFF;0.4mm nozzle /0.25mm layer /100% ±45° infill /300°C extrusion /140°C bed. Z and conditioning not supplied.
- **[8] 3DXTECH CarbonX PEEK+CF10:** ISO 527; XY Flat; open-sourceFFF;0.4mm nozzle /0.25mm layer /100% ±45° infill /400°C extrusion /140°C bed. Z and conditioning not supplied.
- **[9] 3DXTECH CarbonX PEKK-A+CF15:** ISO 527; XY Flat; open-sourceFFF;0.4mm nozzle /0.25mm layer /100% ±45° infill /390°C extrusion /140°C bed. Z and conditioning not supplied.
- **[10] INTAMSYS PEEK-CF:** ISO 527; FUNMAT HT;410°C nozzle /45mm/s /2 shells /100% infill; annealed200°C2h. Print direction not declared. Current official Tech Sheet requires form; no submission/contact performed.

제조사들은 위 인장 수치를 `Tensile Strength`로 표기하거나3DXTECH처럼 명시적으로 `Break`로 표기한다. `Tensile Strength`를 별도 근거 없이 항복강도 또는 파단강도와 동일시하지 않았다. 시험기의 최대 힘 범위를 가늠하는 대표 인장값으로 사용한 것이다. ISO527와 ASTM D638, 서로 다른 시편/적층 방향/래스터/시험속도를 동등한 시험으로 간주하지 않는다. 사출성형 원료 펠릿이나 연속 탄소섬유 라미네이트 강도는 이 표에 넣지 않았다.

23°C는 **우리 시험기의 사용 조건**이다. 이 TDS들 모두가 인장시험의 실제 온도·습도·컨디셔닝 시간을 동일하게 공개하는 것은 아니다. 공개하지 않은 문서에23°C/50%RH를 임의로 채워 넣지 않았다. 따라서 표는 구매 전 하중 선정용이며 같은 조건의 재료 순위표가 아니다.

PA6-CF는 특히 건조/흡습 상태를 분리해야 한다. Fiberon PA6-CF20은 건조XY109.3 MPa에서 wet54.7 MPa로 바뀌며, wet은 **60°C 물48h, 평균 수분5.30%** 조건이다. 이를23°C 대기 중의 평형 상태나 Bambu의80°C12h 건조값과 직접 비교하면 안 된다. Bambu PPS/PPA의 비어닐링 값, Bambu PA6/PC의80°C12h 처리값, Polymaker100°C16h, INTAMSYS200°C2h는 서로 다른 열 이력이다.

## 인장과 굽힘 수치의 오인 방지

- Bambu PPA-CF의 **208 MPa는 굽힘**, 인장은168 MPa다.
- Bambu PPS-CF의 **142 MPa는 굽힘**, 인장은87 MPa다.
- Bambu PA6-CF의 **151 MPa는 굽힘**, 인장은102 MPa다.
- INTAMSYS PEEK-CF의 제조사 작성 TDS는 **인장87.4 MPa / 굽힘168.6 MPa**다. 검색 스니펫이나 현재 비교 페이지의 선택 항목이 불분명한 추출값168.6을 인장으로 가져오지 않는다.
- CarbonX PC+CF의 제조사 블로그/일부 구자료73 MPa와 달리, **현재 제품 페이지가 연결하는 Rev3.0 TDS는 인장파단70 MPa**다. 본 계산은70을 썼다.

## 10 kN와20 kN 선택

| 작업 등급 | 40 mm²의 대응 강도 | 10 mm² | 4 mm² | 해석 |
|---|---:|---:|---:|---|
| 2 kN |50 MPa|200 MPa|500 MPa|전체 크기 XY 엔지니어링 소재군에는 부족 |
| 5 kN |125 MPa|500 MPa|1,250 MPa|PPA-CF168 MPa×40 mm²를 담지 못함 |
| **10 kN** |**250 MPa**|1,000 MPa|2,500 MPa|이번 조사 소재군과 명시한 단면 범위에 합리적인 작업 목표 |
| 20 kN |500 MPa|2,000 MPa|5,000 MPa|더 큰 단면·250 MPa 초과 단섬유 등급·다른 복합재 시험을 확장할 때 검토 |

**제안 사양:** 작업0–10 kN, 설계 검토 하중15 kN, 환경23°C.15 kN는10 kN 작업하중의1.5배로 잡는 **제안된 구조 검토/검증 목표**이며, 모든 부품의 허용응력 안전계수1.5가 자동 충족된다는 뜻이 아니다. 실제 proof 시험은 아직 수행하지 않았다. 하중 셀·그립·핀·볼트·프레임·베어링·나사·전원 차단의 등급/하중 경로를 맞추고,15 kN가 센서 안전 과부하를 넘지 않게 검증 절차를 별도로 설계해야 한다.

10 kN를 채택하면 현재 UTM V2의 단일2060/출력 지그/저가 감속모터를 수치만 바꾸어 확대해서는 안 된다. 이전1 kN 수준 실증에서10 kN는 완전히 다른 하중 설계다. 또한 큰 센서 하나로 수십N–10 kN 전체에서 같은 정확도를 얻는다는 뜻도 아니다. 약한Z 시편을 위한 하위 범위 교정/분해능과 필요시 작은 로드셀을 따로 검토한다.

20 kN가 필요한 조건은 재료명이 아니라 **σ×실제 A**가10 kN를 넘거나, 제조사/예비 시험의 높은 값·그립 여유·규격 요구가10 kN 범위를 넘는 경우다.40 mm²에서250 MPa를 넘는 신규 등급, 더 두꺼운 시편, 연속섬유/테이프·적층 복합재·금속 등은 이 조사 범위 밖이다. 해당 자료가 나오면20 kN 또는 그 이상으로 재선정한다.

## 축소 시편의 예산 효과와 한계

5×2 mm 단면은10×4 mm의1/4이므로168 MPa 소재도1,680 N,250 MPa를 가정해도2,500 N이다.4 mm²는168 MPa에서672 N,250 MPa에서1,000 N이다. 따라서50만원 예산을 우선하면 축소/맞춤 시편을 이용한 상대 비교 장비는 별도 범위로 검토할 수 있다. 그러나 단면을 줄이면 표준 시편과 형상·게이지 길이·그립·필라멘트 경로·벽/인필 비율·공극의 영향이 달라진다. 이 방법을 기존2 kN 요구나 ISO527 전체 크기 시험을 충족한 것으로 표시하면 안 된다. 사용자 승인 없는 목표 변경도 아니다.

## 출처

모두 제조사 작성 TDS다. Bambu 링크는2026-10-25 공식 UK 제품 페이지 HTML의 Filament TDS 링크를 읽어 확보했고,3DXTECH/Polymaker는 당일 공식 제품 페이지의 현재 TDS 링크를 열었다. INTAMSYS만 제조사 문서의 유통사 미러이며 최신판 확인 제한을 명시했다. 문서에 발행일이 없으면 edition만 적었으며 CDN 경로 날짜를 발행일로 만들지 않았다.

[1] [Bambu PPS-CF, TDS V1.0, currently linked 2026-10-25](https://store.bblcdn.eu/s8/default/623b28bf2fbe495fa9dd559a85f494ed/Bambu_PPS-CF_Technical_Data_Sheet.pdf)

[2] [Bambu PA6-CF, TDS V3.0, currently linked 2026-10-25](https://store.bblcdn.com/b2abc59ac250492b979a52f1ce3e61b3.pdf)

[3] [Bambu PPA-CF, TDS V1.0, currently linked 2026-10-25](https://store.bblcdn.eu/s8/default/f592e57fe69c40289897513bdd2b61bc/Bambus_PPA-CF_Technical_Data_Sheet_2ab26420-79f5-4692-888e-090006814050.pdf)

[4] [Polymaker Fiberon PA6-CF20 dry, TDS V1.1 EN, currently linked 2026-10-25](https://fiberon.polymaker.com/wp-content/uploads/TDS_FIBERON-PA6-CF20_V1.1_EN.pdf)

[5] [Polymaker Fiberon PA6-CF20 wet, TDS V1.1 EN, currently linked 2026-10-25](https://fiberon.polymaker.com/wp-content/uploads/TDS_FIBERON-PA6-CF20_V1.1_EN.pdf)

[6] [Bambu PC, TDS V3.0, currently linked 2026-10-25](https://store.bblcdn.com/3bf3be91a7164c86a7e5ceffb18ee21b.pdf)

[7] [3DXTECH CarbonX PC+CF, TDS Rev3.0, currently linked 2026-10-25](https://cdn.shopify.com/s/files/1/0625/4185/6821/files/CarbonX_CF_PC_TDSv3.pdf?v=1723942764)

[8] [3DXTECH CarbonX PEEK+CF10, TDS Rev3.0, currently linked 2026-10-25](https://cdn.shopify.com/s/files/1/0625/4185/6821/files/CarbonX_CF_PEEK_TDS_v3.pdf?v=1723942765)

[9] [3DXTECH CarbonX PEKK-A+CF15, TDS Rev1.0, currently linked 2026-10-25](https://cdn.shopify.com/s/files/1/0625/4185/6821/files/CarbonX_CF15_PEKK-A__TDS_v1.pdf?v=1723942767)

[10] [INTAMSYS PEEK-CF, Manufacturer-authored TDS, ©2021; distributor filename v2; current manufacturer revision unverified](https://shop.bfi-it.de/media/20/3e/0b/1693570740/intamsys_peek-cf_tds_v2.pdf)

추가 원본 페이지: [Bambu PA6-CF](https://uk.store.bambulab.com/products/pa6-cf), [Bambu PPA-CF](https://uk.store.bambulab.com/products/ppa-cf), [Bambu PPS-CF](https://uk.store.bambulab.com/products/pps-cf), [Fiberon PA6-CF20](https://fiberon.polymaker.com/product/pa6-cf20/), [INTAMSYS PEEK-CF](https://www.intamsys.com/materials/peek-cf), [3DXTECH PC+CF](https://www.3dxtech.com/products/carbonx-pc-cf-1), [3DXTECH PEKK-A+CF](https://www.3dxtech.com/products/carbonx-pekk-a-cf15-1).

