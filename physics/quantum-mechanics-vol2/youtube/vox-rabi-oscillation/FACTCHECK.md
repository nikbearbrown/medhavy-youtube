# FACTCHECK — vox-rabi-oscillation

Source: `quantum-mechanics-vol2/chapters/04-quantum-dynamics-and-the-pictures.md` (§ "Worked Example — Rabi Oscillation")

## Claims verified

**B01 — Complete population transfer**
"The spin doesn't just wobble — it marches all the way down to spin-down."
Source: "The population starts in |↑⟩, transfers entirely to |↓⟩ at t = π/ω₀, and returns." ✓

**B02 — NMR context**
"A short radio pulse at just the right frequency flips the spin completely."
Source: "a spin driven by a resonant pulse oscillates between up and down at the Rabi frequency." ✓

**B03 — Sinusoidal exchange**
"Spin-up starts at one, falls to zero at half a period, rises back to one."
Source (eq.): ⟨S_z⟩(t) = (ℏ/2)cos(ω₀t), which means P(↑) = cos²(ω₀t/2): starts at 1, reaches 0 at t = π/ω₀. ✓
"The two probabilities sum to one at all times." — normalization. ✓

**B07 — Relative phase beats**
"The beat drives the populations at the Rabi frequency."
Source: "All dynamics live in the relative phases between energy eigenstates. A single eigenstate has no relative phase... Two or more eigenstates produce a beat frequency (E_m - E_n)/ℏ that drives oscillations in every observable." ✓

**B08 — Complete destructive/constructive interference at phase=pi**
"When the beat reaches pi, the two phasors are exactly out of step. They destructively interfere for spin-up and constructively interfere for spin-down."
Source: Explicit calculation shows P(↑) = cos²(ω₀t/2) → 0 at ω₀t/2 = π/2, i.e., t = π/ω₀. ✓

**B09 — Rabi frequency = energy gap / ℏ**
"The Rabi frequency is just the energy gap between the two eigenstates divided by h-bar."
Source: Hamiltonian H = ω₀S_x; eigenstates ±ℏω₀/2; gap = ℏω₀; beat frequency = ω₀. ✓
"A weaker field means a smaller gap, a longer period — a slower oscillation. But the oscillation still goes all the way."
Source: amplitude of flip is always 100% by the interference argument; only the period changes. ✓

**B10 — Pi-pulse NMR (illustrative)**
"She applies a radio-frequency pulse for exactly half a Rabi period — a pi-pulse. The spin-up population drops to zero: complete inversion."
Labeled illustrative. Mechanism matches source. ✓

## Exclusions confirmed
- No eigenstate-expansion algebra on screen
- No interaction-picture formalism
- No pulse-area calculation

## Terms table
| Term | Debut beat | Setup beat |
|------|-----------|------------|
| Rabi oscillation | B02 | B01 (the phenomenon) |
| eigenstate | B06 | B05 (energy eigenstates introduced by need) |
| beat frequency | B07 | B06 (two eigenstates with different energies) |
| Rabi frequency | B09 | B07 (the beat frequency concept) |
| pi-pulse | B10 | B09 (half a period) |

## VERDICT: PASS
