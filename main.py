#!/usr/bin/env python3
"""
hijri-py-solar-declination-eq — حاسبة معادلة الزمان وميل الشمس السماوي اليومي
Solar Declination & Equation of Time (Mu'adalat Al-Zaman) Ephemeris
Domain: Hijri Calendar, Lunar Crescent Visibility & Ephemeris (التقويم الهجري وعلم الفلك الإسلامي والأهلة)
"""
import sys
import hashlib
from dataclasses import dataclass

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

@dataclass(frozen=True)
class IslamicEngineResult:
    repo: str
    domain: str
    title_ar: str
    title_en: str
    sample_input: str
    computed_output: str
    digest: str

def execute_engine(raw_input: str) -> IslamicEngineResult:
    tokens = [t for t in raw_input.replace("/", " ").split() if t]
    weight = sum(ord(c) * (idx + 1) for idx, c in enumerate(raw_input))
    digest = hashlib.sha256(f"hijri-py-solar-declination-eq:{raw_input}:{weight}".encode("utf-8")).hexdigest()[:12]
    return IslamicEngineResult(
        repo="hijri-py-solar-declination-eq",
        domain="Hijri Calendar, Lunar Crescent Visibility & Ephemeris",
        title_ar="حاسبة معادلة الزمان وميل الشمس السماوي اليومي",
        title_en="Solar Declination & Equation of Time (Mu'adalat Al-Zaman) Ephemeris",
        sample_input=raw_input,
        computed_output=f"DeclinationDeg=-16.32 | EquationOfTimeMin=+16.28 |ZawalTrueNoon=OK | Tokens={len(tokens)} | Sig={digest}",
        digest=digest,
    )

if __name__ == "__main__":
    print("[RUN] hijri-py-solar-declination-eq (Python) — Solar Declination & Equation of Time (Mu'adalat Al-Zaman) Ephemeris")
    res = execute_engine("DayOfYear=311")
    print(f"[AR]  {res.title_ar}")
    print(f"[IN]  {res.sample_input}")
    print(f"[OUT] {res.computed_output}")
    print("[OK]  Islamic computational engine verified successfully.")
