# PEDAGOGY — vox-spin-echo

## Concept chain
1. Spins in a field precess (Larmor). Inhomogeneous field → each spin sees slightly different B → slightly different precession rate.
2. After time τ, the phase spread has accumulated: fast spins lead, slow spins trail. Vector sum → zero.
3. π-pulse inverts each spin's phase: fast ones (previously ahead) are now behind; slow ones (previously behind) are now ahead.
4. After another τ, the fast spins have exactly caught up — everyone arrives at the same phase. Echo.
5. The echo amplitude is NOT full — it decays as e^(-2τ/T₂). Static inhomogeneity cancels. Only irreversible T₂ processes (random fluctuating spin-spin interactions) reduce the echo.
6. Application: MRI measures T₂ in imperfect magnets by varying τ and fitting echo heights.

## Misconception barriers
- "The π-pulse somehow corrects the field" — NO: the field remains inhomogeneous throughout; the pulse only reverses the spin ordering.
- "The echo restores full signal" — NO: only inhomogeneous dephasing is reversed; T₂ decay is not.
- "T₂ = T₂*" — T₂* includes inhomogeneous broadening; spin-echo measures the true T₂, free of field imperfections.

## Narrative logic check
- B01/B02: cold open shows the mystery (fans out → pulses → echoes back) before explaining it. ✓
- B03: question stated explicitly. ✓
- B04/B05: builds the problem — why spins fan out. ✓
- B06/B07: mechanism — why π-pulse reverses it. ✓
- B08/B09: implication — T₂ measurement and MRI. ✓
- B10: illustrative numerical example. ✓
- B11: recap card. ✓

## Terms introduced in order
1. [implicitly] precession / fan-out — B01
2. π-pulse — B06 (after dephasing problem is established in B04/B05)
3. spin echo / 2τ — B07 (after mechanism is shown)
4. T₂ — B08 (after echo mechanism is clear)
5. MRI — B09

No term introduced before the need is established.

## Runtime check
Estimated: ~113s (~1:53). Well within 5:00 cap.

VERDICT: PASS
