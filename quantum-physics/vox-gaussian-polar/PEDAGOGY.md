# PEDAGOGY AUDIT — vox-gaussian-polar

## Act structure map

| Beat | Act | Type |
|------|-----|------|
| B01 | COLD OPEN | CARD |
| B02 | THE QUESTION | CARD |
| B03 | THE PROBLEM | GRAPHIC |
| B04 | THE PROBLEM | GRAPHIC |
| B05 | THE MECHANISM | GRAPHIC |
| B06 | THE MECHANISM | GRAPHIC |
| B07 | THE IMPLICATION | GRAPHIC |
| B08 | THE IMPLICATION | GRAPHIC |
| B09 | THE EXAMPLE | GRAPHIC |
| B10 | RECAP | CARD |

Act structure present and in order: COLD OPEN -> QUESTION -> PROBLEM -> MECHANISM -> IMPLICATION -> EXAMPLE -> RECAP. PASS.

## Key-case cold open
B01 opens with a concrete statement of the impossibility: "You can't integrate e to the minus x squared the normal way." Then reveals the trick: "Square it and rotate." This is a concrete mystery — no thesis given early, the HOW is withheld until B05-B06. PASS.

## Gap formula on THE QUESTION beat (B02)
"How do you compute int e^{-x^2} dx when it has no antiderivative?" — named on screen AND in narration. The gap is: the function has finite area visibly, but no integration technique closes it. PASS.

## Utility-framing lint check
Scanning all narration_text fields:
- No instance of "is critical for", "important to understand", "we'll cover", "in this video".
- B07 mentions "underlies all of quantum mechanics" — this is a consequence, not utility framing for the intro. PASS.

## Vocabulary law
- "Gaussian integral" debuts B02 — B01 created the need (you can't integrate it).
- "double integral" debuts B04 — B04 explains why (squaring trick).
- "polar coordinates" debuts B05 — B04 set up x^2+y^2 = r^2 naturally.
- "Jacobian / r dr dtheta" debuts B05 — part of the coordinate switch explanation.
- "substitution u = r^2" debuts B06 — B05 created the r-integral.
- "normalization" debuts B07 — B06 delivered sqrt(pi), now we connect to QM.
No term debuts before its need is established. PASS.

## Equations
The film uses equations throughout (B04, B05, B06 are step-by-step derivation). These are shown as text overlays, not narrated derivations — they serve as visual confirmation of the spoken steps. No EQUATIONS.md tangent required (the equations ARE the mechanism here — each step is one beat, ~20s, within the ~45s guideline). PASS.

## Recap endcard (B10)
"Square it: I^2 = int int e^{-r^2} dA. Switch to polar: r dr dtheta. I^2 = pi -> I = sqrt(pi)."
States question (can't integrate directly) -> answer (square, polar, get sqrt(pi)). Topic eyebrow: "QUANTUM MECHANICS". Does not say "chapter" or full book title. PASS.

## THE EXAMPLE act
B09 is THE EXAMPLE: concrete normalization check with exact numbers. (1/sqrt(pi)) * int e^{-x^2} dx = (1/sqrt(pi)) * sqrt(pi) = 1. This is exact math, labeled as exact in FACTCHECK. PASS.

## Length law
Total estimated: ~152s (~2:32). Well under 5:00 hard cap. PASS.

## Color law
TEAL = 1D bell curve / x-direction. CRIMSON = 2D surface / r-direction. GOLD = polar grid highlight fill (never text color). SLATE = axes/structure. Two accents (TEAL + CRIMSON) stated in metadata.color_semantics. PASS.

VERDICT: PASS
