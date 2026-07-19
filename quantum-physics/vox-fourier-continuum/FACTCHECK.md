# FACTCHECK — vox-fourier-continuum

## B03 — Allowed wavenumbers in a box
- For Dirichlet boundary conditions (standing waves): k_n = n*pi/L, n=1,2,...
- For periodic boundary conditions: k_n = 2*pi*n/L, n=0,±1,±2,...
- Spacing: delta_k = pi/L (Dirichlet) or 2*pi/L (periodic).
- The film uses delta_k = pi/L (Dirichlet). CORRECT for particle-in-a-box.

## B06 — Sum to integral transition
- Fourier series: f(x) = sum_n c_n * e^{i*k_n*x}, spacing delta_k = pi/L.
- As L→∞, delta_k→0, and sum_n c_n (...) * delta_k → integral.
- The Fourier transform: f(x) = (1/2pi) * integral phi(k) * e^{ikx} dk. CORRECT.
- The coefficient c_n = (L/2pi) * phi(k_n): the density of modes factor. CORRECT.

## B07 — QM connection: discrete vs continuous spectrum
- Bound states (finite box/well): discrete allowed energies E_n = (hbar*k_n)^2/(2m). CORRECT.
- Free particle: continuous spectrum E(k) = (hbar*k)^2/(2m) for all real k. CORRECT.

## B09 — Numerical example
- L=1m: delta_k = pi/1 = 3.14 per meter. CORRECT.
- L=10m: delta_k = pi/10 = 0.314 per meter ≈ 0.31/m. CORRECT.
- L=1000m: delta_k = pi/1000 = 0.00314/m ≈ 0.003/m. CORRECT.
- L→∞: delta_k→0. CORRECT.

VERDICT: All facts verified. The L→∞ limit turning discrete sums into continuous integrals is a standard result in Fourier analysis and quantum mechanics.
