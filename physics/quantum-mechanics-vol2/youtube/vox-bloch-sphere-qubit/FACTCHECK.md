# FACTCHECK — vox-bloch-sphere-qubit

## Claims audit

| beat | claim | verdict | source |
|------|-------|---------|--------|
| B02 | "qubit is alpha|0>+beta|1> with complex alpha, beta" | ✓ | Ch.7: two-dimensional complex vector space C^2 |
| B03 | "probability of measuring zero is |alpha|^2" | ✓ | Born rule, standard QM |
| B03 | "probabilities sum to one" | ✓ | normalization |
| B05 | "two complex numbers need four real parameters" | ✓ | each complex number is 2 real parameters |
| B06 | "normalization: |alpha|^2 + |beta|^2 = 1 removes one param (four to three)" | ✓ | standard; Ch.7 "minus one constraint from normalization" |
| B07 | "global phase: multiply by e^{i phi}, all probabilities unchanged; removes one more param" | ✓ | Ch.7: "unobservable global phase" |
| B07 | "three minus one equals two" | ✓ | arithmetic |
| B08 | "theta=0: north pole, all up; theta=pi: south pole, all down; equator: equal superpositions" | ✓ | Ch.7: "The north pole (theta=0) is |up>; south pole (theta=pi) is |down>; equator holds equal superpositions" |
| B09 | "P(+) = cos^2(gamma/2)" | ✓ | Ch.7: boxed formula |
| B09 | "perpendicular gives 50%, parallel gives 100%, antiparallel gives 0%" | ✓ | Ch.7: verified against three cases |
| B10 | "theta=60, gamma=60 (measuring along z), P(up) = cos^2(30) = 3/4" | ✓ | cos^2(30 deg) = (sqrt(3)/2)^2 = 3/4 |
| B10 | "1000 copies, ~750 up" | illustrative | EXAMPLE beat — invented scenario labeled illustrative |

## Terms table

| term | debut beat | prior beat creating need |
|------|-----------|--------------------------|
| qubit | B02 | B01 (hook) |
| Born rule | B03 | B02 (superposition setup) |
| normalization | B03 | B03 (probabilities sum to 1) |
| global phase | B07 | B06 (parameter counting) |
| Bloch sphere | B08 | B07 (2 params = sphere) |
| theta, phi | B08 | B08 (the sphere's coordinates) |
| gamma (angle between vectors) | B09 | B08 (state and analyzer on sphere) |

## Exclusions confirmed
- No half-angle proof from the amplitudes ✓
- No gate operations ✓
- No density-matrix/mixed states ✓

## Illustrative numbers
- B10: theta=60 degrees, 1000 copies, ~750 results — all labeled illustrative.
