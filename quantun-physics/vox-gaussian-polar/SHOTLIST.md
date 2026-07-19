# SHOTLIST — vox-gaussian-polar
## Square the integral, spin it into polar coordinates

---

## Histogram
- CARD: 3 (B01, B02, B10)
- GRAPHIC: 7 (B03–B09)
- STILL·ai: 0

## Rhythm check
B01 CARD, B02 CARD — 2 consecutive CARDs (acceptable: cold open + question).
B03–B09: 7 consecutive GRAPHICs (acceptable: all mechanism/implication/example).
B10 CARD — recap endcard.
No more than 2 consecutive of same type except the GRAPHIC run (standard for derivation-heavy reels). PASS.

## Act map
| Beat | Act | Type | Shot source |
|------|-----|------|-------------|
| B01 | COLD OPEN | CARD | own |
| B02 | THE QUESTION | CARD | own |
| B03 | THE PROBLEM | GRAPHIC | own |
| B04 | THE PROBLEM | GRAPHIC | own |
| B05 | THE MECHANISM | GRAPHIC | own |
| B06 | THE MECHANISM | GRAPHIC | own |
| B07 | THE IMPLICATION | GRAPHIC | own |
| B08 | THE IMPLICATION | GRAPHIC | own |
| B09 | THE EXAMPLE | GRAPHIC | own |
| B10 | RECAP | CARD | own |

## Color law
- TEAL = 1D bell curve / x-direction
- CRIMSON = 2D surface / r-direction
- GOLD = polar grid highlight fill (FILL ONLY — never a text color)
- SLATE = axes / structure labels

## Exclusions confirmed
- No other methods of evaluating Gaussian integrals (residues, series)
- No Gamma function
- No error function erf
- No moment-generating function formalism
- Squaring trick + polar rotation ONLY

---

## Per-beat shot descriptions

### B01 — COLD OPEN (CARD, own)
CARD with QUANTUM MECHANICS eyebrow. Headline states the impossibility and the trick.

### B02 — THE QUESTION (CARD, own)
CARD with THE QUESTION eyebrow. Headline names the problem explicitly.

### B03 — THE PROBLEM: 1D bell curve (GRAPHIC, own)
- Axes (SLATE). TEAL Gaussian bell curve. Shaded area under curve (TEAL fill).
- Label I = int e^{-x^2} dx.
- Annotation: "no elementary antiderivative".

### B04 — THE PROBLEM: Squaring trick (GRAPHIC, own)
- Show equation I^2 = (int e^{-x^2} dx)(int e^{-y^2} dy) = int int e^{-(x^2+y^2)} dx dy.
- TEAL equation text, then 2D surface illustration in CRIMSON.

### B05 — THE MECHANISM: Polar substitution (GRAPHIC, own)
- Left panel: Cartesian grid with circle x^2+y^2 = r^2 (SLATE).
- Right panel: polar grid with r and theta labeled (GOLD highlight for angle, CRIMSON for r).
- Arrow between panels labeled "x = r cos theta, y = r sin theta".
- Area element: dx dy -> r dr dtheta.

### B06 — THE MECHANISM: Computing I^2 (GRAPHIC, own)
- Step-by-step equation build in CRIMSON.
- Show integral splits into theta (gives 2pi) and r (substitution u=r^2 gives 1/2).
- I^2 = 2pi * (1/2) = pi.
- Final: I = sqrt(pi) in TEAL.

### B07 — THE IMPLICATION: QM normalization (GRAPHIC, own)
- Show QM Gaussian wavefunction psi(x) formula in TEAL.
- Normalization integral in CRIMSON with arrow pointing to sqrt(pi) factor.

### B08 — THE IMPLICATION: Gaussian moments (GRAPHIC, own)
- Show I(a) = int e^{-ax^2} dx = sqrt(pi/a) in TEAL.
- Show -dI/da formula to extract <x^2>.
- Connect to same trick.

### B09 — THE EXAMPLE: Normalization check (GRAPHIC, own)
- Clean equation display:
  (1/sqrt(pi)) * int_{-inf}^{inf} e^{-x^2} dx = (1/sqrt(pi)) * sqrt(pi) = 1.
- TEAL for (1/sqrt(pi)), CRIMSON for integral = sqrt(pi), GOLD highlight bar on = 1.
- "Normalization confirmed" bar below.

### B10 — RECAP (CARD, own)
- CARD with QUANTUM MECHANICS eyebrow.
- Headline: 3-line recap of the method.
