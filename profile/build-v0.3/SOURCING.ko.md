# 원본형 저가 구성 견적 — 2026-10-24

**총85만3,462원은 공개가와 충당금을 합친 계획 예산이다. 확정 발주 견적·최저가·2kN 성능 보증 견적이 아니다.** 50만원 목표보다35만3,462원 높다. 센서·가공·운송의 공급자 확정가와 실물 교정·검증비를 아직 받지 않았으므로, “2kN 최소 보장 예산”은 현재 확정할 수 없다.

## 비교 총액

| 구성 | 계획 금액 | 범위와 미확정 |
|---|---:|---|
| 프로파일+원본형 구동·전장, 센서 제외 | **603,462원** | 공개 표시가365,462 + 충당금238,000. 배송·가공 예산 포함, 확정 견적 아님 |
| 위 구성+Zemic H3 500kg 후보 | **853,462원** | 센서250,000원은 **견적 전 충당금**. H3용 센서/그립 어댑터 재설계 필요 |
| 위 구성+AEP TC4 5kN 센서 단품 | **1,638,960원** | 센서 해외참고€635×1482.46원/€에 단순10%를 가산. 국내견적 아님; 센서 운송/수입제비·OEM인장킷·교정 별도 |

원본 AEP의 OEM base+rod ends까지 사면 센서 인장 키트 해외참고가가€1,004이므로, 같은 방식 비교시 전체 약224만원이 된다. 이것도 CNC Kitchen의 원본 BOM 총액은 아니다. 원본은 완성 가격표나 현재 최소 조달가를 제시하지 않는다. 공장 교정서가 있어도 조립된 시험기의 힘/정렬/프레임 변형 교정을 대신하지 않는다.

## 기구·재료와 배송

| 항목 | 수량/선택 | 합계 원 | 근거 |
|---|---|---:|---|
| 감속 모터 | STEPPERONLINE17HS19-1684S-PG14×2 | **88,889** | [제조사 공식](https://www.omc-stepperonline.com/nema-17-stepper-motor-bipolar-l-48mm-w-gear-ratio-14-1-planetary-gearbox-17hs19-1684s-pg14), KR표시44,444.40/개 반올림. 중국발 배송/세금 별도 |
| TR10 lead2×500+황동너트 | NasspopP00000XS000K×2 | **19,600** | [상품616](https://nasspop.com/product/detail.html?product_no=616), lead4와 혼동 금지 |
| 커플링 저가 비교품 | D20L20,8×10×2 | **4,800** | [상품854](https://nasspop.com/product/detail.html?product_no=854), **허용토크/미끄럼 미공개라2kN 확정품 아님** |
| 프로파일 | 4080·780×2/260×2/250×1 | **79,750** | [YJ4080](https://www.yjprofile.co.kr/goods/goods_view.php?goodsNo=1000000051):701–800mm25,520/개,201–300mm9,570/개, VAT포함 |
| 베어링 | 3200×2/6202×2/608×4 | **40,000 충당금** | 정확한 제조사·실치수·하중등급/끼워맞춤 확정 전 |
| 하드웨어·소수 금속가공 | 나사/와셔/축단/센서어댑터/반력판 | **70,000 충당금** | 수량·가공도면 최종견적 전. 초과 가능 |
| 공통 출력재 | PETG1kg×4 | **60,000** | [태강737 black](https://3dprinterstore.co.kr/product/detail.html?product_no=737&item_code=P0000BCJ000B), VAT포함15,000/kg. 수정 CAD 신규25출력 후보는 약2.709kg. 나머지1.291kg는 원본 grip/서포트 여유이며 모든 grip의 출력 적합성·slicer 검증 수량은 아님 |
| 전면 보호판 | PC3T400×600×1 | **16,800** | [아코빅스34765](https://www.akobigs.com/goods/goods_view.php?goodsNo=34765), VAT처리 재확인 필요. 측면/장착부 상세 미완료 |
| 국내 배송 | YJ3,000+Nasspop약7,000+나머지16,000 | **26,000 충당금** | Nasspop장척 별도배송 포함 가정. 주문 합배송 확정 전 |
| 모터 국제배송/수입·결제비 | 40,000+20,000 | **60,000 충당금** | 한국 주소 결제화면의 운임/세금 견적은 아님 |

NEMA17 기어박스는 연속허용3N·m, 순간5N·m이며 출력축 축하중 허용50N이다. 축당1kN을 모터로 직접 지지하면 안 된다. 별도 고정 베어링 반력 경로와 실제 축단 설계가 필요하다. 원본 STEP와 저가 TR10 판매품이 동일하게 축단 가공되어 있다고 가정하지 않는다. 정격 있는 SUNG-IL SJC-25C-RD-8X10을 두 개 쓰면 공개 비교가63,976원으로 저가 커플링보다59,176원 오른다. 이 차액은 위 총액에 포함하지 않았으므로 정격 부품 확정시 재견적한다.

## 전장 — 공개가95,623원 + 추가 충당금42,000원

| 공개가 항목 | VAT포함 원 | 판매처 |
|---|---:|---|
| UnoCH340 |3,190|[갓파츠EN00005032](https://godparts.co.kr/content/time/view?it_id=EN00005032)|
| CNCshield+A4988×4+방열판 |23,650|[VCTEC10229](https://vctec.co.kr/product/detail.html?product_no=10229),2개사용2개예비|
| HX711 |1,870|[디바이스마트1327440](https://www.devicemart.co.kr/goods/view?no=1327440)|
| ComsP5301·24V3A 외장전원 |26,070|[1329320](https://www.devicemart.co.kr/goods/view?no=1329320),가격비교 기준품|
| OmronA22E-M-02·2NC |26,015|[12765103](https://www.devicemart.co.kr/goods/view?no=12765103)|
| OmronD2F-L×5 |4,840|[12719450](https://www.devicemart.co.kr/goods/view?no=12719450)|
| Songle24Vrelay×3 |2,772|[15239964](https://www.devicemart.co.kr/goods/view?no=15239964)|
| Recom24→5V1A |7,216|[14567891](https://www.devicemart.co.kr/goods/view?no=14567891)|

원본은24V5A이므로3A를 그대로 적합품으로 확정하지 않았다. **5A전원 차액20,000원**, 배선/퓨즈/버튼/USB 등 **22,000원**을 별도 충당금으로 합쳤다. 이중으로 전원 두 개를 구매한다는 뜻이 아니다. exact5A 모델과 실제 A4988 전류/방열은 확정 전이다. 원본 Nano 펌웨어를 Uno+CNCshield에 연결만 바꾸어 검증 완료했다고 주장하지 않는다. 핀맵·독립 홈/탈조·EStop·과부하/ADC timeout 정지는 새 배선/펌웨어 검증이 남는다. 일반 릴레이는 PL/SIL 안전릴레이가 아니다.

## 센서와 품질 근거

원본 **AEP TC4 5kN**은 [제조사 도면](https://www.aep.it/wp-content/uploads/2020/02/Data-sheet-TC4.pdf), [해외 exact5kN 공개가](https://www.vetek.com/en/article/dynamometer-tc4-stainless-steel-5kn)를 기준으로 한다. 국내 AEP 취급처는 견적 전용이다. [원본 센서 상세](sources/aep-original-sensor.md).

대체 후보 **Zemic H3-C3-500kg-3B**는 정격약4.903kN, M12×1.75 상하 하중 나사다. AEP의Ø100/35/M20×1.5/PCD86 플랜지와 전혀 달라 교체용 어댑터를 새로 설계해야 한다. [제조사 직판 견적](https://www.zemiceurope.com/en/h3), [공식 도면](https://www.zemiceurope.com/media/Documentation/H3_Datasheet.pdf), [개별 공장 교정서 정책](https://www.zemiceurope.com/de/faq/force-sensors---load). OIML 형식증명이 인장시험기 전체 정밀도 인증은 아니다. [대체 센서 상세](sources/substitute-sensor.md).

HX711은 유지하되 모듈의 실제 bridge excitation과 센서 요구값을 맞춘다. H3 권장5–12V에 E+4.3V 모듈을 무조건 적합이라고 쓰지 않는다. **정품 모델·로트·개별 교정서·인장 교정 데이터**, 입력저항/영점/반복성/영점복귀/단계하중/양축 정렬/체결 마킹을 입고·시운전에서 확인할 조건이다. 이 작업은 아직 실제로 수행하지 않았다.

Ali의 동일 모델명·리뷰·공식점이라는 상호만으로 정품을 보증하지 않았다. 이번 시도에서는 알리 상품 접근이 브라우저 사이트 안전 정책에 차단돼 한국배송 최종 옵션·공식 판매자 연결을 확인하지 못했다. **현재 조달 기준은 검증 가능한 제조사 직판/국내 판매처이며 Ali 확정 구매목록은 아니다.** 제조사 자료 없는 최저가를 “품질 보장된 대체품”으로 승격하지 않는다.
