# 10 kN 요구로 변경할 때: 구조·계측·예산 검토

조사일 2026-10-25. 연구 전용 메모. 구입·업체 문의·CAD 수정·Git 변경을 하지 않았다. **50만원 이하의 완성된 10 kN 시험기를 현재 근거로 구성했다고 말할 수 없다.** 아래 제품은 후보 예시이며 최종 선정품이나 납품 견적이 아니다. 외화는 **1 USD=1,500원이라는 계획 환산값**을 썼다. 실시간 환율 견적이 아니다.

## 요구 하중과 MT02의 경계

전폭 A1의 공칭 단면 10×4=40 mm²에서 250 MPa를 계획하면 10,000 N이다. 실제 단면이 10.2×4.2 mm이면 같은 응력에서 10,710 N이다. 250 MPa는 모든 PPS-CF/PA6-CF의 상한이라는 뜻이 아니며, 실제 재료 데이터와 단면으로 시험 상한을 정해야 한다. 2 kN으로는 전폭 40 mm²에서 50 MPa까지만 인장할 수 있다.

[MT02 원문](https://repositum.tuwien.at/handle/20.500.12708/200949)의 3.5 kN 목표/3.388 kN 계산 추진력은 10 kN 근거가 아니다. 비교 실험은 PETG 평균 최대하중 약 800 N 규모였다. 500 kg 센서, 원래 BK12 계열 지지, 출력 그립, 경량 프로파일/알루미늄 체결부를 유지한 채 센서만 바꾸면 10 kN 기계가 되지 않는다. 새 설계는 **MT02에서 영감을 받은 요구 배치**이며 진품 MT02 CAD나 검증된 10 kN 기계로 표시하면 안 된다.

23°C 상온 요청에는 가열 챔버가 필요하지 않다. PA6 계열의 수분 조건과 실제 시편 치수는 시험기록에서 관리해야 한다. 높은 탄성률을 주장하려면 크로스헤드 이동량과 별개로 표점 구간 변형률을 측정해야 한다. 원 MT02의 보정 탄성률도 Zwick 영상식 측정 대비 약 48% 낮았다.

## CAS SBA-2 2 tf 외형과 계측

[CAS 공식 2쪽 브로슈어](https://www.globalcas.com/upload/goods/1600822642799_398.pdf)의 2–3 tf 공통 도면: **폭 77 × 높이 108 × 본체 두께 25.4 mm**, 덮개 포함 최대 깊이 33 mm. 상·하 동축 **M18×1.5**, 축은 폭 방향 38.5 mm / 본체 깊이 방향 12.7 mm 중심이다. E=19 mm는 암 두께이며, 별도 탭 깊이 또는 유효 체결 길이가 아니다. 실제 체결 길이는 미확정이다. 케이블 Ø5.4 mm×3 m는 우측 중간 높이로 나오며 글랜드 돌출 길이는 미기재다. 로컬 도면은 `cas-sba-official-p1.png`에 있다.

1 tf는 9.80665 kN이므로 엄밀한 10 kN 정격을 충족하지 않는다. 2 tf는 19.6133 kN이다. 공식 자료는 **SBA 인장 타입**이다. 국내 판매 제목의 인장압축형 문구만으로 압축 정격/보정을 확정할 수 없다. 출력 3.0±0.3 mV/V, 권장 여기 10 V, 최대 15 V이므로 공칭 전범위 출력은 30 mV, 10 kN에서 약 15.30 mV다. 셀의 150% 과부하 사양은 그립/프레임/기계 전체 허용하중이 아니다.

[국내 판매 페이지](https://nissysc.co.kr/product/cas-%EB%A1%9C%EB%93%9C%EC%85%80-sba-2-%EC%9D%B8%EC%9E%A5%EC%95%95%EC%B6%95%ED%98%95-load-cell/2427/) 공개가는 165,000원, 배송 4,000원이며 세금 포함 여부가 명확하지 않아 예산에는 165,000–181,500원을 잡았다. 실제 용량 옵션 재고/주문 및 배송 결제는 확인하지 않았다.

**일반 5 V HX711 보드를 그대로 연결하는 BOM을 쓰지 않는다.** 10 V로 여기한 정상 브리지는 신호 공통모드가 약 5 V다. [AVIA HX711 데이터시트](https://cdn.sparkfun.com/datasheets/Sensors/ForceFlex/hx711_english.pdf) p3의 입력 공통모드는 AGND+1.2~AVDD−1.3 V이므로 AVDD=5 V에서 상한 3.7 V다. 증폭도128의 차동 범위도 약 ±20 mV다. 따라서 낮은 차동 신호만 보고 호환된다고 판단하면 안 된다. 10 V 저잡음 여기와 적합한 instrumentation amplifier/ADC, 또는 호환 브리지 지시계·로그 출력을 선정해야 한다. SBA를 5 V로 실험 보정할 수는 있어도 권장 10 V 조건의 제조사 성능 등급을 자동 승계하지 않는다. 아래에는 해당 계측에 **20–40만원의 미견적 허용액**을 별도 배정했다. 인장 방향 실제 사용범위의 영점·스팬·반복성·히스테리시스와 기록 대역을 검증해야 한다.

## BK/FK 지지와 볼스크루 구동

[NTN-SNR 1차 카탈로그](https://www.ntn-snr.com/sites/default/files/2024-09/DOC_I_BS_CAT7_GBc-WEB.pdf) p86 표6.11, p88 표6.13은 C0a와 별도의 유닛 축방향 정적 용량을 구분한다. 아래는 해당 제조사의 특정 C5품이며 범용 판매품에 전용할 수 없다.

| 지지 유닛 | Ca kN | C0a kN | 유닛 static axial capacity kN |
| --- | ---: | ---: | ---: |
| BK12_C5 / FK12_C5 | 5.05 | 2.46 | 2.38 |
| BK17_C5 / FK17_C5 | 10.50 | 5.40 | 4.07 |
| BK20_C5 | 10.30 | 6.05 | 5.75 |
| FK20_C5 | 13.60 | 7.55 | 5.79 |
| BK25B_C5 / FK25B_C5 | 15.40 | 9.47 | 6.97 |
| BK30B_C5 / FK30B_C5 | 21.30 | 13.60 | 9.22 |
| BK35_C5 | 28.20 | 18.50 | 12.80 |

두 축이 이상적으로 균등 분담하면 10 kN에서 축당 5 kN이다. 프로젝트가 요구한 **끝단 지지당 ≥10 kN**은 불균등 분담 등에 대한 설계 여유 기준이며 ISO의 보편적 요구라고 주장하지 않는다. BK12/FK12는 균등 5 kN도 미달한다. BK20/FK20는 공칭 5 kN을 조금 넘을 뿐 이 프로젝트의 10 kN 기준에는 미달한다. BK35는 정격 예시이고 SFU1605의 12 mm 저널에 맞는 선택품이 아니다.

저가 대안으로 [NTN 추력베어링 카탈로그](https://www.ntn-snr.com/sites/default/files/2024-01/DOC_I_DGBB_CAT4_A4_Fa-WEB-vok.pdf) PDF p42의 51101은 12×26×9 mm, Ca 10.3/C0a 15.4 kN이다. 양방향 구속용 대향 배치, 별도 방사 지지, 가공 하우징·록너트·정밀 간격과 지지면이 필요하다. 축 지지면 최소 Ø20 mm라 Ø16 mm 나사 몸체만으로 지지하지 못한다. 적절한 경화 백킹 스페이서/어깨 설계가 필요하며 **BK12 대체 끼움품이 아니다**. 단품 C0a가 커도 저널·나사·너트·하우징을 포함한 전체 지지 정격은 아직 미확정이다.

국내 SFU1605 500 mm [축+너트 47,000원](https://mizo.kr/product/detail.html?product_no=109&item_code=P00000EF00DF) 또는 [BK12 EF12 포함 표기 세트 79,000원](https://mizo.kr/product/detail.html?product_no=96&item_code=P00000DS00EE)은 가격 참고다. 어떤 것도 이 조사에서 10 kN 하중 경로가 검증된 조립품은 아니다. 아래 볼스크루 항목에는 확인되지 않은 세트를 확정품으로 넣지 않았다.

리드 5 mm, 나사 효율 0.9라는 가정에서 10 kN 총 나사 토크는 **8.84 N·m**, 두 축 각각 **4.42 N·m**다. 따라서 2 N·m나 3 N·m NEMA23의 직결은 정지 토크만으로도 부족하다. 감속 3:1·벨트 효율0.95라면 모터당 계산 요구는 약 **1.55 N·m**지만 이는 예비 계산이다. 운전 속도 토크곡선, 전류, 구동전압, 벨트/풀리/축 및 양축 동기·실제 변위가 검증되어야 한다. 감속기와 끝단 지지는 **미선정**이다.

제조사 직판 [23HS45-4204S](https://www.omc-stepperonline.com/nema-23-bipolar-3nm-425oz-in-4-2a-57x57x114mm-4-wires-stepper-motor-cnc-23hs45-4204s)는 3 N·m **유지 토크**, 4.2 A/상, 개당 $28.70이다. [DM556T](https://www.omc-stepperonline.com/digital-stepper-driver-1-8-5-6a-20-50vdc-for-nema-23-24-34-stepper-motor-dm556t)는 개당 $22.92다. 각각 2개 합계 $103.24=154,860원 계획 환산이며 배송 전이다. 드라이버 피크/RMS 전류와 모터 운전토크를 맞춰야 하므로 이 조합 자체가 검증된 10 kN 구동을 뜻하지 않는다.

## 금속 그립의 계산 경계

배치 후보는 강재 조판 50×30×12 mm, 그립당 M8 4개다. 마찰계수 μ=0.2를 임의 가정하고 `F=2μQ`로 쓰면 10 kN에서 Q=25 kN이다. **Q는 각 접촉면에 작용하는 법선력/볼트 조임 합력이고, 양쪽 면 법선력 합계는 50 kN**이다. 15 kN 설계 검토 경우에는 Q=37.5 kN이다. 4개 볼트 균등 분배 가정은 각각 6.25/9.375 kN이지만 실제 분배, 볼트 등급/프리로드, 시편 압궤·노치와 마찰은 미검증이다. 15 kN 수치는 미검증 조립체의 현장 가압 지시가 아니다. 아래 가공비는 **업체 견적을 받지 않은 허용액**이다.

## 수동 잭과 속도 제어 후보

[제조사 Kemusen KMA25](https://screwjackfactory.en.made-in-china.com/product/sPOpczBbnEkr/China-25-kN-Adjustable-Screw-Jack-for-Lifting-and-Support.html)는 최대 정적25 kN, Ø30 mm 사다리꼴 나사 피치6 mm, 감속6:1 또는24:1, 주문 스트로크·끝단 구성으로 광고한다. [제조사 가격 목록](https://m.made-in-china.com/company-screwjackfactory/productlist.html)의 $99–199 FOB/MOQ1은 제품군 광고 범위이며 선택 스트로크/인장 끝단/핸드휠 포함 납품가는 아니다. 인장 구성과 입력토크·좌굴·회전방지·부착을 확인해야 한다. 24:1은 입력1회전당0.25 mm이며 1 mm/min이면4 rpm, 50 mm/min이면200 rpm이다.

손으로 돌리는 것만으로 일정 시험 속도를 입증하지 못한다. **수동은 비표준 강도 선별용 후보이며 ISO 속도 준수로 권하지 않는다.** [국내 WGM93-446812 12 V 모터](https://m.motiongearon.com/product/detail.html?cate_no=128&display_group=1&product_no=1062)의 광고가는85,000원+배송3,500원이다. 감속별1.5–40 rpm,12–65 kgf·cm 광고 범위는 하나의 부하 운전점이 아니다. 잭 입력토크 및 선택 감속비가 미확정이다. PWM만 추가해도 충분하다고 볼 수 없으며 실제 이동 피드백/제어기/전원/커플러/마운트와 부하 속도 검증을 포함해 **20–35만원 추가 허용액**을 잡았다.

## 누락 방지용 전체 계획 비용

아래는 공급업체 합산 확정 견적이 아니다. 외형의 철재 프레임·금속 그립·파편 가드·계측·실제 이동량·기본 검증·배송/세금 여유까지 포함한다. 보유 프린터/PC, 사용자 인건비, 공인 교정, 고정밀 표점 변형률계, 표준 인증은 제외한다. 가공·계측의 실제 선정에 따라 상단을 넘을 수 있다.

### 수동25 kN 잭 기반

| 항목 | 원 | 근거 |
| --- | ---: | --- |
| CAS SBA-2 2 tf tension load cell | 165,000–181,500 | 공개가격/세금 여유 |
| 25 kN KMA25 worm screw jack | 148,500–298,500 | 공개가격/세금 여유 |
| Steel reaction frame, cutting/drilling/basic fabrication | 150,000–300,000 | 미견적 허용액 |
| Pair of machined steel grips and jaw hardware | 100,000–250,000 | 미견적 허용액 |
| Fragment guard, hinges/latch and fixture | 50,000–100,000 | 미견적 허용액 |
| 10 V bridge supply, compatible conditioner/ADC or indicator, force logging | 200,000–400,000 | 미견적 허용액 |
| Independent travel sensor/readout and mount | 50,000–100,000 | 미견적 허용액 |
| M18 adapters, pins, fasteners, jack mounts | 50,000–100,000 | 미견적 허용액 |
| Basic validation fixtures and checks | 50,000–150,000 | 미견적 허용액 |
| Shipping and import tax reserve | 80,000–180,000 | 미견적 허용액 |
| **합계** | **1,043,500–2,060,000** | **약104–206만원** |

12 V 모터·피드백 구동을 추가한 범위는 **1,243,500–2,410,000원(약124–241만원)**이다. 수동 잭 구조가 반드시 제어 자동화 후에도 더 싸거나 빠르다고 단정하지 않는다.

### 쌍볼스크루 자동 구조

| 항목 | 원 | 근거 |
| --- | ---: | --- |
| CAS SBA-2 2 tf tension load cell | 165,000–181,500 | 공개가격/세금 여유 |
| Steel reaction frame and fabricated crossheads | 200,000–400,000 | 미견적 허용액 |
| Pair of machined steel grips and jaw hardware | 150,000–300,000 | 미견적 허용액 |
| Two ball screws, nuts and verified end-support assemblies | 250,000–500,000 | 미견적 허용액 |
| 2 x 23HS45-4204S plus 2 x DM556T | 154,860–170,346 | 공개가격/세금 여유 |
| Proposed reduction, timing synchronization, couplings and mounts | 60,000–120,000 | 미견적 허용액 |
| Motor DC power supply and wiring | 40,000–80,000 | 미견적 허용액 |
| Metal linear guides and carriage interfaces | 80,000–150,000 | 미견적 허용액 |
| 10 V bridge supply, compatible conditioner/ADC or indicator, force logging | 200,000–400,000 | 미견적 허용액 |
| Controller, limit switches, stop circuit and enclosure | 70,000–130,000 | 미견적 허용액 |
| Independent travel sensor/readout and mount | 50,000–100,000 | 미견적 허용액 |
| Fragment guard, hinges/latch and fixture | 70,000–130,000 | 미견적 허용액 |
| Basic validation fixtures and checks | 50,000–150,000 | 미견적 허용액 |
| Shipping and import tax reserve | 100,000–220,000 | 미견적 허용액 |
| **합계** | **1,639,860–3,031,846** | **약164–303만원** |

50만원 제한을 유지하면 전폭 A1/250 MPa/10 kN/안전가드/실제 계측을 한꺼번에 충족한다고 약속할 수 없다. 잭+셀 광고가격만 약313,500–480,000원이며 남은 돈으로 프레임·그립·가드·계측·배송까지 검증하는 근거가 없다. 저렴한 공급처가 존재할 가능성과 검증된 완성 BOM의 존재는 구분한다.

## 2 kN을 살리는 별도 시편 경로

[현행 ISO 카탈로그](https://www.iso.org/standard/527-2)는527-2:2025이다. [Zwick의 설명](https://www.zwickroell.com/industries/plastics/thermoplastics-and-thermosetting-molding-materials/tensile-test-iso-527-1-2/)은 A22/A25/1BA/1BB를 조건부 대안으로 다루며 속도 조정·직접 비교 한계를 지적한다. [구판 제조사 치수 자료](https://www.interempresas.net/FeriaVirtual/Catalogos_y_documentos/85077/Plastics.pdf)의2×2 mm 축소 단면이라면250 MPa에서1 kN이다. 그러나 이는 같은 전폭 A1 결과가 아니며, 현행 규격과 FFF 단섬유 시편 적합성·로드/섬유 방향·그립을 별도 검토해야 한다. 이번 요구를 저절로 2 kN으로 충족시킨다는 결론이 아니다.

## 다음 선정 전 미확정 사항

- 실제 재료/시편 단면과 요구 하중 여유, 금속 프레임·연결부 강도와 변형.
- 나사/너트/끝단 지지/저널/록너트 전체 경로 또는 인장 정격 잭의 정확 구성.
- 금속 그립의 조임력·미끄럼·압궤와 M18 어댑터 체결 길이.
- 10 V 브리지 계측 구성, 인장 실제 사용범위 보정, 기록 대역과 영점 드리프트.
- 부하 상태 실제 속도·이동량·전 모드 정지, 가드 구성과 시험 접근.
- 탄성률을 보고할 경우 표점 변형률계와 교정.

수치·부품 상태·출처·예산 항목은 `10kn-upgrade-budget.json`에 구조화했다. 원문 도면·정격표 추출물은 같은 무시 폴더에 보존했다.
