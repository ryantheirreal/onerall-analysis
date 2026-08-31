#!/usr/bin/env python3
"""Rebrand visível: Artificial Analysis -> Onerall Analysis AI.
NÃO toca em paths técnicos, hashes de bundle, nem nomes de classe CSS.
Roda em dry-run por padrão; usar --apply para gravar.
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"

PAIRS = [
    ("Artificial Analysis", "Onerall Analysis AI"),
    (" Artificial Analysis ", " Onerall Analysis AI "),
    ("'Artificial Analysis'", "'Onerall Analysis AI'"),
    ("\"Artificial Analysis\"", "\"Onerall Analysis AI\""),
    ("ArtificialAnalysis", "OnerallAnalysis"),
]

# Em paths/href visíveis, trocamos o domínio também
DOMAIN_PAIRS = [
    ("https://artificialanalysis.ai", "https://analysis.onerall.com"),
    ("http://artificialanalysis.ai",  "http://analysis.onerall.com"),
    ("//artificialanalysis.ai",       "//analysis.onerall.com"),
]

TARGETS = [
    PUB / "index.html",
    PUB / "js" / "page-01a6245af3c0fec6.js",
    PUB / "js" / "74630-b2533bcea6fc5b9e.js",
    PUB / "js" / "46056-700627a25bad4b71.js",
]


def rebrand(text: str) -> tuple[str, dict]:
    counts = {}
    for old, new in PAIRS + DOMAIN_PAIRS:
        n = text.count(old)
        if n:
            text = text.replace(old, new)
            counts[f"{old!r} -> {new!r}"] = n
    return text, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Gravar mudanças no disco")
    args = ap.parse_args()

    total = 0
    for path in TARGETS:
        if not path.exists():
            print(f"[skip] {path} (não existe)")
            continue
        original = path.read_text(encoding="utf-8")
        new, counts = rebrand(original)
        file_total = sum(counts.values())
        total += file_total
        marker = "OK " if file_total else "   "
        print(f"[{marker}] {path.relative_to(ROOT)} -> {file_total} substituição(ões)")
        for k, v in counts.items():
            print(f"        {k}: {v}")
        if args.apply and file_total:
            path.write_text(new, encoding="utf-8")
            print(f"        gravado.")
    print()
    print(f"Total de substituições: {total}")
    if not args.apply:
        print("(dry-run) use --apply para gravar.")


if __name__ == "__main__":
    main()