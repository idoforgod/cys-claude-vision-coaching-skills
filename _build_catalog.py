#!/usr/bin/env python3
"""
_build_catalog.py — CYS Vision Coaching Skills 카탈로그 자동 빌드

skills/*/SKILL.md frontmatter를 스캔하여 README.md와 docs/SKILL_CATALOG.md의
마커 사이 영역을 자동 재생성한다.

사용법:
    python3 _build_catalog.py            # 빌드 실행 (파일 갱신)
    python3 _build_catalog.py --check    # 검증만 (변경 필요 시 exit 1)

마커 형식:
    <!-- AUTO:BLOCK_NAME -->
    ...auto-generated...
    <!-- /AUTO:BLOCK_NAME -->

자동 갱신 블록:
    README.md          : BADGE, CATEGORY_TABLE, SKILL_INDEX
    SKILL_CATALOG.md   : TITLE_COUNT, CATEGORY_TABLE, SKILL_INDEX
    (STAGE_MAPPING은 박사님이 직접 관리하는 *순서가 의미를 가지는 표* — 자동 갱신 제외)

새 스킬 추가 절차:
    1) skills/<name>/SKILL.md 작성
       - frontmatter에 category(diagnosis|spine|flesh|prescription)와
         stage(콤마 구분 1~8) 명시 권장
    2) ~/.claude/skills/<name> 심볼릭 링크 생성
    3) python3 _build_catalog.py 실행

frontmatter에 category/stage 없을 시 본 스크립트 DEFAULT_META에서 보충한다.
DEFAULT_META에도 없으면 'uncategorized'로 분류되며 경고가 표시된다.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
CATALOG = ROOT / "docs" / "SKILL_CATALOG.md"

CATEGORIES = {
    "diagnosis": {
        "label_ko": "Vision Coding - 진단",
        "label_en": "Diagnosis",
        "stages_ko": "1단계",
        "order": 1,
    },
    "spine": {
        "label_ko": "박사님 책 토대 — 척추 도식",
        "label_en": "Spine",
        "stages_ko": "5·6·8단계",
        "order": 2,
    },
    "flesh": {
        "label_ko": "박사님 책 토대 — 살·근육 + 응용",
        "label_en": "Flesh + Applied",
        "stages_ko": "2·3·4·7단계",
        "order": 3,
    },
    "prescription": {
        "label_ko": "처방·실행",
        "label_en": "Prescription",
        "stages_ko": "5·7·8단계",
        "order": 4,
    },
}

STAGE_TITLES = {
    1: "Vision Coding — 내 안에 있는 것 파악",
    2: "나와 연관된 미래 예측",
    3: "5가지 시대적 필요(문제·욕구·결핍·위기·기회) 발견",
    4: "마음을 사로잡는 가치 명확화 + 비전 열매",
    5: "비전 출발점·큰 그림",
    6: "비전선언문 작성",
    7: "비전 성취 구체 설계 (목표·전략·필요한 것)",
    8: "미래비전 지속 셀프코칭",
}

# 기존 26개 스킬 기본 분류. 새 스킬은 SKILL.md frontmatter에 category/stage를 적으면 됨.
DEFAULT_META = {
    "vision-cys-competence-visioncoding": ("diagnosis", [1]),
    "vision-mbti-visioncoding": ("diagnosis", [1]),
    "vision-enneagram-visioncoding": ("diagnosis", [1]),
    "vision-strong-visioncoding": ("diagnosis", [1]),
    "vision-multipleintel-visioncoding": ("diagnosis", [1]),
    "vision-values-visioncoding": ("diagnosis", [1, 4]),
    "vision-readiness-visioncoding": ("diagnosis", [1]),
    "vision-five-stages": ("spine", [8]),
    "vision-mission-frame": ("spine", [5]),
    "vision-statement-writer": ("spine", [6]),
    "vision-smart-five-competence": ("spine", [8]),
    "vision-eight-training-areas": ("spine", [8]),
    "vision-financial-3shields-3windows": ("flesh", [7]),
    "vision-personal-future-research": ("flesh", [2]),
    "vision-futures-timeline-map": ("flesh", [2]),
    "vision-four-futures": ("flesh", [2]),
    "vision-future-promise-five-criteria": ("flesh", [3]),
    "vision-three-realm-balance": ("flesh", [4]),
    "vision-future-needs-prediction": ("flesh", [3]),
    "vision-strategy-coach": ("prescription", [7]),
    "vision-career-recommendation": ("prescription", [7]),
    "vision-clarity-coaching": ("prescription", [5]),
    "vision-goal-reframing": ("prescription", [7]),
    "vision-financial-coach": ("prescription", [7]),
    "vision-follow-through-habits": ("prescription", [8]),
    "vision-progress-review": ("prescription", [8]),
}


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm


def collect_skills() -> tuple[list[dict], list[str]]:
    skills: list[dict] = []
    warnings: list[str] = []
    if not SKILLS_DIR.exists():
        return skills, [f"⚠ skills/ 폴더가 없습니다: {SKILLS_DIR}"]
    for d in sorted(SKILLS_DIR.iterdir()):
        if not d.is_dir():
            continue
        sm = d / "SKILL.md"
        if not sm.exists():
            warnings.append(f"⚠ {d.name}: SKILL.md 없음")
            continue
        fm = parse_frontmatter(sm)
        name = fm.get("name", d.name)
        desc = fm.get("description", "")
        if not desc:
            warnings.append(f"⚠ {name}: description 누락")

        cat = fm.get("category")
        if cat:
            cat = cat.strip().lower()

        stages: list[int] | None = None
        raw_stage = fm.get("stage")
        if raw_stage:
            try:
                stages = [
                    int(s.strip())
                    for s in raw_stage.replace("·", ",").split(",")
                    if s.strip()
                ]
            except ValueError:
                warnings.append(f"⚠ {name}: stage 파싱 실패 ('{raw_stage}')")
                stages = None

        if not cat or not stages:
            default = DEFAULT_META.get(name)
            if default:
                cat = cat or default[0]
                stages = stages or list(default[1])
            else:
                warnings.append(
                    f"⚠ {name}: category/stage 누락 + DEFAULT_META 미등록 — "
                    "frontmatter에 'category:'와 'stage:'를 적거나 "
                    "_build_catalog.py DEFAULT_META에 등록하세요"
                )
                cat = cat or "uncategorized"
                stages = stages or []

        if cat not in CATEGORIES and cat != "uncategorized":
            warnings.append(f"⚠ {name}: 알 수 없는 category '{cat}' (기본값으로 처리)")
            cat = "uncategorized"

        skills.append(
            {
                "name": name,
                "desc": desc,
                "category": cat,
                "stages": sorted(set(stages)),
            }
        )
    return skills, warnings


def short_desc(desc: str, n: int = 70) -> str:
    if not desc:
        return ""
    desc = re.sub(r"\s+", " ", desc).strip()
    desc = re.sub(r"[*_`]", "", desc)
    if len(desc) <= n:
        return desc
    return desc[:n].rstrip() + "…"


def render_badge(skills: list[dict]) -> str:
    n = len(skills)
    return (
        "[![License: CC BY-NC-SA 4.0]"
        "(https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)]"
        "(https://creativecommons.org/licenses/by-nc-sa/4.0/)\n"
        f"[![Skills: {n}](https://img.shields.io/badge/Skills-{n}-blue)]"
        "(docs/SKILL_CATALOG.md)\n"
        "[![Korean](https://img.shields.io/badge/언어-한국어%20%2B%20English-success)](#)"
    )


def render_stage_mapping(skills: list[dict]) -> str:
    by_stage: dict[int, list[str]] = {st: [] for st in STAGE_TITLES}
    for s in skills:
        for st in s["stages"]:
            if st in by_stage:
                by_stage[st].append(s["name"])
    rows = [
        "| 단계 / Stage | 박사님 단계명 / Stage | 사용 스킬 / Skills |",
        "|----------|-------------------|----------------|",
    ]
    for st in sorted(STAGE_TITLES):
        names = by_stage[st]
        skill_str = " · ".join(f"`{n}`" for n in names) or "—"
        rows.append(f"| **{st}** | {STAGE_TITLES[st]} | {skill_str} |")
    return "\n".join(rows)


def render_category_table(skills: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = {}
    for s in skills:
        by_cat.setdefault(s["category"], []).append(s)
    rows = [
        "| # | 카테고리 / Category | 스킬 수 | 박사님 8단계 |",
        "|---|------------------|--------|--------------|",
    ]
    sorted_cats = sorted(CATEGORIES.items(), key=lambda kv: kv[1]["order"])
    for i, (key, meta) in enumerate(sorted_cats, 1):
        items = by_cat.get(key, [])
        rows.append(
            f"| {i} | **{meta['label_ko']} ({meta['label_en']})** | "
            f"{len(items)} | {meta['stages_ko']} |"
        )
    rows.append(f"| | **합계** | **{len(skills)}** | |")
    uncat = by_cat.get("uncategorized", [])
    if uncat:
        rows.append("")
        rows.append(
            f"⚠ 미분류 스킬 {len(uncat)}개: "
            + ", ".join(f"`{s['name']}`" for s in uncat)
        )
    return "\n".join(rows)


def render_skill_index(skills: list[dict]) -> str:
    rows = [
        "| 카테고리 | 스킬 | 단계 | 한 줄 설명 |",
        "|---------|------|------|----------|",
    ]
    sorted_cats = sorted(CATEGORIES.items(), key=lambda kv: kv[1]["order"])
    for key, meta in sorted_cats:
        items = [s for s in skills if s["category"] == key]
        items.sort(
            key=lambda s: (min(s["stages"]) if s["stages"] else 99, s["name"])
        )
        for s in items:
            stage_str = (
                "·".join(str(x) for x in s["stages"]) if s["stages"] else "—"
            )
            rows.append(
                f"| {meta['label_en']} | `{s['name']}` | {stage_str} | "
                f"{short_desc(s['desc'])} |"
            )
    uncat = [s for s in skills if s["category"] == "uncategorized"]
    for s in uncat:
        rows.append(
            f"| ⚠ Uncat. | `{s['name']}` | — | {short_desc(s['desc'])} |"
        )
    return "\n".join(rows)


def render_title_count(skills: list[dict]) -> str:
    n = len(skills)
    return (
        f"# {n}개 스킬 카탈로그 / {n} Skills Catalog\n\n"
        f"> 최윤식 박사 『미래준비학교』 토대 {n}개 Claude Code 스킬 전체 카탈로그\n"
        f"> Complete catalog of {n} Claude Code skills based on Dr. Choi's *Future Preparation School*"
    )


def replace_block(text: str, name: str, content: str) -> tuple[str, bool]:
    pat = re.compile(
        rf"<!-- AUTO:{re.escape(name)} -->.*?<!-- /AUTO:{re.escape(name)} -->",
        re.DOTALL,
    )
    repl = f"<!-- AUTO:{name} -->\n{content}\n<!-- /AUTO:{name} -->"
    new_text, n = pat.subn(repl, text)
    return new_text, n > 0


def update_file(
    path: Path, blocks: dict[str, str], *, check_only: bool = False
) -> tuple[bool, list[str]]:
    if not path.exists():
        return False, [f"⚠ {path} 없음"]
    text = path.read_text(encoding="utf-8")
    new_text = text
    msgs: list[str] = []
    for name, content in blocks.items():
        new_text, found = replace_block(new_text, name, content)
        if not found:
            msgs.append(
                f"⚠ {path.name}: 마커 'AUTO:{name}' 없음 — "
                "마커를 먼저 삽입해야 자동 갱신됩니다"
            )
    changed = new_text != text
    if changed and not check_only:
        path.write_text(new_text, encoding="utf-8")
    return changed, msgs


def main() -> int:
    check_only = "--check" in sys.argv
    skills, warnings = collect_skills()
    n = len(skills)

    # NOTE: STAGE_MAPPING은 박사님이 직접 관리하는 *순서가 의미를 가지는 표*
    # (예: 2단계 순차 흐름 personal-future-research → futures-wheel → four-futures → timeline-map).
    # 자동 정렬로 손상되지 않도록 자동 갱신 대상에서 제외한다.
    readme_blocks = {
        "BADGE": render_badge(skills),
        "CATEGORY_TABLE": render_category_table(skills),
        "SKILL_INDEX": render_skill_index(skills),
    }
    catalog_blocks = {
        "TITLE_COUNT": render_title_count(skills),
        "CATEGORY_TABLE": render_category_table(skills),
        "SKILL_INDEX": render_skill_index(skills),
    }

    readme_changed, m1 = update_file(README, readme_blocks, check_only=check_only)
    catalog_changed, m2 = update_file(CATALOG, catalog_blocks, check_only=check_only)

    print(f"📦 총 스킬: {n}개")
    by_cat: dict[str, list[str]] = {}
    for s in skills:
        by_cat.setdefault(s["category"], []).append(s["name"])
    sorted_cats = sorted(
        by_cat.items(),
        key=lambda kv: CATEGORIES.get(kv[0], {"order": 99})["order"],
    )
    for cat, names in sorted_cats:
        label = CATEGORIES.get(cat, {}).get("label_en", cat)
        print(f"   • {label}: {len(names)}개")

    print()
    if readme_changed:
        print(f"✓ README.md {'갱신 필요' if check_only else '갱신됨'}")
    else:
        print("· README.md 변경 없음")
    if catalog_changed:
        print(f"✓ docs/SKILL_CATALOG.md {'갱신 필요' if check_only else '갱신됨'}")
    else:
        print("· docs/SKILL_CATALOG.md 변경 없음")

    for msg in warnings + m1 + m2:
        print(msg)

    if check_only and (readme_changed or catalog_changed):
        return 1
    if any(s["category"] == "uncategorized" for s in skills):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
