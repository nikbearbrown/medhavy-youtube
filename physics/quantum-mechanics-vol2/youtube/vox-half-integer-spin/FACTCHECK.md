# FACTCHECK — vox-half-integer-spin

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B02 | Ladder algebra allows ℓ = 0, ½, 1, 3/2, 2, … | ✓ | Ch.06: "The significance of the algebraic approach is that it allows ℓ to be a half-integer." |
| B03 | Atomic orbitals have integer ℓ only: 0 (s), 1 (p), 2 (d), 3 (f) | ✓ | Standard; Ch.06 confirms orbital angular momentum is integer-only |
| B06 | Orbital L_z eigenfunction is e^{imφ}; single-valuedness requires e^{2πim}=1, so m integer | ✓ | Ch.06 verbatim: "Single-valuedness — e^{im(φ+2π)} = e^{imφ} — requires e^{2πim} = 1, so m must be an integer and ℓ must be a non-negative integer." |
| B07 | For m=½: after φ → φ+2π, wave function gains factor e^{iπ} = −1 (sign flip) | ✓ | e^{i(φ+2π)/2} = e^{iφ/2} · e^{iπ} = −e^{iφ/2}; sign flips, single-valuedness fails |
| B08 | Spin lives in abstract 2D complex space with no azimuthal angle φ | ✓ | Ch.06: "For spin angular momentum, there is no wave function in position space and no single-valuedness condition to impose." |
| B08 | Half-integer spin is realized without restriction | ✓ | Ch.06: "Nothing prevents ℓ = 1/2. The algebra is more general than the orbital case; the sphere has added a constraint that the algebra itself does not require." |
| B10 | Student writes e^{iφ/2}, finds sign flip after 2π rotation | ✓ | Ch.06 example alluded to; calculation: e^{i(φ+2π)/2} = e^{iφ/2}·e^{iπ} = −e^{iφ/2} ✓ |

## Terms table

| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| ladder operators / raising/lowering | B02 | — (hook frames the algebra) |
| half-integer quantum number | B02 | B01 (contrast established) |
| orbital angular momentum | B03 | B02 (two cases presented) |
| wave function / e^{imφ} | B06 | B04 (THE QUESTION asks about position space) |
| single-valuedness | B06 | B06 (periodicity condition explained) |
| spin / abstract 2D space | B08 | B07 (negative result for orbitals established) |
