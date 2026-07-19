# FACTCHECK — vox-spin-720

Source: `quantum-mechanics-vol2/chapters/07-spin-and-the-bloch-sphere.md`

---

## Claims checked

**B01 — "Rotate an electron's state by 360 degrees and it comes back as the negative of itself. Only after 720 degrees is it truly home."**
PASS. Ch.07 §"The half-angle also carries a deeper meaning": "a $2\pi$ rotation that returns every ordinary vector to where it started sends a spinor to its negative. Only after a full $4\pi$ rotation does the state come back to itself."

**B02 — "A normal vector rotated 360 degrees is identical to where it started. An electron's spin state picks up a minus sign after exactly one full turn. Expectation values don't change, but the state itself does."**
PASS. Ch.07: the state acquires an overall minus sign under $2\pi$, but all probabilities (which are squared moduli) are unchanged. Expectation values depend on probabilities, so they are unaffected.

**B03 — "Neutron interferometry measured this. At 360 degrees, the two beams destructively interfere. At 720 degrees, they constructively interfere again."**
PASS. Ch.07 §references: "Rauch et al. (1975) and Werner et al. (1975) confirmed this directly with neutron interferometry." The interference minimum at $2\pi$ and return at $4\pi$ is the experimental signature described in these papers.

**B04 — "Every physical quantity you can measure is unchanged by the sign flip — probabilities square the amplitude."**
PASS. $|\!-\!\psi\rangle$ gives identical Born-rule probabilities to $|\psi\rangle$ for all observables. Standard QM; consistent with Ch.07.

**B06 — "The general state is cos(theta/2) times spin-up plus a phase times sin(theta/2) times spin-down."**
PASS. Ch.07 eq. (7.2) (standard Bloch parameterization): $|\psi\rangle = \cos(\theta/2)|\uparrow\rangle + e^{i\phi}\sin(\theta/2)|\downarrow\rangle$.

**B07 — "Rotating the physical axis by theta means theta goes to theta plus 2pi. The half-angle goes from theta/2 to theta/2 + pi. Cosine of theta/2 + pi equals negative cosine of theta/2."**
PASS. Ch.07: "Then $\theta$ advances to $\theta + 2\pi$, and $\cos(\theta/2)$ becomes $\cos(\theta/2 + \pi) = -\cos(\theta/2)$, so the spin state picks up an overall minus sign."

**B08 — "Minus-psi and psi give identical probabilities. In interference with an unflipped reference beam, the minus sign shows up as a pi phase shift — destructive interference."**
PASS. Standard quantum mechanics. The global phase between the two arms of the interferometer produces the observable interference contrast.

**B09 — "Ordinary three-dimensional rotations form SO(3). Spin-half states live in SU(2), which wraps around SO(3) twice. Every ordinary rotation corresponds to two spin-half operations."**
PASS. Ch.07: "This is the spinor double cover: spin states live in $\mathrm{SU}(2)$, which wraps around the ordinary rotation group $\mathrm{SO}(3)$ twice."

**B11 endcard — "Half-angle in state → 360 deg flips sign. Sign invisible alone → real in interference. 720 deg restores the state."**
PASS. All three facts verified above.

---

## Exclusions honored

- No SU(2)/SO(3) group theory derivation on screen (B09 names the groups without developing them)
- No Pauli-exponential derivation
- No interferometer optics detail (beam splitters, paths not described beyond "two paths")

---

VERDICT: PASS
