# FACTCHECK — vox-rabi-parabola

## Claims Audit

| Claim | Beat | Verdict | Source/Note |
|-------|------|---------|-------------|
| Textbook perturbation theory predicts 247% at first pi-pulse | B02 | ✓ | Ch05: "At the first π-pulse (Ωt = π): exact P = 1; PT predicts (π/2)² ≈ 2.47" |
| PT assumes ground state amplitude c_i(t) ≈ 1 throughout | B04 | ✓ | Ch05: "we replace every c_n(t) on the right-hand side with its initial value: c_n(t) ≈ δ_ni" |
| PT result is a parabola: P = (Ωt/2)² | B05 | ✓ | Ch05: "P_PT = (Ωt/2)² — a parabola" |
| Exact Rabi formula: P = sin²(Ωt/2) | B06 | ✓ | Ch05: "sin²(Ωt/2) — a bounded oscillation" |
| Parabola and sine agree when Ωt ≪ 1 | B07 | ✓ | Ch05: "For Ωt ≪ 1, expanding sin² x ≈ x²" |
| At pi-pulse: exact = 100%, PT = 247% | B08 | ✓ | Ch05: exact quote |
| Rabi oscillations in qubits, NMR, trapped-ion gates | B09 | ✓ | Ch05: "A superconducting transmon... every qubit readout protocol" |
| Validity window: Ωt ≪ 1 | B09 | ✓ | Ch05: "The regime of validity is Ωt ≪ 1" |
| Illustrative: h-bar Omega = 0.01 eV, h-bar omega0 = 2 eV | B10 | ✓ illustrative | Ch05 worked example: "ℏω₀ = 2.00 eV, ℏΩ = 0.010 eV" |
| At pi-pulse PT predicts 2.47, Rabi gives 1 | B10 | ✓ | Ch05: "(π/2)² ≈ 2.47" |

## Terms Table
| Term | Debut Beat | Prior beat creating need |
|------|-----------|--------------------------|
| perturbation theory | B02 | B01 poses the question |
| parabola (runaway) | B05 | B04 explains why PT keeps integrating |
| Rabi formula / Rabi oscillation | B06 | B05 shows PT fails |
| pi-pulse | B08 | B06/B07 establish Rabi oscillation concept |
| Omega (Rabi frequency) | B07 | B06 introduces Rabi formula |

## Illustrative Numbers
- B10: h-bar Omega = 0.01 eV, h-bar omega0 = 2 eV — from chapter worked example; labeled "Illustrative" in narration.
