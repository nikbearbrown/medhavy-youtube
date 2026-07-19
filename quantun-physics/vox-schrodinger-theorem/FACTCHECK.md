# FACTCHECK — vox-schrodinger-theorem

## Claims audit

| beat | claim | verdict | source |
|------|-------|---------|--------|
| B02 | "Total probability of finding the particle somewhere must always equal one" | ✓ | Ch.4: "probability is conserved. The norm of the state cannot change." |
| B03 | "That requirement constrains time evolution to be a unitary operator" | ✓ | Ch.4: "U-dagger U = I: the time-evolution operator must be unitary" |
| B06 | "U-dagger U = I, the definition of a unitary operator" | ✓ | Ch.4: exact statement |
| B07 | "Unitarity forces the generator to be Hermitian" | ✓ | Ch.4: "Unitarity to first order requires H-dagger = H: the generator must be Hermitian" |
| B07 | "Hermitian eigenvalues are real — those are the energies" | ✓ | Standard: Hermitian operators have real eigenvalues (Ch.4 implies) |
| B08 | "Compose N infinitesimal unitary steps: get e^{-iHt/hbar}" | ✓ | Ch.4: "composing infinitesimal steps gives the matrix exponential U(t) = e^{-iHt/hbar}" |
| B09 | "Differentiate the exponential with respect to time: get i h-bar d/dt psi = H psi" | ✓ | Ch.4: "Differentiate |psi(t)> = U(t)|psi(0)>... i hbar d/dt |psi> = H|psi>" |
| B09 | "The Schrodinger equation is the derivative of unitarity" | ✓ | Ch.4: "It is the statement that U(t) satisfies its own differential equation." |
| B10 | "Because H must be Hermitian, measured energies are real numbers" | ✓ | Standard consequence of Hermitian operators |
| B11 | Student derives the Schrodinger equation from probability conservation alone | illustrative | Consistent with Ch.4; labeled illustrative |

## Terms table

| term | debut beat | prior beat creating need |
|------|-----------|--------------------------|
| unitary | B06 | B05 (postulate framing hides a derivable chain — what does the constraint look like mathematically?) |
| Hermitian | B07 | B06 (unitarity established, need to characterize the generator) |

## Exclusions confirmed
- No interaction-picture detour ✓
- No path-integral derivation ✓
- No Stone's theorem ✓
- No Hamiltonian in curved spacetime ✓

## Illustrative numbers
- B11: student scenario is purely illustrative, no invented numbers beyond the derivation steps.
