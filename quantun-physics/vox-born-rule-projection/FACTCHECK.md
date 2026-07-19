# FACTCHECK — vox-born-rule-projection

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B02 | Born rule: P = |⟨a|ψ⟩|² | ✓ | Ch.02: P(aₙ) = |cₙ|² = |⟨aₙ|ψ⟩|², standard result |
| B02 | For |+x⟩ measured along z: P(+z) = ½ | ✓ | ⟨+z|+x⟩ = 1/√2, |1/√2|² = ½ |
| B03 | |+x⟩ at 45° from |+z⟩ in Hilbert space; shadow = 1/√2; squared = ½ | ✓ | |⟨+z\|+x⟩|² = ½; angle between them in Hilbert space = 45°; shadow length 1/√2 squared is ½ |
| B05 | Inner product is complex; probability must be real and non-negative | ✓ | Ch.02: "The quantity ⟨aₙ|ψ⟩ = cₙ is a complex amplitude. The probability is |cₙ|², its squared modulus." |
| B06 | Squared moduli of coefficients sum to 1 when state is normalized | ✓ | Ch.02: completeness → Σ|cₙ|² = ⟨ψ|ψ⟩ = 1 |
| B08 | Phase disappears under |·|²; survives in interference | ✓ | Ch.02: "That phase disappears when we compute a single measurement probability, but it returns in interference terms whenever two amplitudes feed the same outcome." |
| B09 | Born rule is forced by Hilbert-space geometry (not a separate axiom in this sense) | ✓ (framing) | Ch.02: "Probability is not a separate postulate bolted onto the formalism — it is the squared norm of a component, a geometric quantity that already lives in the structure of the Hilbert space." |
| B10 | At 30° from x-axis: P(E₁) = cos²(30°) ≈ 0.75, P(E₂) = sin²(30°) = 0.25 | ✓ | cos²(30°) = 3/4 = 0.75; sin²(30°) = 1/4 = 0.25; sum = 1 ✓ |

## Note on B03 geometry
Fixed in beat_sheet.json: narration now says "forty-five degrees" (correct — |+x⟩ and |+z⟩ are at 45° in Hilbert space, giving inner product 1/√2 and probability ½). The 90° case would give probability 0 (orthogonal states). ✓

## Terms table

| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| Born rule | B01 | — (hook) |
| inner product / projection | B03 | B02 (probability question established) |
| amplitude (complex) | B05 | B04 (question asks why squared) |
| squared modulus | B05 | B04 (question asks why squared) |
| eigenbasis / eigenstate | B06 | B05 (decomposition mentioned) |
| unit vector / normalized | B06 | B06 (sum to 1 explained) |
