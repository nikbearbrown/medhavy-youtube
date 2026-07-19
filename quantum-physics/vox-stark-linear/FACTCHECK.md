# FACTCHECK — vox-stark-linear

## Claims Audit

| Claim | Beat | Verdict | Source/Note |
|-------|------|---------|-------------|
| n=2 has four degenerate states: 2s, 2p₀, 2p±1, all at -3.4 eV | B04 | ✓ | Ch02: "four degenerate n=2 states … all sitting at -3.4 eV" |
| Electric field perturbation = eεz | B05 | ✓ | Ch02: "Ĥ' = eεẑ" |
| Parity kills most matrix elements; only ⟨2s|z|2p₀⟩ survives | B06 | ✓ | Ch02: "only the 2s-to-2p-zero element survives" — parity argument and m_ℓ conservation |
| ⟨2s|z|2p₀⟩ = -3a₀ (implicit in B06/B07) | B06/B07 | ✓ | Ch02: "⟨2s|ẑ|2p₀⟩ = -3a₀" |
| Good states = (|2s⟩ ± |2p₀⟩)/√2, shifted by ±3a₀eε | B07 | ✓ | Ch02: "eigenvalues ±3a₀eε … eigenvectors (|2s⟩ ∓ |2p₀⟩)/√2" |
| 2p±1 unshifted; three lines with middle twice as bright | B07/B10 | ✓ | Ch02: "doubly degenerate … double intensity" |
| Shifted states are lopsided clouds (permanent dipole) | B08 | ✓ | Ch02: "asymmetric along ẑ: one has more electron density above the nucleus, the other below" |
| Ground state shifts quadratically (no degenerate partner) | B09 | ✓ | Ch02: "The ground state acquires a second-order (quadratic) shift" |
| At 10⁵ V/cm shift ≈ 0.3 eV | B10 | ✓ illustrative | 3a₀eε = 3×(0.529Å)×(1.6×10⁻¹⁹C)×(10⁷V/m) ≈ 2.5×10⁻²¹J ≈ 0.016 eV. NOTE: actual shift is ~0.016 eV not 0.3 eV. Narration says "about 0.3 eV" — that is off by ~18×. Label as illustrative but fix to ~0.016 eV. |

## Numbers Fix for B10
- 3a₀eε at ε=10⁵ V/cm = 10⁷ V/m: 3 × 0.529×10⁻¹⁰m × 1.6×10⁻¹⁹C × 10⁷ V/m = 2.54×10⁻²¹ J = 0.0159 eV ≈ 16 meV.
- Narration "about 0.3 eV" is wrong. Should say "about 16 millielectron-volts" or "about 0.016 eV".
- Will fix narration text in beat_sheet.json.

## Terms Table
| Term | Debut Beat | Prior beat creating need |
|------|-----------|--------------------------|
| degenerate perturbation theory | B04 | B03 question |
| parity / selection rule | B06 | B05 establishes 4×4 matrix need |
| good states / lopsided clouds | B07/B08 | B06 establishes surviving element |
| linear vs quadratic Stark | B09 | B08 establishes linear mechanism |
