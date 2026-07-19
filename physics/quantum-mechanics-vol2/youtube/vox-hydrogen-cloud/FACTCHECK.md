# FACTCHECK — vox-hydrogen-cloud

## Claims audit

| beat | claim | verdict | source |
|------|-------|---------|--------|
| B02 | "Bohr's electron circles at one fixed radius — the Bohr radius, about half an angstrom" | ✓ | Ch.9: "a_0 ≈ 0.529 Å" — the Bohr radius |
| B02 | "Both most-likely and average position equal that same radius in Bohr model" | ✓ | Implied: a point mass on a circle has r_mp = mean(r) = r_orbit |
| B03 | "Schrödinger gives a radial probability curve with peak at one radius and mean at a different larger radius" | ✓ | Ch.9: "r_mp = a_0, mean = 3a_0/2 — two different numbers" |
| B05 | "For any classical orbit, most-likely and average both give you the orbital radius" | ✓ | Standard mechanics: a fixed-radius orbit has a delta-distribution in r |
| B06 | "The wave function's absolute square is largest at the nucleus for the 1s state" | ✓ | Ch.9: psi_100 = (1/sqrt(pi a_0^3)) e^(-r/a_0), maximum at r=0 |
| B06 | "Probability in a thin shell grows as r-squared times the density" | ✓ | Ch.9: "P(r) = r^2 |R_10(r)|^2" with 4pi r^2 dr shell volume |
| B07 | "The curve peaks at the Bohr radius" | ✓ | Ch.9: "dP/dr = 0 gives r_mp = a_0" |
| B08 | "Peak at one Bohr radius" | ✓ | Ch.9: r_mp = a_0 |
| B08 | "Mean at one-and-a-half Bohr radii" | ✓ | Ch.9: "<r> = 3a_0/2" |
| B08 | "The tail skews the average past the peak" | ✓ | Ch.9: "P(r) is right-skewed — it has a long tail at large r that pulls the mean to the right of the peak" |
| B09 | "A distribution with two distinct typical values is spread out — not a path" | ✓ | Ch.9: "The fact that r_mp != <r> is a signature of wave mechanics" |
| B10 | "Student measures 1000 times, most common near one Bohr radius, average comes out 1.5" | illustrative | Consistent with Ch.9; labeled illustrative |

## Terms table

| term | debut beat | prior beat creating need |
|------|-----------|--------------------------|
| Bohr radius | B02 | B01 (hook mentions Bohr put electron on circle) |
| radial probability | B06 | B05 (naive orbit gives one number, need to understand what wave mechanics actually says) |
| right-skewed | B08 | B07 (P(r) curve shown with long tail) |

## Exclusions confirmed
- No radial equation / Laguerre derivation on screen ✓
- No SO(4) symmetry ✓
- No normalization algebra ✓

## Illustrative numbers
- B10: "1000 measurements, most common near a_0, average at 1.5 a_0" — labeled illustrative; consistent with exact values from Ch.9
