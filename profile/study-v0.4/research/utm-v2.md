# CrazyBlackStone UTM Version 2 검토 및 한국 조달 계획

확인일: 2026-10-25. 조사만 수행했으며 구매·판매자 연락·CAD 변경은 하지 않았다. 금액은 원화이며, 공개 판매가와 명시한 충당금을 구분했다. 배송지 결제화면 견적이 아니므로 재고·최종 운임·결제세금은 확정 전이다.

**판정: 이 설계는 저가 복제 후보로 유용하지만, 기존 최소 2 kN 요구를 충족한 설계로 채택할 근거는 없다.** 아래 기본 복제 계획은 **499,084원**, 예비비 50,000원을 포함하면 **549,084원**이다. 기본 계획만으로도 50만원 여유가 916원뿐이고, 2 kN 보강·가공·교정비는 확정할 수 없다. 따라서 “50만원에 검증된 2 kN 시험기”라는 결론은 성립하지 않는다. 1 kN로 목표를 변경한 것이 아니다.

## 1. 버전과 성능 문구의 차이

| 자료 | 확인 내용 | 해석 |
|---|---|---|
| [Version TWO 원문](https://www.instructables.com/Universal-Tensile-Testing-Machine-VERSION-TWO/) | 2020-11-01 발행. 당시 신규 제작비 약 US$180–200. 제작자 시험에서 적어도 1 kN | 당시 재료비이며 현재 한국 도착가가 아니다. 2 kN 실증 자료가 아니다 |
| [2023 Hackaday 프로젝트](https://hackaday.io/project/192166-low-cost-universal-tensile-testing-machine/) | US$300, 1 kN 미만 시편용. 원문의 2.0에서 전장 개선 중인 2.1이라는 설명 | 기구는 대체로 동일하며 전장 개정이 하중 정격을 올린다는 설명은 없다 |
| [GitHub README](https://github.com/CrazyBlackStone/Universal-Tensile-Testing-Machine) | 플라스틱 시편, 2 kN 미만이라는 범위 문구 | 인증 정격·안전계수·2 kN 하중 시험 결과가 없다. 위 1 kN 중심 설명과 구분해야 한다 |

제작자의 [2023 권장 시편 로그](https://hackaday.io/project/192166-low-cost-universal-tensile-testing-machine/log/221734-recommended-testing-specimen)는 ASTM D638 Type IV를 권하고 파단하중 1 kN 미만을 전제로 한다. 반면 [사용 설명](https://hackaday.io/project/192166/instructions?page=3)은 ISO 527-2 1A 또는 ASTM D638-II도 언급한다. 시편 형상이 끼워진다는 설명과 해당 단면을 끝까지 파단시킬 하중 능력은 별개다. 원문 링크의 정확한 말미는 `VERSION-TWO`이며 `Version-2`가 아니다.

## 2. 원본 CAD와 라이선스

[GitHub CAD 디렉터리](https://github.com/CrazyBlackStone/Universal-Tensile-Testing-Machine/tree/main/CAD%20Files)에 편집 가능한 Fusion 파일 6개와 전체 STEP가 실제 존재한다. 2026-10-25 확인한 Git tree SHA는 `be75abab5a2ee7439486bf0d66ecfbde7ac7960b`다.

| 파일 | 크기 |
|---|---:|
| Grip Block v5.f3d | 103,374 B |
| Grip Screw Head v8.f3d | 90,626 B |
| Moving Grip v40.f3d | 448,727 B |
| Moving Load Cell Mount Mk2 v23.f3d | 333,438 B |
| Stationary Grip Mk3 v37.f3d | 572,102 B |
| Stepper Motor Mount Mk4 Long v11.f3d | 367,901 B |
| [Tensile Testing Machine Assembly v50.step](https://github.com/CrazyBlackStone/Universal-Tensile-Testing-Machine/blob/main/CAD%20Files/Tensile%20Testing%20Machine%20Assembly%20v50.step) | 15,584,409 B |

STEP blob SHA: `c535fdf556560d4ac7aa4abba1db6c0b55a113a3`. STL과 정렬 도구는 Instructables Step 68에 제공된다. 현재 GitHub CAD 폴더에는 STL이나 별도 정렬 도구 F3D가 없다. 전체 조립 STEP는 형상 확인에 적합하지만 Fusion 피처 이력을 포함하는 편집 원본과 같지는 않다.

라이선스 표기는 두 층이다. 저장소의 LICENSE는 GPL-3.0이고, 제작자의 Hackaday 설명 및 소스 주석은 프로젝트 하드웨어를 CC BY-NC-SA 4.0으로 표시한다. [ATTiny 소스](https://github.com/CrazyBlackStone/Universal-Tensile-Testing-Machine/blob/main/Arduino%20Code/ATTiny_Code.ino)는 코드 GPLv3도 별도로 명시한다. 하드웨어 재배포에는 저자·원본·변경사항을 표시하고 NC/SA 조건을 보수적으로 유지해야 하며, 저장소 GPL 표기만 보고 하드웨어의 비상업 조건이 사라진 것으로 해석하면 안 된다. 상업 이용 범위는 제작자 확인 전이다.

## 3. 실제 구조와 2 kN에 대한 검토

하중 경로는 `시편 → 출력 그립/고정 지그 → 2060 프로파일 → 모터측 출력 베어링 하우징 → 7201 베어링/축 칼라 → T12 스크루/너트 → 출력 로드셀 마운트 → S 로드셀 → 이동 그립 → 시편`이다. 모터·커플러는 회전 토크를 전달하며, 스크루 축력은 별도 베어링 경로로 받아야 한다.

| 부분 | 장점 | 확인해야 할 한계 |
|---|---|---|
| 550 mm 2060 단일 백본 | 부품 수와 조립비가 작음 | 시편축이 프로파일 중심에서 벗어나므로 휨 모멘트가 발생. 2 kN 강성·안전계수 자료 없음 |
| 출력 고정·이동 지그 | M5 긴 보강 볼트, M12 삽입 너트로 V1보다 개선 | 볼트가 들어가도 하중 경로에 출력 벽·베어링 끼움·T너트 체결부가 남음. 층간 파괴·크리프·지압·인발 검토 필요 |
| MGN12H 2블록/레일 1개 | 이동 그립과 로드셀 마운트를 각각 안내 | 레일 진행방향 하중 2 kN를 정정격과 직접 비교하면 안 됨. 편심에 따른 모멘트와 실제 블록/레일 제조사 정격을 검토해야 함 |
| T12 스크루 | 축 굵기가 작지 않고 저렴함 | 원문 BOM은 lead 7 mm, 4-start로 기재하지만 조립 설명과 펌웨어는 pitch 2/lead 8 mm. 본 견적은 **T12×8(P2), 4-start**를 명시적으로 선택. 실제 너트 플랜지 구멍·윤활·축단/베어링 접촉면은 대조 전 |
| 7201×2 + 6001×1 | 양방향 축력을 별도 지지하는 의도 | 7201의 접촉 방향과 끼워맞춤·예압·축 칼라 축방향 유지력이 중요. 일반 7201 2개가 공장 매칭·예압된 페어라는 뜻은 아님 |
| D25 L40, 8→12 rigid coupler | 긴 체결 길이로 V1의 미끄럼을 개선 | 원본·저가 후보 모두 토크/미끄럼 한계 미공개. 정렬 오차를 흡수하지 못하므로 강한 조임만으로 2 kN 보증 불가 |
| M12 나사 압착 그립 4개 | 삽입 너트와 사포로 미끄럼 감소 | 40-grit 사포/접착제와 출력 블록의 마찰·변형·박리·국부 시편 손상은 수치로 검증되지 않음. 자기조임 쐐기 그립 정격을 대신하지 않음 |
| S 로드셀 500 kg/1 t | 센서 용량은 목표보다 큼 | 500 kgf≈4.903 kN라는 센서 정격이 시험기 정격은 아님. M16 원본 체결과 후보의 나사·높이·축 중심이 맞는지 확인 필요 |

제작자는 PLA처럼 강성이 높은 재료, 6–8개 벽, 100% rectilinear 또는 30% 초과 gyroid를 권하며 일반 PETG는 쓰지 말라고 한다. 이는 제작 권장값이며 출력 부품의 정격 증명이 아니다. 이번 복제 계획에 PETG를 기본값으로 넣지 않았다. [조립·출력 지침](https://hackaday.io/project/192166/instructions)

### 토크 검산 — 기어비를 곱해 정격을 만들 수 없음

원문 사용 모터는 42HS6015A4 100:1이다. 현재 가격·데이터시트가 함께 확인되는 비교 후보는 [STEPPERONLINE 17HS19-1684S-PG100](https://www.stepperonline.co.kr/nema-17-%EC%8A%A4%ED%85%8C%ED%8D%BC-%EB%AA%A8%ED%84%B0-%EB%B0%94%EC%9D%B4%ED%8F%B4%EB%9D%BC-l-48mm-w-%EA%B8%B0%EC%96%B4%EB%B9%84-100-1-%EC%9C%A0%EC%84%B1-%EA%B8%B0%EC%96%B4%EB%B0%95%EC%8A%A4-17hs19-1684s-pg100)이다. 실 기어비 99.548:1, 출력 연속 허용 3 N·m/순간 5 N·m, 출력축 축하중 50 N, Ø8 mm D축이다. 기존 브래킷과 길이/축 형태의 대조가 필요하다.

계산식 `T = F × lead / (2π × η)`에서 η는 스크루의 실제 효율이다. 기어박스 효율 70%와 혼동하면 안 된다.

| 조건, lead 8 mm | η=0.30 가정 | η=0.50 가정 |
|---|---:|---:|
| 1 kN 필요 토크 | 4.24 N·m | 2.55 N·m |
| 2 kN 필요 토크 | 8.49 N·m | 5.09 N·m |
| 출력 3 N·m의 계산상 추력 | 707 N | 1,178 N |

효율 값은 공급자 보증이 없는 민감도 가정이다. 3 N·m로 2 kN를 내려면 스크루 효율이 약 84.9%여야 한다. 따라서 이 모터와 T12×8 조합은 **연속 2 kN 적합품으로 확정할 수 없다**. 1 kN 실증을 2 kN로 외삽할 수도 없다. 더 낮은 lead(예: 2 mm)는 토크 요구를 낮추지만 속도·너트/축단·제어를 함께 바꾸는 별도 재설계이며, 전체 구조의 2 kN 검증을 대체하지 않는다.

정품 HIWIN MGN12H-0의 제조사 표는 C=4.27 kN/C0=5.9 kN를 제시하지만 본 저가 후보는 정품 HIWIN이 아니라고 판매자가 명시한다. 이 수치를 저가 후보의 정격으로 전용하지 않았다. [HIWIN 표](https://www.hiwin.com/wp-content/uploads/Linear_Guideway-E-2.pdf), [저가 후보 설명](https://nasspop.com/product/detail.html?product_no=714)

## 4. ISO 플라스틱 시편의 범위

예를 들어 평행부가 10×4 mm인 시편은 단면적 40 mm²이므로 1 kN에서 25 MPa, 2 kN에서 50 MPa에 해당한다. 이는 `F/A` 계산이고, 해당 재료의 예상 파단강도를 보증하지 않는다. 60 MPa가 나오는 시편이라면 2.4 kN가 필요하다. 따라서 1 kN 장비로 일반 ISO 크기의 모든 PLA/ABS/PETG 시편을 파단할 수 있다고 할 수 없다. 얇거나 좁은 시편으로 줄여 하중을 맞출 경우 적용 규격·결과 명칭도 함께 확인해야 한다.

FDM 시편은 방향·레이어·벽 수·온습도·실제 단면을 기록해야 하며, 그립 파단/미끄럼은 정상 게이지부 파단과 구분해야 한다. 원본 명령 스텝으로 계산한 크로스헤드 변위에는 프레임·그립·로드셀 마운트 변형 및 미끄럼이 포함된다. 강도 비교는 교정 후 제한적으로 가능하지만, 이를 그대로 게이지부 변형률이나 정확한 탄성계수로 부르면 안 된다. 원문 modulus 모드는 제작자도 미시험이라고 밝혔다. [ISO 527-1 현행 항목](https://www.iso.org/standard/527-1), [ZwickRoell ISO 527 시험 설명](https://www.zwickroell.com/industries/plastics/thermoplastics-and-thermosetting-molding-materials/tensile-test-iso-527-1-2/)

HX711의 24-bit 표기는 유효 분해능·정확도·피크 포착 보증이 아니다. red 보드의 실제 80 SPS 설정, 평균 횟수, 노이즈, 힘 교정·영점복귀를 확인해야 한다. 샘플 평균과 표시 주기 때문에 짧은 취성 파단 피크를 낮게 잡을 가능성이 있다. 센서 교정과 직접 변위/영상 신율 측정 검증 없이 ISO 적합 시험기로 표시할 수 없다.

## 5. 누락까지 반영한 원본 BOM

아래는 제작자의 [31개 구매 BOM](https://hackaday.io/project/192166/components) 및 조립 지침을 합친 목록이다. 상세 기계 판독본은 `utm-v2-bom.json`에 함께 저장했다.

| 분류 | 원본 수량·규격 |
|---|---|
| 기구 | 2060 EU 550 mm×1; MGN12H×2; MGNR12 300 mm×1; T12 400 mm×1; T12 flange nut×1; 7201×2; 6001ZZ/2RS×1; Ø12 shaft collar×2; D25 L40 8→12 rigid coupler×1; S load cell 500 kg/1 t×1 |
| 전장 | custom PCB×1; Nano+USB×1; ATTiny85-20PU×1; 12/24 V PSU×1; red/XFW HX711×1; A4988/DRV8825 StepStick×1; NEMA17 planetary 51–100:1×1; SSD1306 128×64 I2C×1; LM7805+heatsink 또는 동형 buck×1; B3F-4000×6; 2.54 mm male/female headers |
| 상단 구매목록 나사류 | M5×14 button×20; M3×8 socket×20; M12×50 hex×4; M3×22 socket×4; M3×8 low-profile×4; M3 nyloc nut×4; M5×50 button×2; load-cell bolts M16×25 또는 센서 적합품×2; 2020용 M5 T-nut×20/M3 T-nut×20 |
| 조립 중 드러나는 추가품 | 고정/이동 fixture 보강 M5×90 각 2개, 총 4개(도면 대조 필요); M12 low-profile nut 각 2개, 총 4개; 40-grit 사포/그립테이프·접착제; DIP8 socket; KF301/XH2.54; jumper; 100 µF/50 V; decoupling capacitors; 1–10 kΩ 저항, 선택 330 Ω/LED; 전원역극성/USB 전류경로 diode; 배선; 정렬 지그 |
| 출력 | stationary fixture×1; moving fixture×1; moving load-cell mount×1; stepper mount×1; alignment tool×2; grip block×4; grip screw head×4 |

상단 BOM의 collar 수량은 Hackaday에서 1개지만 조립 Step 11은 명시적으로 2개다. “M3x8 Nuts”는 나사 길이를 가진 너트라는 뜻으로 해석하지 않고 M3 너트로 정리했다. 엔드스톱은 PCB/코드에 있지만 상단 BOM에 누락되어 있으며 본 계획에는 2개와 전원 차단용 부품 충당금을 넣었다. 상세 패시브 수량은 실 PCB 회로/BOM과 대조 전이다.

## 6. 현재 조달 후보와 확인가

**Ali는 이전 접근이 사이트 안전 정책에 차단됐으므로 재시도·다른 브라우저·우회 요청을 하지 않았다.** Ali의 현재 옵션·한국 배송·세금·최종 결제가는 검증되지 않았다. 원문 규격은 Ali 검색/대조의 참고만 가능하며, 아래 가격은 제조사 직판 또는 국내 판매자의 공개가다. 상호명·리뷰만으로 정품이나 정격을 보증하지 않았다.

| 선택 후보/수량 | 공개가, 원 | 배송·세금 및 미확정 |
|---|---:|---|
| STEPPERONLINE 17HS19-1684S-PG100×1 | 45,276 | KR 사이트 실시간 표시 45,275.22 반올림. 중국발; 국제배송/세금 별도 충당. 원본 모터 대체 후보 |
| [Nasspop 714](https://nasspop.com/product/detail.html?product_no=714), `P0000BBM000H` 300 mm+MGN12H×1 | 23,500 | 페이지 ProductGroup의 정확한 300 mm 옵션 확인. 기본 19,500원은 220 mm. 표기 배송 3,000원, 합배송 불가 설명 |
| [Nasspop 678](https://nasspop.com/product/detail.html?product_no=678), 추가 MGN12H×1 | 11,000 | rail 포함 안 됨. 기존 rail과 실제 호환/유격 확인 필요 |
| [Nasspop 838](https://nasspop.com/product/detail.html?product_no=838), T12 lead8×1,000 mm `P0000BGG000I`×1 | 18,000 | 400 mm 직접 옵션 없음. 1,000 mm를 구매해 절단. 너트 별도. 반력 베어링용 축단 가공 포함 아님 |
| 같은 838, lead8 nut `P0000BGG000F`×1 + cut `P0000BGG000V`×1 | 3,400 | 너트 2,400+1컷 1,000. 플랜지 구멍·베어링 끼움용 축단/나사외경 실제 치수 대조 전 |
| [NACHI 7201, Navimro K11504922](https://www.navimro.com/p/K11504922/)×2 | 28,578 | 당일 열린 페이지 12,990 ex VAT/14,289 incl VAT, ×2. Ø12×32×10, 접촉각30°. 배송 별도. 과거 검색가 13,189와 구분 |
| [VCTEC 13582 S-type 500 kg](https://vctec.co.kr/product/detail.html?product_no=13582)×1 | 69,740 | 63,400 ex VAT×1.1. 배송 3,500원. 제조사 모델·나사 도면·개별 교정서·재고 미확정; 원본 M16을 그대로 쓸 수 있다고 가정하지 않음 |
| [Nano SZH-EK025](https://www.devicemart.co.kr/goods/brand?category_code=00050001&code=1224)×1 | 6,050 | 5,500 ex VAT×1.1. USB 포함. 원본 PCB와 핀/전원 다이오드 확인 |
| [OLED VLT-OL023](https://www.devicemart.co.kr/goods/view?no=15960990)×1 | 6,490 | 5,900 ex VAT×1.1. SSD1306 128×64 I2C, pin 순서 확인 |
| [A4988 RED 1327610](https://www.devicemart.co.kr/goods/view?no=1327610)×1 | 1,980 | VAT 포함, 방열판 포함. 판매자 설명에 칩/보드 변경 가능 명시. 실제 전류·방열 확인 |
| [Coms P5301 24V/3A 1329320](https://www.devicemart.co.kr/goods/view?no=1329320)×1 | 26,070 | VAT/AC 코드 포함. 단일 모터 전원 후보. 커넥터·실제 전류여유 검증 전 |
| **확인 공개가 소계** | **240,084** | 완성 구매가격/2 kN 적합 BOM이 아님 |

Nasspop 옵션은 2026-10-25 해당 상품 HTML의 공식 JSON-LD에서 정확한 SKU/가격/InStock를 읽었다. hidden SOLD OUT 문자열이 페이지 텍스트에 함께 나타날 수 있어 그것만으로 품절 판정을 내리지 않았다. 실제 출하재고는 주문 전 확인이 필요하다. 국내 판매자 표기가격은 소비자 표시가로 반영했지만 Nasspop의 VAT 별도 추가가 결제에서 발견되면 예산을 수정해야 한다.

### 미확정품·운임·세금 충당금

| 항목 | 충당금 원 | 상태 |
|---|---:|---|
| 2060 EU 550 mm 절단품 | 20,000 | exact 단면·슬롯·수량 옵션 공개가 미확정. 국내 DAS-2060도 EU 슬롯 호환 검토 전 |
| 6001 bearing×1 + Ø12 shaft collar×2 | 13,000 | 제조사/축 유지력/정확한 폭 선정 전 |
| D25 L40 8→12 rigid coupler×1 | 15,000 | exact 정격품 미확정. 이 금액에 2 kN 보장품이 확보됐다는 뜻 아님 |
| 전체 bolts/nuts/T-nuts/보강부 | 35,000 | M5×90/M12 low nuts 및 load-cell 나사 변경분 포함 가정 |
| grip tape/sandpaper/접착제 | 5,000 | 소비재 |
| rigid PLA 총 2 kg | 30,000 | 출력 질량·서포트·재출력 미산정. 보유 프린터/공구/노트북 사용 가정 |
| ATTiny85-20PU + DIP8 socket | 6,000 | [국내 후보 1341738](https://www.devicemart.co.kr/goods/view?no=1341738). 최소 주문수량/현재 단가 확인 전 |
| custom red-HX711 PCB 제조 | 20,000 | Gerber 소량 제조·운임 확정 전 |
| 원본 red/XFW HX711 module | 5,000 | exact 핀배치/80 SPS/회로 확인 전. generic green 보드를 동일품으로 대입하지 않음 |
| LM7805/heatsink, 버튼6, headers/connectors, passives, diode, wiring | 15,000 | 실 회로 수량·패키지 확정 전 |
| 전원차단부/퓨즈/limit switch×2 | 15,000 | 구체 회로·정격 선정 전; 안전릴레이 인증 장치 가격 아님 |
| 파편 차폐판·장착물 | 20,000 | 실제 범위/두께 확정 전 |
| 국내 분할 배송 | 25,000 | VCTEC3,500+Nasspop 분리포장+Navimro/전자부품 등 가정 |
| 모터 국제배송 | 25,000 | 한국 주소 운임 미확정 |
| 모터 수입세금/결제수수료 및 VAT 미확정분 | 10,000 | 세법에 따른 산출액이 아닌 예산 충당. HS/과세가격/결제조건 미확정 |
| **충당금 소계** | **259,000** | 초과 가능 |

`240,084 + 259,000 = 499,084원`, 예비비 50,000원을 두면 **549,084원**. 공구·프린터·PC 신규구매, 전기료/제작 노동, 공인 힘 교정·extensometer, 실패 부품, 2 kN 금속 보강/축단 가공·정격 커플링 차액은 확정 금액에 포함되지 않았다. 50만원을 넘지 않으려면 단순히 부품 단가를 낮추는 것보다 미확정품·운임과 구조 변경을 먼저 확정해야 한다.

## 7. 채택 조건과 남은 일

1. 2 kN 목표 유지: 스크루 lead와 연속 토크를 다시 정하고, 정격 커플링·축 칼라/베어링 고정 경로·금속 반력부를 선정한다. 현재 원본 복제로 2 kN 시험을 시도하는 단계로 넘어가면 안 된다.
2. 실제 CAD 대조: 그립 개구/유효 시험길이/유효 stroke, load-cell 상하 나사와 중심높이, T12 flange pitch circle, motor length/shaft reach, 7201 양방향 예압·칼라 접촉을 확인한다.
3. 금속 강체 시편으로 기계 순응도와 그립 미끄럼을 따로 측정하고, 추적 가능한 힘 기준기로 단계 하중·반복·영점복귀를 검증한다. 2 kN까지 구조/하중 경로가 검증되기 전에는 최소 2 kN 달성으로 표시하지 않는다.
4. 원본 EStop은 MCU를 정지시켜도 모터에 전원이 남는다고 제작자가 경고한다. 소프트웨어 버튼 외의 전원 차단·limit/overload 동작과 차폐를 구체화한다. [제작자 EStop 설명](https://hackaday.io/project/192166-low-cost-universal-tensile-testing-machine/)

권고: 원본 STEP를 기구 참고 모델로 삼고, 50만원 안에서 가능한 부분을 모델링·검토하되 **2 kN 미달을 숨긴 원본 채택은 하지 않는다**. 50만원은 현재 확인된 “2 kN 완성 견적”이 아니라 미확정 조건이 많은 제작 예산 상한이다.
