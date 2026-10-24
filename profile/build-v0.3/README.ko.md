# Open-Pull v0.3 — 원본 구동계 복귀 / 저가 프레임 비교

**견적·배치 검토판. 2kN은 목표이며, 실물 보증 정격과 조립 확정 도면은 아직 아니다.**

216만원은 CNC Kitchen 원본 BOM 가격이 아니다. 앞서 제안한 산업용 모터·감속기·정밀 부품의 상향 구성 일부 소계였다. 원본 README는 일부 품목을 `...`로 끝내며 현재 가격 총액을 제공하지 않는다. 이 판은 원본 감속 NEMA17 두 개, TR10×2 나사 두 개와 직접 연결하는 구조로 돌아간다. 풀리와 벨트는 없다. 원본 AEP TC4 5kN/HX711 안을 보존하고, 저가 센서는 별도 후보로 비교한다.

| FreeCAD 저장 파일 | 내용 |
|---|---|
| `cad/OpenPull_v0.3.0-costdown-layout.FCStd` | 4080 기둥780mm×2, 고정 가로보260mm×2, 이동 가로보250mm×1. 원본 실제 부품 STEP 형상과 신규 출력 후보25개 |
| `cad/OpenPull_v0.3.0-printed-frame.FCStd` | 기둥80×60, 벽6mm,195mm 모듈4개씩; 가로보도 분할 출력하는 비교안 |
| `cad/OpenPull_v0.3.0-rod-reinforced.FCStd` | 같은 출력 기둥에 M8봉4개·금속 단부판4개를 넣고 가로보3개는 프로파일을 유지하는 비교안 |

주요 부품은 원본 STEP의 월드 좌표를 변환해 재사용한다. 단순 모터 상자만 새로 배치한 모델이 아니다. 다만 원본 형상 재사용은 모터/그립의 제조사 정격 또는 원본의 모든 나사산 규격이 검증됐다는 뜻은 아니다. 원본 그립의 Ø17 공간을 M8/M20 나사로 임의 해석하지 않았다. 대체 Zemic 센서는 아직 설치 완료 형상으로 표시하지 않는다.

새 파란 출력 부품은 발·분할 랩·커버·패드·함체의 **시제품 후보**다. STL은 `printed-candidates`에 있고 제작 승인 파일이 아니다. 가로보는 원본 기능 높이를 유지하며, 상부에는 강재 베어링 반력 인서트 후보를 추가했다. 끝단 캡처·M20 센서/그립 연결·축단 저널·체결부·배선/펌웨어는 `config.json/open_interfaces`에 미완료로 남긴다. 프로파일 CAD는 외형과 단순 중공 단면이며 YJ 슬롯의 가공용 실단면이나 강도해석 메쉬가 아니다.

- [견적과 소싱](SOURCING.ko.md)
- [NG 방식 출력 프레임 검토](PRINTED_FRAME.ko.md)
- `COST_SUMMARY.json`: 공개가/충당금/센서별 총액 구분
- `MODEL_BOM_MAP.json`: 원본 CAD와 조달 후보의 일치/미일치 상태. 특히 가격용 커플링은 원본 CAD 부품과 다름
- `SCREENING.json`: 연속 보/기둥을 가정한 손계산. FEA와 접합부 검증은 아님
- `ROUNDTRIP.json`: 저장 후 재개방 및 STEP 왕복 검증
- `cad/STEP_exchange.zip`: 세 비교안 STEP 교환 파일

FreeCAD Python 콘솔에서 `runpy.run_path('.../build_costdown.FCMacro')['build'](repository_root)`를 실행하고, `build_printed_variants.FCMacro`의 `build(root,False)`와 `build(root,True)`로 비교안을 재생성한다. 생성기는 원본 부품 배치 후, 프레임 추가 후 각각 native 파일을 저장한다. 기존 v0.1·v0.2와 원본 디렉터리는 수정하지 않는다.
