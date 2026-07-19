# FACTCHECK — vox-spin-measurement

## B03 — Pauli matrices and eigenstates
- sigma_z = diag(1,-1): CORRECT.
- sigma_x off-diagonal (0,1;1,0): CORRECT.
- |up_z> = (1,0) is eigenstate of sigma_z with eigenvalue +1: CORRECT.
- |+x> = (1/sqrt(2))(1,1) is eigenstate of sigma_x with eigenvalue +1: CORRECT.

## B04 — Superposition structure
- |up_z> written in x-basis: |up_z> = (1/sqrt(2))|+x> + (1/sqrt(2))|−x>: CORRECT.
- After projecting to |+x>, z-measurement gives 50/50: CORRECT.

## B05 — Commutator
- [sigma_x, sigma_z] = sigma_x*sigma_z - sigma_z*sigma_x: 
  sigma_x*sigma_z = [[0,1],[1,0]]*[[1,0],[0,-1]] = [[0,-1],[1,0]]
  sigma_z*sigma_x = [[1,0],[0,-1]]*[[0,1],[1,0]] = [[0,1],[-1,0]]
  [sigma_x, sigma_z] = [[0,-1],[1,0]] - [[0,1],[-1,0]] = [[0,-2],[2,0]] = -2i*[[0,i],[i,0]]... 
  Actually: [sigma_x, sigma_z] = 2i*epsilon_{xzy}*sigma_y = 2i*(-1)*sigma_y = -2i*sigma_y.
  From the commutation relation [sigma_i, sigma_j] = 2i*eps_{ijk}*sigma_k:
  [sigma_x, sigma_z] = 2i*eps_{xzy}*sigma_y = 2i*(-1)*sigma_y = -2i*sigma_y. CORRECT.
- Non-zero commutator means no shared eigenbasis: CORRECT.

## B06 — Bloch sphere picture
- |up_z> at north pole of Bloch sphere: CORRECT.
- x-measurement projects to equator (±x points): CORRECT.
- Equatorial states give 50/50 for z-measurement: CORRECT (expectation value of sigma_z in equatorial state is 0).

## B08 — Quantum cryptography connection
- Measuring in wrong basis introduces detectable errors in BB84 protocol: CORRECT.
- Non-commutativity is the physical basis for QKD security: CORRECT.

## B09 — Sequential measurement probabilities
- Start in |up_z>. P(+x) = |<+x|up_z>|^2 = |(1/sqrt(2))|^2 = 1/2: CORRECT.
- After collapse to |+x>, P(+z) = |<up_z|+x>|^2 = 1/2: CORRECT.

VERDICT: All facts verified. The Pauli commutation relations, eigenstates, and Bloch sphere picture are all standard. The quantum cryptography application is correctly described.
