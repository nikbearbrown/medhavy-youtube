# FACTCHECK — vox-gaussian-polar
## Every claim checked against source: quantum-mechanics-vol5/chapters/02-probability-normalization-expectation.md

## B02 — The Gaussian integral has no elementary antiderivative
- The antiderivative of e^{-x^2} is (sqrt(pi)/2)*erf(x), where erf is the error function.
  erf is NOT an elementary function (not expressible in terms of +, *, exp, log, trig).
  CORRECT: no elementary antiderivative.
- The integral int_{-inf}^{inf} e^{-x^2} dx = sqrt(pi). CORRECT.

## B04 — Squaring trick: I^2 = double integral
- I = int_{-inf}^{inf} e^{-x^2} dx.
- I^2 = (int e^{-x^2} dx)(int e^{-y^2} dy) = int int e^{-(x^2+y^2)} dx dy.
- The two factors use different dummy variables (x, y). CORRECT.
- The product of two integrals over independent variables equals the double integral. CORRECT (Fubini's theorem).

## B05 — Polar coordinate substitution
- x = r*cos(theta), y = r*sin(theta). CORRECT.
- x^2 + y^2 = r^2. CORRECT.
- Area element: dx*dy = r*dr*d(theta). CORRECT (Jacobian = r).
- Limits: r in [0, inf), theta in [0, 2*pi). CORRECT (covers entire plane once).

## B06 — Computing I^2 = pi
- I^2 = int_0^{2pi} d(theta) * int_0^{inf} e^{-r^2} * r dr.
- Theta integral: int_0^{2pi} d(theta) = 2*pi. CORRECT.
- r integral: int_0^{inf} e^{-r^2} * r dr. Substitute u = r^2, du = 2r*dr:
  = (1/2) * int_0^{inf} e^{-u} du = (1/2)*[-e^{-u}]_0^{inf} = (1/2)*(0 - (-1)) = 1/2. CORRECT.
- I^2 = 2*pi * (1/2) = pi. CORRECT.
- I = sqrt(pi) (positive since I > 0). CORRECT.

## B07 — QM Gaussian wavefunction normalization
- A normalized Gaussian wavefunction: psi(x) = (2*pi*sigma^2)^{-1/4} * exp(-x^2/(4*sigma^2)).
- Normalization: int |psi|^2 dx = 1 requires the prefactor (2*pi*sigma^2)^{-1/4}. CORRECT.
- The normalization integral reduces to sqrt(pi) * sigma (after variable change). CORRECT.
- Specifically int exp(-x^2/(2*sigma^2)) dx = sigma*sqrt(2*pi), derived from the Gaussian integral. CORRECT.

## B08 — Gaussian moments via parameter differentiation
- Define I(a) = int_{-inf}^{inf} e^{-a*x^2} dx = sqrt(pi/a). CORRECT (from the main result by substitution u=sqrt(a)*x).
- Differentiate: -dI/da = int x^2 * e^{-a*x^2} dx = (sqrt(pi)/2) * a^{-3/2}. CORRECT.
- At a=1: int x^2 * e^{-x^2} dx = sqrt(pi)/2. CORRECT.
- The moment <x^2> for the Gaussian probability density (1/sqrt(pi)) * e^{-x^2} equals 1/2. CORRECT.

## B09 — Concrete normalization check
- I = sqrt(pi) => (1/sqrt(pi)) * int_{-inf}^{inf} e^{-x^2} dx = (1/sqrt(pi)) * sqrt(pi) = 1. CORRECT.
- (1/sqrt(pi)) * e^{-x^2} is a valid normalized probability density. CORRECT.
- "The probability of finding the particle somewhere is certain." = normalization = 1. CORRECT.

## Terms table
| Term | Debuts | Made needed by |
|------|--------|---------------|
| Gaussian integral | B02 | B01 (can't integrate directly) |
| elementary antiderivative | B02 | B02 setup |
| dummy variable / independent integrals | B04 | B04 squaring trick |
| double integral | B04 | B04 squaring |
| polar coordinates | B05 | B04 (r^2 = x^2 + y^2) |
| Jacobian / area element r dr dtheta | B05 | B05 polar switch |
| substitution u = r^2 | B06 | B06 r-integral |
| normalization | B07 | B07 QM connection |
| probability density | B09 | B09 example |

## Illustrative numbers
- B09: (1/sqrt(pi)) * sqrt(pi) = 1 is exact, not illustrative.
- All numerical claims are exact mathematical results.

VERDICT: All facts verified. The Gaussian integral equals sqrt(pi); the polar-coordinate squaring trick is the standard derivation. Every QM normalization claim follows directly.
