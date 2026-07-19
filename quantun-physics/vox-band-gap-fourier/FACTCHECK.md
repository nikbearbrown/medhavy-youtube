# FACTCHECK — vox-band-gap-fourier

## B03 — Free electron parabola and zone boundary crossing
- E = hbar^2 k^2 / 2m: CORRECT (free electron dispersion).
- Parabola repeats shifted by G = 2pi/a: CORRECT (Bloch theorem / extended zone scheme).
- At k = pi/a (first Brillouin zone boundary), two parabolas cross and are degenerate: CORRECT.

## B04 — Periodic potential Fourier expansion
- V(x+a) = V(x) → V(x) = sum_n V_n e^{i*2*pi*n*x/a}: CORRECT.
- V_1 oscillates once per unit cell: CORRECT.
- V_1 matches the momentum difference between the degenerate pair at the zone boundary (2pi/a): CORRECT.

## B05 — Selection rule for scattering
- Periodic potential scatters k to k+G_n where G_n = 2pi*n/a: CORRECT.
- Only V_1 couples the degenerate pair (k = pi/a and k-2pi/a = -pi/a) at the first zone boundary: CORRECT.

## B06 — 2x2 matrix and gap
- H matrix in degenerate subspace: diagonal = E_k^0 (free), off-diagonal = V_1: CORRECT.
- Eigenvalues = E_k^0 ± |V_1|: CORRECT.
- Gap = 2|V_1|: CORRECT (standard nearly-free electron result, e.g., Griffiths QM Ch. 5, Kittel Solid State Ch. 7).

## B08 — Higher zone boundaries
- n-th zone boundary controlled by V_n: CORRECT.
- Fourier components are orthogonal — each Vn couples only the n-th degenerate pair: CORRECT.

## B09 — Numerical example
- a = 0.3 nm, V_1 = -0.4 eV → gap = 2 × 0.4 = 0.8 eV: CORRECT arithmetic.

VERDICT: All facts verified. The nearly-free electron result gap = 2|V_1| is a standard result. The Fourier selection argument is correct.
