# CYS Futures Vision Coaching Skills

> **최윤식 박사의 미래준비학교 — Claude Code Skills Package**
> *Dr. Choi Yoon-Sik's Future Preparation School — Claude Code Skills Package*

<!-- AUTO:BADGE -->
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Skills: 28](https://img.shields.io/badge/Skills-28-blue)](docs/SKILL_CATALOG.md)
[![Korean](https://img.shields.io/badge/언어-한국어%20%2B%20English-success)](#)
<!-- /AUTO:BADGE -->

---

## 📖 소개 / Introduction

**한국어**

본 패키지는 미래학자 최윤식 박사의 저서 『미래준비학교 — 흔들림 없는 인생을 계획하는 5단계』(지식노마드, 2016)의 *모든 토대*를 Claude Code Skills로 구현한 *비전 코칭 도구 모음*입니다. 28개의 스킬(콘텐츠 26개 + 메타 인터뷰 1개 + 데이터 백본 1개)이 박사님이 직접 운영하는 미래준비학교의 *비전 발견·완수 흐름* 그대로 작동하여, 누구나 *자신의 비전을 발견하고 완수하는 인생*을 살도록 돕습니다.

박사님 정의: **비전 = 가치 있는 시대적 소명**

박사님 핵심 메시지:
> *"혼자서 이룰 수 있는 꿈은 절대로 큰 꿈이 아니다!"*

본 패키지가 GitHub에 공개된 이유는 박사님 책의 **비전 재생산 — 비전에 몰입한 사람의 최고 경지**를 디지털·글로벌 차원에서 실현하기 위함입니다.

**English**

This package implements *every framework* from Dr. Choi Yoon-Sik's book 『Future Preparation School: 5 Stages of Planning an Unshakable Life』(Knomad, 2016) as a collection of Claude Code Skills. The 28 skills (26 content skills + 1 meta-interview skill + 1 data backbone skill) work as Dr. Choi's *vision discovery·fulfillment flow*, helping anyone *discover and fulfill their vision*.

Dr. Choi's definition: **Vision = A Valuable Calling of the Times**

Core message:
> *"A dream that can be achieved alone is never a big dream!"*

This package is published on GitHub to realize the **Vision Reproduction — the highest level of one fully immersed in vision** at a digital and global scale.

---

## 📢 최근 업데이트 / Recent Updates

**2026-05-18 — 28번째 vision 스킬 `vision-school-major-info` 신설 (한국 7개 API + ONET 데이터 백본)**
- 공공데이터포털 키 1개로 7개 API 통합 호출 — 커리어넷 4종(학과·학교·직업·진로자료) + KCUE 3종(학과·기본정보·통합)
- ONET Web Services v2.0 — 미국 923 직업 · 1,016 SOC 코드 · 277 descriptors · 분기 갱신 (선택 기능)
- 사용자 본인 키 입력 방식 — `check_api_keys` 진입 가드가 미등록 시 setup_guide 자동 안내
- `~/.config/vision-school-major-info/api_keys.json` (chmod 600) 안전 저장
- 결정론 모듈 `school_major_lib.py` 16+ 함수 — 진입 가드 3 · 한국 데이터 호출 · ONET · Holland→ONET 매핑 · 한↔영 학과 사전 · CC-BY attribution 자동 생성
- `ystory/korea-universities` 491개 대학 데이터 캐시(7일 TTL) — `vision-grill-with-docs/grill_lib.py`에 통합
- 검증: 단위 56 PASS + 검증 라운드 24 PASS
- 새 카테고리 **`data` (Data Backbone — External API)** 도입
- 박사님 vision-strong-visioncoding(Holland/RIASEC) ↔ ONET 직업 자동 매핑

**2026-05-18 — 28th vision skill `vision-school-major-info` added (Korean 7-API + ONET data backbone)**
- Public data portal single-key access to 7 Korean APIs — Career-net (major·school·job·resources) + KCUE (major·univ·combined)
- O*NET Web Services v2.0 — US 923 occupations · 1,016 SOC codes · 277 descriptors · quarterly update (optional)
- User-owned API key model — entry guard `check_api_keys` auto-emits setup_guide if missing
- Safe storage at `~/.config/vision-school-major-info/api_keys.json` (chmod 600)
- Deterministic module `school_major_lib.py` with 16+ functions — guards · Korean lookup · ONET · Holland→ONET mapping · KO-EN major dict · CC-BY attribution auto-generation
- `ystory/korea-universities` 491-university data cached (7-day TTL) — integrated into `vision-grill-with-docs/grill_lib.py`
- Validation: 56 unit PASS + 24 round PASS
- New category **`data` (Data Backbone — External API)**
- Auto-mapping between Dr. Choi's vision-strong-visioncoding (Holland/RIASEC) ↔ ONET occupations

**2026-05-18 — 27번째 vision 스킬 `vision-grill-with-docs` 신설 (cross-stage 메타 인터뷰 엔진)**
- Matt Pocock의 `grill-with-docs` 패턴을 미래비전코칭 맥락으로 전면 커스터마이즈
- **3-모드**: A(비전 grill 1:1 인터뷰) · B(다른 vision 산출물 메타 검증) · C(다목적 자유 주제 인터뷰 — 진로·재정·관계·사역 등 어떤 주제든)
- **LDR (Life Decision Record)** — ADR을 인생 결정 기록기로 매핑, 3조건(번복 어려움·미래 의문·진짜 trade-off) 자동 판정
- 결정론 모듈 `grill_lib.py` **21개 함수** — 박사님 사전 충돌·인용 위조 차단·LDR 자격·sync 검증 등 LLM 자연어 추론 완전 차단
- 검증 **211/211 PASS** (단위 130 + 기존 라운드 48 + 신규 10시나리오 33)
- 새 카테고리 **`meta` (Cross-stage)** 도입 — 8단계 어디서든 호출 가능
- 부수: 카탈로그 자동 빌드 재생성 (`README.md` · `docs/SKILL_CATALOG.md`)

**2026-05-18 — 27th vision skill `vision-grill-with-docs` added (cross-stage meta-interview engine)**
- Customizes Matt Pocock's `grill-with-docs` pattern for Dr. Choi's vision coaching context
- **3 modes**: A (1:1 vision grill) · B (verify other vision skill artifacts) · C (free-form interview on any topic — career·finance·relationship·ministry)
- **LDR (Life Decision Record)** — ADR mapped to life-decision recorder, 3-criteria gate (hard-to-reverse · surprising · real trade-off) auto-evaluated
- Deterministic module `grill_lib.py` with **21 functions** — blocks LLM natural-language inference for fact lookup·quote forgery·LDR qualification·sync validation
- Validation **211/211 PASS** (130 unit + 48 existing round + 33 new 10-scenario)
- New category **`meta` (Cross-stage)** — invokable at any of the 8 stages
- Side update: catalog regenerated (`README.md` · `docs/SKILL_CATALOG.md`)

**2026-05-17 — 26개 vision 스킬 결정론 모듈·테스트·검증 자료 일괄 추가**
- 26개 SKILL.md 본문 보강 (총 +3,505줄 / −1,352줄)
- 스킬별 결정론 엔진·라이브러리·검증 스크립트·테스트 시나리오 신규 추가
  (career-recommendation·clarity·enneagram·mbti·five-stages·follow-through·
   four-futures·futures-timeline·goal-reframing·mission-frame·multipleintel·
   personal-future-research·progress-review·readiness·smart-five·statement·
   strategy·strong·three-realm·values·financial-3shields·financial-coach·
   future-needs·future-promise·cys-competence·eight-training 등 전 영역)
- `.gitignore`에 Python 캐시(`__pycache__`·`*.pyc`) 패턴 추가
- 변경량: 202 files, +44,864줄 / −1,352줄 (커밋 `710a3f9`)
- 부수 갱신: `docs/SKILL_CATALOG.md` 자동 빌드 재생성

**2026-05-17 — Deterministic modules·tests·validation assets added to 26 vision skills**
- 26 SKILL.md bodies enhanced (+3,505 / −1,352 lines in skill docs)
- Per-skill deterministic engines, libraries, validation scripts, and test
  scenarios added across all four areas (diagnosis · spine · flesh · prescription)
- `.gitignore` extended with Python cache patterns (`__pycache__`·`*.pyc`)
- Diff: 202 files, +44,864 / −1,352 lines (commit `710a3f9`)
- Side update: `docs/SKILL_CATALOG.md` regenerated via auto-build

**2026-05-13 — 22개 vision 스킬 대규모 품질 보강**
- 진단·척추·살근육·처방 전 영역 22개 SKILL.md 일괄 업데이트
- 박사님 책 인용 정밀화 + 코칭 흐름 일관성 강화
- 변경량: +3,051줄 / −932줄
- 부수 갱신: `docs/SKILL_CATALOG.md` 자동 빌드 재생성

**2026-05-13 — Large-scale quality enhancement of 22 vision skills**
- 22 SKILL.md files updated across diagnosis · spine · flesh · prescription
- Refined Dr. Choi's book citations · strengthened coaching flow consistency
- Diff: +3,051 / −932 lines
- Side update: `docs/SKILL_CATALOG.md` regenerated via auto-build

---

## 🎯 누구를 위한 패키지인가? / Who Is This For?

| 대상 / Target | 추천 활용 / Recommended Use |
|--------------|---------------------------|
| 🧑‍🎓 **청년·학생 (18~30)** | 진로·소명 발견 · Discover vocation·calling |
| 👨‍💼 **중년·직업 전환자 (35~55)** | 인생 후반 비전 재설계 · Re-design 2nd half of life |
| 👴 **은퇴기 (55+)** | 제2의 사역·가치 있는 봉사 · Find purpose for retirement |
| ⛪ **교회 청년부·셀모임** | 그룹 비전 코칭 · Group vision coaching |
| 🏫 **신학교·대학교** | 진로 지도 도구 · Career counseling tool |
| 👨‍🏫 **비전 코치·강사** | 강의·세미나 부속 도구 · Lecture·seminar companion |

---

## 🚀 빠른 시작 / Quick Start

> **컴퓨터를 잘 모르셔도 괜찮습니다.** 아래 3단계만 따라하시면 됩니다.
> 한 줄 한 줄 풀어쓴 상세 가이드는 → **[INSTALLATION.md](docs/INSTALLATION.md)**

### 1단계 — 패키지 내려받기

터미널을 열고 **아래 두 줄을 차례로** 복사·붙여넣기 후 Enter:

```bash
cd ~
git clone https://github.com/idoforgod/cys-claude-vision-coaching-skills.git
```

- 첫 줄: 내 홈 폴더로 이동 (Mac은 `/Users/내이름`, Windows는 `C:\Users\내이름`)
- 둘째 줄: 패키지를 GitHub에서 통째로 내려받기

### 2단계 — Claude Code에 28개 스킬 자동 등록

방금 만들어진 폴더로 들어가서 아래 한 덩어리를 통째로 복붙:

```bash
cd ~/cys-claude-vision-coaching-skills
mkdir -p ~/.claude/skills
for d in skills/*/; do
  name=$(basename "$d")
  ln -sf "$(pwd)/$d" ~/.claude/skills/$name
done
```

- 첫 줄: 방금 내려받은 패키지 폴더로 이동
- 둘째 줄: Claude Code 스킬 폴더가 없으면 만들기
- `for ... done`: 28개 스킬을 한꺼번에 등록

### 3단계 — Claude Code 재시작 → 첫 스킬 실행

Claude Code를 **완전히 종료**(창 닫기가 아니라 앱 종료)한 뒤 다시 실행. 그리고 입력창에:

```
/vision-five-stages
```

박사님 비전 5단계 안내가 나오면 **설치 성공**입니다.

---

### 처음이라 어디서 시작해야 할지 모르겠다면

- **자기 자신을 알고 싶다** → `/vision-cys-competence-visioncoding` (박사님 직접 개발 CYS 진단)
- **박사님 책의 흐름대로 따라가고 싶다** → `/vision-five-stages` (비전 5단계 척추)
- **이미 비전이 있고 실행이 막혔다** → `/vision-strategy-coach` (전략 코치)
- **비전이 막혀있다·생각이 정리가 안 된다·진로/재정/관계/사역 큰 결정으로 막혔다** → `/vision-grill-with-docs <자유 주제>` (메타 인터뷰 — 8단계 어디서든 호출 가능)
- **실제 한국 대학·학과·직업 데이터가 필요하다·유학 진로** → `/vision-school-major-info` (공공데이터포털 7개 API + ONET 미국 직업)

---

### 이미 설치하신 분 — 최신 버전으로 업데이트

```bash
cd ~/cys-claude-vision-coaching-skills
git pull origin main
```

이 두 줄이면 끝납니다. (심볼릭 링크 방식은 자동 반영됨)
Windows에서 복사 방식으로 설치하신 분은 [INSTALLATION.md 업데이트 절차](docs/INSTALLATION.md#-업데이트--updates) 참고.

---

## 🧭 박사님 비전 발견·완수 8단계 / The 8-Stage Flow

박사님이 직접 정리하신 *비전 발견·완수 8단계*. 이 순서대로 스킬을 사용합니다.
Dr. Choi's 8-stage flow for vision discovery·fulfillment. Skills follow this exact order.

```
1. Vision Coding (내 안에 있는 것 파악)
       ↓
2. 나와 연관된 미래 예측
       ↓
3. 5가지 시대적 필요 발견 (문제·욕구·결핍·위기·기회)
       ↓
4. 마음을 사로잡는 가치 명확화 + 비전의 결과·열매
       ↓
5. "가치 + 시대적 필요 + 내 안의 능력" 종합 → 비전 출발점·큰 그림
       ↓
6. 비전선언문 작성
       ↓
7. 비전 성취 구체 설계 (목표·전략·필요한 것)
       ↓
8. 미래비전 지속 셀프코칭 (자극·디자인·심층탐구·훈련·네트워킹·재생산)
```

| 단계 / Stage | 박사님 단계명 / Stage | 사용 스킬 / Skills |
|----------|-------------------|----------------|
| **1** | Vision Coding — 내 안에 있는 것 파악 | 진단 7종 (아래 카탈로그) |
| **2** | 나와 연관된 미래 예측 | `vision-personal-future-research` → `foresight-futures-wheel` → `vision-four-futures` → `vision-futures-timeline-map` (순차) |
| **3** | 5가지 시대적 필요(문제·욕구·결핍·위기·기회) 발견 | `vision-future-needs-prediction` · `vision-future-promise-five-criteria` |
| **4** | 마음을 사로잡는 가치 명확화 + 비전 열매 예상 | `vision-values-visioncoding` · `vision-three-realm-balance` |
| **5** | "가치 + 시대적 필요 + 내 능력" 종합 — 비전 출발점·큰 그림 | `vision-clarity-coaching` · `vision-mission-frame` |
| **6** | 비전선언문 작성 | `vision-statement-writer` |
| **7** | 비전 성취 구체 설계 — 목표·전략·필요한 것 | `vision-goal-reframing` · `vision-strategy-coach` · `vision-financial-3shields-3windows` · `vision-financial-coach` · `vision-career-recommendation` |
| **8** | 미래비전 지속 셀프코칭 — 자극·디자인·심층탐구·훈련·네트워킹·재생산 | `vision-five-stages` · `vision-smart-five-competence` · `vision-eight-training-areas` · `vision-follow-through-habits` · `vision-progress-review` |

> 참고: 본 8단계 표는 박사님이 명시한 *순서가 의미 있는* 표이므로 빌드 스크립트 자동 갱신 대상에서 제외됩니다. 새 스킬을 단계에 편입할 때 직접 편집하세요.

---

## 📚 28개 스킬 카탈로그 / 28 Skills Catalog

> 본 섹션이 *전체 카탈로그*입니다. 자동 생성 인덱스(짧은 표)는 [docs/SKILL_CATALOG.md](docs/SKILL_CATALOG.md)에도 동기화됩니다.
> This section *is* the full catalog. A slim auto-generated index is also synced to [docs/SKILL_CATALOG.md](docs/SKILL_CATALOG.md).

### 📊 6대 카테고리 / Six Categories

<!-- AUTO:CATEGORY_TABLE -->
| # | 카테고리 / Category | 스킬 수 | 박사님 8단계 |
|---|------------------|--------|--------------|
| 1 | **Vision Coding - 진단 (Diagnosis)** | 7 | 1단계 |
| 2 | **박사님 책 토대 — 척추 도식 (Spine)** | 5 | 5·6·8단계 |
| 3 | **박사님 책 토대 — 살·근육 + 응용 (Flesh + Applied)** | 7 | 2·3·4·7단계 |
| 4 | **처방·실행 (Prescription)** | 7 | 5·7·8단계 |
| 5 | **메타 인터뷰 (Cross-stage) (Meta-Interview)** | 1 | 전 단계 |
| 6 | **데이터 백본 (External API) (Data Backbone)** | 1 | 1·3·7단계 보조 |
| | **합계** | **28** | |
<!-- /AUTO:CATEGORY_TABLE -->

### 📋 전체 스킬 인덱스 / Skill Index (auto-generated)

<!-- AUTO:SKILL_INDEX -->
| 카테고리 | 스킬 | 단계 | 한 줄 설명 |
|---------|------|------|----------|
| Diagnosis | `vision-cys-competence-visioncoding` | 1 | 최윤식 박사가 직접 개발한 CYS 비전 역량 진단 검사(『미래준비학교』)를 그대로 구현한 비전 역량 진단 스킬. 박사님의 20… |
| Diagnosis | `vision-enneagram-visioncoding` | 1 | 에니어그램(Enneagram) 9유형의 핵심 동기(Core Desire)와 핵심 두려움(Core Fear)을 검사 문항의 중심… |
| Diagnosis | `vision-mbti-visioncoding` | 1 | MBTI 전문가·심리측정학자 페르소나로 사용자가 자신의 MBTI 16유형을 발견하도록 돕는 자가 진단 스킬. 4축(E/I 외향… |
| Diagnosis | `vision-multipleintel-visioncoding` | 1 | Howard Gardner의 다중지능 이론(Theory of Multiple Intelligences, 1983 『Frames… |
| Diagnosis | `vision-readiness-visioncoding` | 1 | 사용자의 꿈 달성 준비도(Dream Readiness)를 20문항 자가 진단으로 평가하고 영어 축 막대 그래프로 시각화하는 비… |
| Diagnosis | `vision-strong-visioncoding` | 1 | STRONG 직업흥미도 검사(Strong Interest Inventory®) 간이 시뮬레이션 스킬. Holland(1959,… |
| Diagnosis | `vision-values-visioncoding` | 1·4 | 사용자의 MBTI 16유형·에니어그램 9유형·다중지능(Multiple Intelligences) 8지능 결과를 가치 단어(va… |
| Spine | `vision-mission-frame` | 5 | 최윤식 박사 『미래준비학교』(2016)의 핵심 도식 비전 프레임(Mission Frame)을 단독 도구로 구현한 비전 코칭 스… |
| Spine | `vision-statement-writer` | 6 | 최윤식 박사 『최윤식의 미래준비학교』(2016, 지식노마드, ISBN 9788993322972)의 Vision Statemen… |
| Spine | `vision-eight-training-areas` | 8 | 최윤식 박사 『미래준비학교』(2016)의 비전 훈련 8대 영역을 그대로 구현한 미래인재 습관 훈련 코칭 스킬. 박사님 인용 "… |
| Spine | `vision-five-stages` | 8 | 최윤식 박사 『미래준비학교』(2016)의 미래준비학교 비전 5단계를 그대로 구현한 통합 비전 코칭 스킬. 박사님 고유 5단계… |
| Spine | `vision-smart-five-competence` | 8 | 최윤식 박사 『미래준비학교』(2016)의 SMART 미래인재 5역량 훈련을 그대로 구현한 비전 훈련 코칭 스킬. 박사님 고유… |
| Flesh + Applied | `vision-four-futures` | 2 | 최윤식 박사 『미래준비학교』(2016, 지식노마드, ISBN 9788993322972)의 4가지 미래 가능성을 그대로 구현한… |
| Flesh + Applied | `vision-futures-timeline-map` | 2 | 최윤식 박사 『미래준비학교』(2016)의 미래지도(Futures Timeline Map) 작성 도구를 그대로 구현한 비전 코칭… |
| Flesh + Applied | `vision-personal-future-research` | 2 | 사용자의 Vision Coding 진단 7종 결과(CYS 비전 역량·MBTI·에니어그램·STRONG/RIASEC·다중지능·가치… |
| Flesh + Applied | `vision-future-needs-prediction` | 3 | 미래 사회 변화로부터 발생할 잠재적 기회·위기·문제·필요·결핍을 현실적이고 분석적으로 예측·분해하는 미래필요 예측 전문가 스킬… |
| Flesh + Applied | `vision-future-promise-five-criteria` | 3 | 최윤식 박사 『미래준비학교』(2016)의 미래 유망성 판단 5가지 기준을 그대로 구현한 비전 영역 평가 스킬. 박사님이 미래준… |
| Flesh + Applied | `vision-three-realm-balance` | 4 | 최윤식 박사 『미래준비학교』(2016)의 비전 영역 3겹 다이어그램을 그대로 구현한 비전 건강도 점검 스킬. 박사님 책 다이어… |
| Flesh + Applied | `vision-financial-3shields-3windows` | 7 | 최윤식 박사 『미래준비학교』(2016) + 『부의 정석』(2011)의 3개의 방패와 3개의 창 재정 전략 모델을 그대로 구현한… |
| Prescription | `vision-clarity-coaching` | 5 | 비전이 막연하거나 막힌 사용자가 비전의 핵심을 한 문장으로 끄집어내도록 돕는 1:1 깊이 코칭 스킬. 소크라테스 산파술(mai… |
| Prescription | `vision-career-recommendation` | 7 | 사용자의 가치 단어·관심사·심리검사 결과(에니어그램·MBTI·다중지능·STRONG/RIASEC) + 나이·학력을 종합하여 적합… |
| Prescription | `vision-financial-coach` | 7 | Dave Ramsey(『The Total Money Makeover』·7 Baby Steps·스노우볼 방식)와 Suze Orm… |
| Prescription | `vision-goal-reframing` | 7 | 사용자의 영감·꿈·소망을 측정 가능한 현실 목표로 변환하는 워크북 스킬. 명료해진 비전 한 문장(vision-clarity-c… |
| Prescription | `vision-strategy-coach` | 7 | 사용자의 비전(Vision)을 구체적·단계별 행동(Action)으로 변환하는 통합 전략 코칭 스킬. 전략 계획·코칭 실무에서… |
| Prescription | `vision-follow-through-habits` | 8 | 결심·계획이 습관·일상 시스템으로 정착하도록 설계하는 실행 지속력 코칭 스킬. BJ Fogg(Tiny Habits, 2019)… |
| Prescription | `vision-progress-review` | 8 | 사용자의 비전·목표·행동 계획 진척을 주간·월간·분기·연간 4단위 정기 점검으로 추적·평가·재조정하는 진척 추적 스킬. 결정론… |
| Meta-Interview | `vision-grill-with-docs` | — | 미래비전코칭의 모든 단계에서 사용자가 난관에 부딪히거나 생각이 정리되지 않을 때 호출하는 다목적 인터뷰 엔진 스킬. Matt… |
| Data Backbone | `vision-school-major-info` | 1·3·7 | 한국 대학·학과·진로 정보(공공데이터포털 7개 API 통합)와 미국 직업 정보(ONET)를 결정론적으로 조회·매핑·진로 추천에… |
<!-- /AUTO:SKILL_INDEX -->

### 🔗 박사님 8단계 ↔ 스킬 흐름도 / 8-Stage Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│ 1단계 — Vision Coding (내 안에 있는 것 파악)                    │
│   ┌──────────────────────────────────┐                          │
│   │ vision-cys-competence-visioncoding │ ★ 핵심                 │
│   └────┬─────────────────────────────┘                          │
│        │  ┌────────┐ ┌────────────┐ ┌──────────┐                │
│        ├→│ mbti   │ │ enneagram  │ │ strong   │                │
│        │  └────────┘ └────────────┘ └──────────┘                │
│        │  ┌────────────┐ ┌────────┐ ┌──────────┐                │
│        ├→│multipleintel│ │ values │ │ readiness│                │
│        └→└────────────┘ └────────┘ └──────────┘                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2단계 — 나와 연관된 미래 예측 (4스킬 순차 흐름)                 │
│                                                                 │
│ ① ┌────────────────────────────────┐                            │
│   │ vision-personal-future-research │ ★ 시작점                  │
│   │ 진단 7종 → 맞춤 미래 매트릭스   │                            │
│   └─────────────┬──────────────────┘                            │
│                 ↓                                               │
│ ② ┌────────────────────────────────┐                            │
│   │ foresight-futures-wheel        │ (외부 시리즈)              │
│   │ 핵심 변화 → 1차→고차 영향      │                            │
│   └─────────────┬──────────────────┘                            │
│                 ↓                                               │
│ ③ ┌────────────────────────────────┐                            │
│   │ vision-four-futures            │                           │
│   │ Plausible/Possible/Wildcard/   │                           │
│   │ Normative 4가지 미래            │                           │
│   └─────────────┬──────────────────┘                            │
│                 ↓                                               │
│ ④ ┌────────────────────────────────┐                            │
│   │ vision-futures-timeline-map    │ ★ 완성                    │
│   │ 시간축 미래지도                │                           │
│   └────────────────────────────────┘                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 3단계 — 5가지 시대적 필요 발견 (문제·욕구·결핍·위기·기회)       │
│   ┌──────────────────────────────┐                              │
│   │ vision-future-needs-prediction │ ★ 5필요 분해              │
│   └──────────────────────────────┘                              │
│   ┌────────────────────────────────────┐                        │
│   │ vision-future-promise-five-criteria │ 후보 평가             │
│   └────────────────────────────────────┘                        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 4단계 — 마음을 사로잡는 가치 명확화 + 비전 열매 예상             │
│   ┌────────────────────────────┐  ┌──────────────────────────┐  │
│   │ vision-values-visioncoding │  │ vision-three-realm-balance│  │
│   │ 가치 단어 매핑              │  │ 3겹 교집합 점검           │  │
│   └────────────────────────────┘  └──────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 5단계 — "가치 + 시대적 필요 + 내 능력" 종합 → 비전 큰 그림      │
│   ┌──────────────────┐  ┌──────────────────────┐                │
│   │ vision-clarity-  │  │ vision-mission-frame │                │
│   │ coaching         │  │ ★ 비전 프레임         │                │
│   │ 한 문장 명료화   │  │                      │                │
│   └──────────────────┘  └──────────────────────┘                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 6단계 — 비전선언문 작성                                          │
│   ┌────────────────────────────┐                                │
│   │ vision-statement-writer    │ ★ 박사님 11빈칸 양식           │
│   └────────────────────────────┘                                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 7단계 — 비전 성취 구체 설계 (목표·전략·필요한 것)               │
│   ┌──────────────────┐  ┌──────────────────────┐                │
│   │ vision-goal-     │  │ vision-strategy-     │                │
│   │ reframing        │  │ coach                │                │
│   │ SMART+OKR        │  │ 일반 5단계            │                │
│   └──────────────────┘  └──────────────────────┘                │
│   ┌─────────────────────────────────┐  ┌──────────────────────┐ │
│   │ vision-financial-3shields-3windows│  │ vision-financial-   │ │
│   │ ★ 박사님 재정 모델               │  │ coach (Ramsey/Orman)│ │
│   └─────────────────────────────────┘  └──────────────────────┘ │
│   ┌─────────────────────────────────┐                           │
│   │ vision-career-recommendation    │ 직업·진로                 │
│   └─────────────────────────────────┘                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 8단계 — 미래비전 지속 셀프코칭                                   │
│  (자극·디자인·심층탐구·훈련·네트워킹·재생산)                     │
│   ┌─────────────────────┐  ┌──────────────────────────┐         │
│   │ vision-five-stages  │  │ vision-smart-five-       │         │
│   │ ★ 박사님 5단계 척추 │  │ competence ★ SMART 5역량 │         │
│   └─────────────────────┘  └──────────────────────────┘         │
│   ┌──────────────────────────────────┐  ┌────────────────────┐  │
│   │ vision-eight-training-areas      │  │ vision-follow-     │  │
│   │ ★ 8대 훈련 영역                  │  │ through-habits     │  │
│   └──────────────────────────────────┘  └────────────────────┘  │
│   ┌──────────────────────────┐                                  │
│   │ vision-progress-review   │ 4단위 점검 사이클               │
│   └──────────────────────────┘                                  │
└─────────────────────────────────────────────────────────────────┘

▲ 위 8단계 어느 위치에서든 사용자가 막히거나 생각이 정리되지 않을 때 ▲
┌─────────────────────────────────────────────────────────────────┐
│ ✦ Cross-stage 메타 인터뷰 (Meta-Interview)                       │
│   ┌────────────────────────────────────────────────┐            │
│   │ vision-grill-with-docs ★ 다목적 인터뷰 엔진     │            │
│   │ - Mode A: 비전 grill (1:1)                      │            │
│   │ - Mode B: 다른 vision 산출물 메타 검증          │            │
│   │ - Mode C: 자유 주제 (진로·재정·관계·사역·결단)  │            │
│   │ + LDR (Life Decision Record) — 인생 결정 기록기 │            │
│   └────────────────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────────────┘

▲ 1·3·7단계에서 실제 학과·학교·직업 데이터가 필요할 때 ▲
┌─────────────────────────────────────────────────────────────────┐
│ ✦ Data Backbone — 외부 API 통합                                  │
│   ┌─────────────────────────────────────────────────┐           │
│   │ vision-school-major-info ★ 데이터 백본           │           │
│   │ - 공공데이터포털 1개 키로 7개 API (커리어넷+KCUE) │           │
│   │ - ONET Web Services (선택·유학 진로용)            │           │
│   │ - Holland → ONET 자동 매핑                       │           │
│   │ - 한↔영 학과명 매핑 사전 + CC-BY attribution     │           │
│   │ - 사용자 본인 키, ~/.config (chmod 600)          │           │
│   └─────────────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

---

### 🎯 사용자 유형별 *최소 패키지* / Minimal Package by User Type

28개 전체를 다 쓸 필요는 없습니다. 본인 상황에 맞는 *최소 패키지*만 따라가도 박사님 비전 발견·완수 흐름이 작동합니다. 진행 중 막히면 언제든지 `/vision-grill-with-docs <주제>`로 메타 인터뷰를 호출하고, 학과·학교·직업 데이터가 필요하면 `/vision-school-major-info`로 한국·미국 데이터를 조회하세요.

#### 🧑‍🎓 청년 (Young Adult) — 8단계 압축 패키지
1. **1단계** — `vision-cys-competence-visioncoding`
2. **2단계** — `vision-personal-future-research` → `foresight-futures-wheel` → `vision-four-futures`
3. **3단계** — `vision-future-needs-prediction`
4. **4단계** — `vision-three-realm-balance`
5. **5단계** — `vision-mission-frame`
6. **6단계** — `vision-statement-writer`
7. **7단계** — `vision-goal-reframing`
8. **8단계** — `vision-smart-five-competence` (요약)

#### 👨‍💼 중년 (Mid-Life) — 직업 전환 패키지
1. **1단계** — 진단 6종 (cys + mbti + enneagram + strong + multipleintel + values)
2. **2단계** — `vision-personal-future-research` → `vision-four-futures` → `vision-futures-timeline-map`
3. **3단계** — `vision-future-promise-five-criteria`
4. **6단계** — `vision-statement-writer`
5. **7단계** — `vision-financial-3shields-3windows` + `vision-career-recommendation`

#### 👴 은퇴기 (Retirement) — 사역 발견 패키지
1. **1단계** — `vision-cys-competence-visioncoding`
2. **4단계** — `vision-three-realm-balance` + `vision-values-visioncoding`
3. **5단계** — `vision-mission-frame`
4. **6단계** — `vision-statement-writer`
5. **8단계** — `vision-five-stages` Stage 5 (비전 재생산)

#### 🏫 고등학생 (High School) — 진로 입문 패키지
1. **1단계** — `vision-multipleintel-visioncoding` + `vision-mbti-visioncoding` + `vision-strong-visioncoding`
2. **3단계** — `vision-future-promise-five-criteria`
3. **7단계** — `vision-career-recommendation`

#### ⛪ 교회 청년부 (Church Youth) — 1년 커리큘럼
박사님 8단계 흐름 그대로 — 28개 스킬 전체 활용 (월 1회 셀모임 × 12회 = 8단계 + 종합 정리 + 비전 재생산). 셀원이 막힐 때마다 `/vision-grill-with-docs`로 1:1 grill 인터뷰, 학과·학교 정보가 필요하면 `/vision-school-major-info`.

---

### Vision Coding - 진단 7종 / Diagnosis (7)
박사님 8단계 *1단계 — 내 안에 있는 것 파악*

| 스킬 / Skill | 측정 / Measures |
|------------|---------------|
| `vision-cys-competence-visioncoding` | CYS 10 비전 코드 (박사님 직접 개발) |
| `vision-mbti-visioncoding` | MBTI 16유형 |
| `vision-enneagram-visioncoding` | 에니어그램 9유형 |
| `vision-strong-visioncoding` | STRONG/RIASEC 직업 흥미 |
| `vision-multipleintel-visioncoding` | 다중지능 9지능 |
| `vision-values-visioncoding` | 가치 매핑 (3프레임워크 통합) — 4단계에서도 사용 |
| `vision-readiness-visioncoding` | 꿈 달성 4능력 |

#### 진단 7종 상세 / Diagnosis Details

##### 1.1 vision-cys-competence-visioncoding ★ 핵심
- **이름**: CYS 비전 역량 진단
- **측정**: 박사님 직접 개발 *200여 문항* 평가 — 10개 비전 코드
  - 비전 방향성·가치 방향·잠재력·기술력·구상력·자기계발력·전략력·추진력·네트워킹력·리더십 스타일
- **통합**: 미래학 + MBTI + STRONG + 에니어그램 + 다중지능
- **재실시**: 1년 1회 권장 (박사님 책)

##### 1.2 vision-mbti-visioncoding
- **측정**: MBTI 16유형 (E/I·S/N·T/F·J/P 4축 × 5문항 = 20문항)
- **박사님 활용**: CYS의 *비전 잠재력(성격)* 영역

##### 1.3 vision-enneagram-visioncoding
- **측정**: 에니어그램 9유형 (Core Desire + Core Fear)
- **문항**: 27문항 (각 유형 3문항·무작위·3문항씩 출제)
- **윙(Wing)**: 인접 두 유형 중 점수 높은 쪽
- **박사님 활용**: CYS의 *비전 잠재력(성격)* 영역

##### 1.4 vision-strong-visioncoding
- **측정**: STRONG 직업흥미도 / Holland RIASEC 6유형
- **문항**: 18문항 (각 영역 3문항)
- **출제**: 3문항씩 6라운드
- **박사님 활용**: CYS의 *비전 기술력(관심사 검사)* 영역

##### 1.5 vision-multipleintel-visioncoding
- **측정**: Howard Gardner 다중지능 9가지 (1983 + 1995 자연친화 + Existential 잠정)
- **문항**: 27문항 (각 지능 3문항)
- **상위 4개**: 우세 지능 식별
- **박사님 활용**: CYS의 *비전 잠재력(재능 — 다중지능)* 영역

##### 1.6 vision-values-visioncoding
- **측정**: MBTI + 에니어그램 + 다중지능 결과 → 가치 단어 매핑
- **9유형 추구 세상** 명시 (박사님 책 인용 그대로)
- **박사님 활용**: CYS의 *비전 가치 방향* 영역 — *4단계*에서도 가치 명확화 도구로 재사용

##### 1.7 vision-readiness-visioncoding
- **측정**: 꿈 달성 4능력 (Big Picture·Reframing·Strategy·Follow-Through)
- **문항**: 20문항 (각 능력 5문항)
- **시각화**: 영어 축 막대 그래프
- **박사님 활용**: 보조 진단

### 박사님 책 토대 — 척추 도식 (5)
박사님 미래준비학교 *고유 프레임* — 8단계 전반에 걸쳐 활용

| 스킬 / Skill | 박사님 고유 모델 | 주 활용 단계 |
|------------|---------------|------|
| `vision-five-stages` | 비전 5단계 (스케치→디자인→훈련→재인식→재생산) | 8단계 (지속 셀프코칭) |
| `vision-mission-frame` | 비전 프레임 (영적 직관력+이성적 판단력+R) | 5단계 (큰 그림) |
| `vision-statement-writer` | 비전 선언문 양식 그대로 | 6단계 (선언문) |
| `vision-smart-five-competence` | SMART 5역량 (S·M·A·R·T) | 8단계 (훈련) |
| `vision-eight-training-areas` | 비전 훈련 8대 영역 | 8단계 (훈련) |

#### 척추 도식 5종 상세 / Spine Details

##### 2.1 vision-five-stages ★★ 최핵심
- **박사님 비전 5단계**:
  - Stage 1 **비전 스케치** (자기 인식)
  - Stage 2 **비전 디자인** (비전 발견)
  - Stage 3 **비전 훈련** (SMART 5역량)
  - Stage 4 **비전 재인식**
  - Stage 5 **비전 재생산** — 최고 경지
- **8단계 매칭**: *8단계 (지속 셀프코칭)* — 자극·디자인·심층탐구·훈련·재생산 사이클의 척추
- **차별점**: 일반 5단계 (vision-strategy-coach)와 *완전 다른* 박사님 정통

##### 2.2 vision-mission-frame ★ 핵심
- **비전 프레임 도식**:
  ```
  영감 + 정신적 가치    → 영적 직관력
        ↑↓ (R)
  정보 + 예측 구성      → 미래 변화 통찰
  ```
- **비전 정의 직결**: "가치 있는"·"시대적"·"소명" 매핑
- **8단계 매칭**: *5단계 (큰 그림)* — 비전 출발점을 비전 프레임으로 정밀화

##### 2.3 vision-statement-writer ★ 실행
- **양식 구성**: 11개 빈칸 (이름·3가지 미래·문제/욕구/결핍·관심·재능·성격·일·가치·Purposes 5개)
- **선행 권장**: 비전 디자인 완료 후 작성
- **8단계 매칭**: *6단계 (비전선언문)*

##### 2.4 vision-smart-five-competence ★ 훈련
- **SMART 5역량**:
  - **S**ense (직관적·훈련된 통찰력)
  - **M**ethod (통합·분석 사고 + 체계 업무)
  - **A**rt (장인 지식·예술적 상상력)
  - **R**elationship (집단지성·인격)
  - **T**echnology (기술지능)
- **OECD DeSeCo 대응**: 1997~2003 OECD 12개국 핵심역량과 정확히 매핑
- **8단계 매칭**: *8단계 (훈련)*

##### 2.5 vision-eight-training-areas ★ 습관
- **8대 영역**:
  1. 균형 잡힌 영성
  2. 건강한 사고
  3. 좋은 언어
  4. 좋은 관계
  5. 효과적 학습
  6. 효율적 실행
  7. 지혜로운 재정 전략
  8. 건강한 신체
- **8단계 매칭**: *8단계 (훈련)*

### 박사님 책 토대 — 살·근육 (7)
박사님 책의 *세부 도구* + 박사님 미래학 *응용 도구* — 8단계 전반에 걸쳐 활용

| 스킬 / Skill | 박사님 고유 모델 / 응용 | 주 활용 단계 |
|------------|---------------|------|
| `vision-financial-3shields-3windows` | 재정 3방패+3창 | 7단계 (구체 설계) |
| `vision-personal-future-research` | 진단 7종 → 개인 맞춤 미래 변화 매트릭스 (응용) | 2단계 (미래 예측 — *시작점*) |
| `vision-futures-timeline-map` | 미래지도 작성 4가지 고려 | 2단계 (미래 예측 — *완성*) |
| `vision-four-futures` | 4가지 미래 (Plausible/Possible/Wildcard/Normative) | 2단계 (미래 예측) |
| `vision-future-promise-five-criteria` | 미래 유망성 5기준 | 3단계 (시대적 필요) |
| `vision-three-realm-balance` | 비전 영역 3겹 (개인/가족·세상/정신적) | 4단계 (가치·열매) |
| `vision-future-needs-prediction` | 미래 필요 3축 분해 | 3단계 (시대적 필요) |

#### 살·근육 + 응용 7종 상세 / Flesh + Applied Details

##### 3.0 vision-personal-future-research ★ 2단계 시작점 (응용)
- **위치**: 박사님 8단계 *2단계 (나와 연관된 미래 예측)의 시작점*
- **입력**: Vision Coding 진단 7종 결과 (CYS·MBTI·에니어그램·STRONG·다중지능·가치·준비도)
- **처리**:
  - 다중지능 → 산업·기술 영역 가중치
  - STRONG/RIASEC → 직업·환경 가중치
  - 가치 단어 → 영성·정치·사회 가중치
  - MBTI/에니어그램 → 변화 대응 스타일 가중치
  - CYS 비전 코드 → 종합 가중치
- **산출**: STEEPS 6영역 × 시간축 3구간(단·중·장기) 매트릭스 + 우선순위 상위 10~15개 *변화 카드*
- **다음 흐름**: foresight-futures-wheel → vision-four-futures → vision-futures-timeline-map
- **차별점**: 일반 미래 보고서가 아닌 *그 사용자 진단 결과 가중치*가 적용된 개인 맞춤 미래 리포트

##### 3.1 vision-financial-3shields-3windows
- **3개의 방패** (자산 보존): 금융·투자·소비 자산 리모델링
- **3개의 창** (자산 증식): 소득·투자·꿈 효과
- **차별점**: vision-financial-coach (Ramsey/Orman)와 *완전히 다른* 박사님 고유 모델
- **8단계 매칭**: *7단계 (구체 설계 — 재정)*

##### 3.2 vision-futures-timeline-map
- **콜럼버스 비유**: 정밀 지도 X, 방향 지도 O
- **4가지 고려사항**: 직면 상황·필요할 것·보잘것없는 정보·뜻밖의 미래
- **6힘 영역**: STEEPS 박사님판 (사회·기술·경제·환경·정치·영성)
- **8단계 매칭**: *2단계 (미래 예측)*

##### 3.3 vision-four-futures
- **4가지 미래**:
  - **Plausible** (기본미래·51~80%)
  - **Possible** (가능 미래들)
  - **Wildcard** (뜻밖의 미래 — 비약적 진보 + 붕괴)
  - **Normative/Preferred** (바람직한 미래)
- **비전 가능성 영역 3~4개** 도출
- **8단계 매칭**: *2단계 (미래 예측)*

##### 3.4 vision-future-promise-five-criteria
- **미래 유망성 5기준**:
  1. 가치 있는 영향력 (지배력 ≠ 영향력)
  2. 행복성 (비전 ↔ 행복 = 동전 앞뒷면)
  3. (적절한) 부의 가능성
  4. 지속가능성
  5. 경쟁력 (10:1 vs 100:1)
- **8단계 매칭**: *3단계 (시대적 필요 영역 평가)*

##### 3.5 vision-three-realm-balance
- **3겹 다이어그램**:
  - 나만 → 개인 욕망
  - 가족·세상만 → 자기희생
  - 정신적으로만 → 왜곡된 사명
  - **교집합 = 진정한 비전 영역**
- **8단계 매칭**: *4단계 (가치·열매 예상)* — 비전 열매가 3겹 교집합에 위치하는지 점검

##### 3.6 vision-future-needs-prediction
- **3축 분해**: 기회/도전 · 필요/결핍 · 해결/신규 문제
- **STEEPS** + 미래 형상 3요소
- **8단계 매칭**: *3단계 (시대적 필요 발견)* — 미래 변화에서 5가지 필요(문제·욕구·결핍·위기·기회) 도출

### 2단계 미래 예측 — 박사님 권장 순차 흐름

박사님이 직접 정리하신 2단계 *4스킬 순차 사용*:

```
[1단계 진단 7종 결과 입력]
     ↓
① vision-personal-future-research
   → 진단 7종 결과로 *나와 연관된* 미래 변화 매트릭스 추출
     ↓
② foresight-futures-wheel
   → 핵심 변화 1~2개로 1차→2차→3차→4차→고차 영향 추론
     ↓
③ vision-four-futures
   → Plausible/Possible/Wildcard/Normative 4가지 미래 가능성 분류
     ↓
④ vision-futures-timeline-map
   → 단기·중기·장기 시간축 미래지도 *완성*
     ↓
[3단계로 — 5가지 시대적 필요 발견]
```

### 처방·실행 (7)
일반 코칭 도구 — 7~8단계에 활용

| 스킬 / Skill | 도구 | 주 활용 단계 |
|------------|------|------|
| `vision-strategy-coach` | 일반 5단계 (비전핵심→장기→단기→행동→측정) | 7단계 (구체 설계) |
| `vision-career-recommendation` | 4유형 직업 추천 (미래·재미·봉사·고소득 각 5개) | 7단계 (구체 설계) |
| `vision-clarity-coaching` | 소크라테스 산파술 비전 명료화 | 5단계 (큰 그림) |
| `vision-goal-reframing` | SMART + Backcasting + OKR | 7단계 (구체 설계) |
| `vision-financial-coach` | Dave Ramsey + Suze Orman 재정 | 7단계 (구체 설계) |
| `vision-follow-through-habits` | BJ Fogg + James Clear + Charles Duhigg 습관 | 8단계 (지속) |
| `vision-progress-review` | 주간·월간·분기·연간 4단위 점검 | 8단계 (지속) |

#### 처방·실행 7종 상세 / Prescription Details

##### 4.1 vision-strategy-coach
- **5단계** (일반): 비전핵심 → 장기 → 단기 → 행동 → 측정
- **박사님 책의 *5단계 (vision-five-stages)*와 별개**
- **8단계 매칭**: *7단계 (구체 설계 — 전략)*

##### 4.2 vision-career-recommendation
- **4유형 직업 추천 × 5개 = 20개**:
  1. 미래 직업 (Future Jobs)
  2. 행복·재미 (Happy & Fun)
  3. 은퇴 후 봉사 (Retirement Volunteering)
  4. 현재 고소득 (High-Pay Current)
- **나이·학력 우선 필터**
- **8단계 매칭**: *7단계 (구체 설계 — 직업·진로)*

##### 4.3 vision-clarity-coaching
- **소크라테스 산파술** (maieutics) 비전 명료화
- **5단계**: 표면 vs 본질·살아있음·5년 후 장면·후회 1순위·한 문장 산출
- **8단계 매칭**: *5단계 (큰 그림)* — 가치+시대적 필요+능력 종합을 한 문장으로

##### 4.4 vision-goal-reframing
- **3 프레임 결합**: SMART + Backcasting + OKR
- **5단계**: 영감 청취·SMART 검증·Backcasting·OKR·첫 한 걸음
- **8단계 매칭**: *7단계 (구체 설계 — 목표)*

##### 4.5 vision-financial-coach
- **Dave Ramsey** (7 Baby Steps·스노우볼) + **Suze Orman** (8개월 응급자금)
- **6단계 분석 + 5단계 목표 시퀀스**
- **차별점**: vision-financial-3shields-3windows (박사님 모델)와 별개
- **8단계 매칭**: *7단계 (구체 설계 — 재정 보조)*

##### 4.6 vision-follow-through-habits
- **3대 습관 과학**: BJ Fogg + James Clear + Charles Duhigg
- **5단계**: 행동 분해·트리거·Tiny·보상·추적
- **한국 작심삼일 패턴 대응**
- **8단계 매칭**: *8단계 (지속 — 습관)*

##### 4.7 vision-progress-review
- **4단위 점검**: 주간(30분)·월간(1시간)·분기(2시간)·연간(반나절)
- **빗나감 정상화** — 학습 신호로
- **8단계 매칭**: *8단계 (지속 — 점검 사이클)*

### 메타 인터뷰 / Meta-Interview (1)
박사님 8단계 *전 단계 어디서든 호출 가능한 Cross-stage 도구*. Matt Pocock의 grill-with-docs 패턴을 미래비전코칭 맥락으로 전면 커스터마이즈.

| 스킬 / Skill | 박사님 고유 모델 / 응용 | 주 활용 단계 |
|------------|---------------|------|
| `vision-grill-with-docs` | 3-모드 인터뷰 엔진 + LDR(Life Decision Record) + 박사님 표준 사전 충돌 검출 + 결정론 21함수 | 전 단계 (Cross-stage) |

#### 메타 인터뷰 상세 / Meta-Interview Detail

##### 5.1 vision-grill-with-docs ✦ Cross-stage
- **3 작동 모드**:
  - **Mode A** — 비전 grill (1:1 인터뷰): 본인·코칭 대상자의 비전 전반을 박사님 표준 사전 기준으로 grill
  - **Mode B** — 산출물 메타 검증: 다른 vision 스킬(mission-frame·three-realm·five-stages 등) 결과물의 자기모순·박사님 사전 위반 검출
  - **Mode C** — 다목적 자유 주제: 진로·전공·학교 / 재정 큰 결정 / 사역 결단 / 결혼·관계 / 비전이 막혔을 때 등 *임의 주제* 인터뷰
- **5가지 grill 액션**:
  ① 박사님 표준 사전 충돌 즉시 지적 (꿈/야망/트렌드 → 비전/시대 통일 권고)
  ② 모호한 비전 언어 정밀화 (성공 → 4 Skill Balance 어느 축?)
  ③ 시나리오 4종 강제 확장 (5년·10년·실패·기회비용)
  ④ 기존 vision 스킬 산출물 cross-reference
  ⑤ 결정 즉시 inline 기록 (VISION-CONTEXT.md·docs/ldr/)
- **LDR (Life Decision Record)** — 원본 ADR을 인생 결정 기록기로 매핑. 3조건(번복 어려움·미래 의문·진짜 trade-off) 모두 충족 시에만 발행 → "기록을 위한 기록" 차단
- **3겹 사전 구조**: 박사님 표준 사전(1순위) + 도메인 영역별 sub-context(2순위) + 학술 fallback(3순위)
- **결정론 모듈** `grill_lib.py` 21개 함수 — 모드 분기·주제 파싱·박사님 사전 충돌·인용 위조 차단·LDR 자격·sync 검증을 LLM 자연어 추론 없이 처리
- **검증 211/211 PASS** — 단위 130 + 기존 라운드 48 + 신규 10시나리오 33
- **8단계 매칭**: *전 단계* — 어떤 단계에서든 막히면 호출

---

### 🔧 외부 시리즈 연계 / External Series Integration

본 패키지는 박사님의 다른 시리즈와 연계 가능:

#### foresight-* 시리즈 (미래 예측)
- `foresight-futures-wheel` — 박사님 8단계 *2단계 (미래 예측)*의 ② 위치, 핵심 변화의 1차→고차 영향 추론에 사용
- `foresight-socratic-critical-thinking` — 비전 비판적 검증 시 활용

#### sermon-* 시리즈 (설교 — 박사님 담임목사 활용)
- 본 vision-* 시리즈와 별도 시리즈
- 교회 사역 시 함께 사용 가능 (vision으로 비전 발견 → sermon으로 회중 전달)

---

### 🆕 박사님 명명 규칙 / Naming Convention

| 패턴 | 적용 |
|------|------|
| `*-visioncoding` | **검사 계열** — readiness·mbti·enneagram·strong·multipleintel·values·cys-competence (7개) |
| 자유 명명 | **처방·코칭·훈련 계열** — 19개 |
| `*-grill-with-docs` | **메타 인터뷰 계열** — 1개 (cross-stage 도구) |
| `*-school-major-info` | **데이터 백본 계열** — 1개 (외부 API 통합 — data.go.kr + ONET) |

박사님 메모리 [Vision visioncoding 명명 원칙] 참조.

---

## 🧭 박사님 비전 철학 / Dr. Choi's Vision Philosophy

박사님 비전 정의: **비전 = 가치 있는 시대적 소명**

### 비전 5대 공리
1. 당신은 *유일하고 고귀하고 특별*하다
2. 비전은 *모든 사람*이 가질 수 있다
3. 비전은 *개별적*이다, 그래서 *시대적*이다
4. 누구에게나 *비전을 이룰 역량*이 있거나 마련할 수 있다
5. 모든 비전은 *나·가족·이웃·인류*에게 가치 있는 것으로 귀결되어야 한다

### 3가지 비전 질문
1. 내가 *기뻐할 수 있는 가치*가 무엇인가?
2. 내가 *살아갈 시대 모습*은 무엇인가?
3. 내가 *기쁘게 헌신할 수 있는 구체적 일(소명)*은 무엇인가?

### 6대 행동 강령
- 서두르지 마라 (**Take a Time**)
- 멀리 보라 (**Foresee Futures**)
- 비전을 품어라 (**Make a Vision**)
- 계획을 짜라 (**Make a Plan**)
- 어떻게 일할지 훈련하고 생각하라 (**Train and Think about How To Work**)
- 작은 일을 소중하게 하라 (**Be Faithful with a Few Things**)

자세한 철학은 [PHILOSOPHY.md](docs/PHILOSOPHY.md) 참조.

---

## 🔧 새 스킬 추가 / Adding New Skills

박사님이 새 스킬을 만드시면 다음 절차를 따르세요:

```bash
# 1) 새 스킬 폴더 + SKILL.md 작성
#    frontmatter에 다음 두 줄을 권장 (자동 분류용)
#    category: diagnosis | spine | flesh | prescription
#    stage: 1   (또는 1,4 등 콤마 구분)

# 2) Claude Code에 등록
ln -sf "$(pwd)/skills/<new-name>" ~/.claude/skills/<new-name>

# 3) 카탈로그 자동 갱신
python3 _build_catalog.py

# (선택) 변경 필요 여부만 검증
python3 _build_catalog.py --check
```

빌드 스크립트가 자동 갱신하는 영역:
- `README.md` — 배지 (`Skills: NN`)
- `docs/SKILL_CATALOG.md` — 제목 카운트, 4대 카테고리 합계, 전체 스킬 인덱스 표

**자동 갱신 *대상 외*** (직접 편집):
- 8단계 매핑 표 (순서가 의미를 가짐)
- 카테고리별 상세 설명 카드
- 8단계 흐름 다이어그램·사용자 유형별 패키지

frontmatter에 `category`/`stage`가 없으면 `_build_catalog.py`의 `DEFAULT_META`에서 보충합니다. 신규 스킬을 카탈로그에 자동 분류시키려면 frontmatter에 직접 적거나 `DEFAULT_META`에 한 줄 추가하면 됩니다.

---

## 📂 폴더 구조 / Folder Structure

```
cys-claude-vision-coaching-skills/
├── README.md # 본 문서
├── LICENSE # CC BY-NC-SA 4.0
├── _build_catalog.py # 카탈로그 자동 빌드 스크립트
├── docs/
│ ├── PHILOSOPHY.md # 박사님 비전 철학
│ ├── SKILL_CATALOG.md # 26개 스킬 카탈로그 (8단계 흐름)
│ ├── INSTALLATION.md # 설치 가이드
│ ├── BOOK_MAPPING.md # 책 ↔ 스킬 매핑 (Phase 2)
│ ├── EIGHT_STAGE_GUIDE.md # 8단계 상세 가이드 (Phase 2)
│ ├── USAGE_PATHS.md # 사용자 유형별 경로 (Phase 2)
│ ├── WORKFLOWS.md # 통합 워크플로우 (Phase 2)
│ ├── GLOSSARY.md # 용어집 (Phase 3)
│ └── CONTRIBUTING.md # 기여 가이드 (Phase 3)
├── skills/ # 26개 Claude Code 스킬
│ ├── vision-cys-competence-visioncoding/
│ ├── vision-five-stages/
│ ├── vision-mission-frame/
│ ├── ... (26개)
│ └── vision-progress-review/
└── examples/ # 시나리오 예시 (Phase 3)
```

---

## 📖 박사님 원서 / Original Book

본 패키지의 모든 토대는 다음 책에 있습니다. 깊이 있는 학습을 위해 반드시 *원서를 함께* 읽으시기를 권장합니다.

This package is rooted in the following book. For deep learning, *please read the original book*.

> **최윤식·최현식, 『최윤식의 미래준비학교 — 흔들림 없는 인생을 계획하는 5단계』, 지식노마드, 2016. (ISBN 978-89-93322-97-2)**

---

## 🤝 기여 / Contributing

본 패키지는 박사님 *비전 재생산* 정신을 따라 *공동체적*으로 발전합니다. 피드백·번역·확장 모두 환영합니다.

This package grows *as a community* in the spirit of Dr. Choi's *vision reproduction*. Feedback, translations, and extensions are all welcome.

자세한 내용은 [CONTRIBUTING.md](docs/CONTRIBUTING.md) (Phase 3 작성 예정) 참조.

---

## 📜 라이선스 / License

본 패키지는 [CC BY-NC-SA 4.0](LICENSE) 라이선스로 제공됩니다 (비상업·저작자표시·동일조건변경허락).

This package is licensed under [CC BY-NC-SA 4.0](LICENSE) (NonCommercial-Attribution-ShareAlike).

상업적 활용 문의 / Commercial use inquiry: **cysinsight@gmail.com**

---

## 🙏 비전 / Vision

박사님 책 인용:
> *"그 어떤 사람들도 비전 재생산의 대상이 될 수 있다."*

이 패키지를 통해 한 사람이라도 더 *자신의 비전을 발견하고 완수하는 인생*을 산다면, 박사님의 *비전 재생산*이 디지털·글로벌 차원에서 살아 있는 것입니다.

If even one more person *discovers and fulfills their vision* through this package, Dr. Choi's *Vision Reproduction* lives on at a digital and global scale.

---

**Made with ❤️ following Dr. Choi Yoon-Sik's Future Preparation School**

*비전, 그 깊은 데로 가라. 비전, 그 행복으로 가라.*
*— 최윤식 박사, 『미래준비학교』*
