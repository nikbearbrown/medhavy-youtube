# FACTCHECK — vox-phase-clock

## Claims audit

| beat | claim | verdict | source |
|------|-------|---------|--------|
| B02 | "Same number every time [measuring energy of eigenstate]" | ✓ | Ch.4: "The state picks up a phase but does not change. Every expectation value is constant." |
| B02 | "The phase of the state rotates continuously" | ✓ | Ch.4: e^(-iEt/hbar) factor on energy eigenstates |
| B03 | "Two energy eigenstates together produce a beat pattern" | ✓ | Ch.4: "Two or more eigenstates produce a beat frequency (E_m - E_n)/hbar that drives oscillations in every observable." |
| B05 | "Probability squares the magnitude — rotating the phase everywhere leaves every magnitude unchanged" | ✓ | Ch.4: |e^(-iEt/hbar)|^2 = 1, so |psi|^2 unchanged |
| B06 | "Clock hand spinning in the complex plane, shadow frozen" | ✓ | Ch.4: |psi_{100}|^2 constant for eigenstate, phase rotating |
| B07 | "Two hands rotate at different speeds, relative angle changes — that relative phase is observable" | ✓ | Ch.4: "All dynamics live in the relative phases between energy eigenstates." |
| B08 | "Cross terms survive because the two phases are different, oscillate at the beat frequency" | ✓ | Ch.4: beat frequency (E_m - E_n)/hbar from interference of e^{-iE_m t/hbar} and e^{-iE_n t/hbar} |
| B09 | "A single energy eigenstate has no second hand to make a relative phase against itself" | ✓ | Ch.4: "A single eigenstate has no relative phase — that is why it is stationary." |
| B10 | "Particle in a box, 50-50 superposition sloshes at (E2-E1)/hbar" | ✓ (illustrative) | Ch.4: beat frequency = (E_m - E_n)/hbar, labeled illustrative |

## Terms table

| term | debut beat | prior beat creating need |
|------|-----------|--------------------------|
| phase | B02 | B01 (hook: stationary but secretly spinning) |
| global phase | B05 | B04 (question: why does spinning phase not show up?) |
| beat frequency | B08 | B07 (two hands at different rates, relative angle changing) |

## Exclusions confirmed
- No time-evolution-operator derivation on screen ✓
- No spectral-theorem formalism ✓
- No Bohr-frequency algebra ✓

## Illustrative numbers
- B10: particle in a box, E1/E2 energies, 50-50 superposition — labeled illustrative
