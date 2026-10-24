# Open-Pull Profile implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** CNC Kitchen 계보를 보존하는 프로파일 검토 CAD와 구매 후보를 GitHub 포크에서 버전 관리한다.

**Architecture:** 원본 디렉터리를 보존하고 profile/ 아래 재생성 가능한 FreeCAD 산출물을 추가한다. 실물 미검증 상태를 모든 진입점에 명시한다.

**Tech Stack:** FreeCAD 1.1, Python, Git, GitHub, JSON/CSV/Markdown.

**Spec:** ../specs/2026-10-24-profile-frame-design.md

## Global Constraints

- 원본 커밋 55017419fae89409b1098540212e1620b1e46d0b 및 GPL-3.0 유지.
- 목표 2,000N은 검증된 정격이 아니다.
- 실제 주문/기계 작동/새 펌웨어 배포는 이번 작업 범위 밖이다.
- 쿠팡 우선 비교, 국내 절단 프로파일, 알리 정밀부품 후보. 검색 링크와 검증한 상품 링크를 구분한다.

## Review Focus

- SFU1605 총길이와 유효 나사 길이 혼동: 제조사 도면 전 가공 금지.
- 가이드/크로스헤드 충돌: 초기와 100mm 아래 위치에서 간섭 확인.
- 로드셀 용량과 장비 허용하중 혼동: 모든 진입 문서에 상태 표시.
- 원본 속도 설정 오사용: 새 구동계에는 미검증임을 명시.
- 역구동 시 낙하: 브레이크/포획장치 미확정 상태를 제작 보류 항목으로 표시.

## Task 1: 설계와 계보

Files: VERSION, UPSTREAM.md, CHANGELOG.md, docs/superpowers/specs/2026-10-24-profile-frame-design.md

- [x] 원본 SHA·라이선스·원본 파일을 확인한다.
- [x] 설계 검토자를 통해 중요한 누락을 확인한다.
- [x] 전용 브랜치에 설계 기준을 커밋한다.

## Task 2: 재현 가능한 CAD

Files: profile/config.json, profile/build_profile.FCMacro, profile/cad/, profile/renders/, tests/test_profile_geometry.py

Interfaces: config.json을 읽는 build(root) → document, 산출물 생성. 검증은 FCStd를 열어 실제 형상과 이동 여유를 확인한다.

- [x] CAD 산출물과 실제 기하를 확인하는 검증을 먼저 작성하고 미생성 상태의 실패를 확인한다.
- [x] FreeCAD 원본 STEP 참조와 프로파일 조립체를 생성한다.
- [x] 실형상 유효성·프레임 간섭·100mm 인장 이동 여유를 검사하고 정면/사시도를 확인한다.
- [x] FCStd/STEP/설정/매크로와 검증 결과를 함께 커밋한다.

## Task 3: 소싱·인수·게시

Files: profile/BOM.csv, profile/SOURCING.ko.md, profile/CUT_LIST.csv, profile/README.ko.md, profile/VALIDATION.json, profile/MANIFEST.sha256, .github/workflows/profile-checks.yml

- [x] 각 구매품의 수량·필수 옵션·후보 URL·가격 상태를 기록한다. 미확정 링크는 구매 확정으로 표기하지 않는다.
- [x] 해시/원본 보존/메타데이터 검사를 실행한다.
- [x] 전체 변경의 별도 검토와 필요한 수정을 마친다.
- [x] 실제 포크에 단계별 브랜치를 게시하고 원격 트리 일치를 확인한다.
- [ ] GitHub Release에서 v0.1.0-design 태그를 고정하고 원격 SHA 일치를 확인한다. 이 단계의 완료 기록은 해당 Release와 Git refs를 기준으로 한다.

## Execution record

사용자의 연속 지시(재설계해보고, 포크로 올려, 버전관리 철저히)에 따라 현재 세션에서 검토용 버전까지 실행한다. 소프트웨어 구현이 아닌 기계 검토 CAD이므로 형상 검증 중심으로 진행하며, 완성된 제작도/실물 성능을 주장하지 않는다.
