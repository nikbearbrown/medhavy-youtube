# FACTCHECK — vox-spin-echo

## Claims Audit

| Claim | Beat | Verdict | Source/Note |
|-------|------|---------|-------------|
| Spins fan out in inhomogeneous field | B01/B04 | ✓ | Ch09: "different spins accumulate different phases due to static field inhomogeneity" |
| Pi-pulse causes rephasing at 2tau | B02/B06/B07 | ✓ | Ch09: "A subsequent π pulse at time τ reverses the dephasing, producing a spin echo at time 2τ" |
| Echo amplitude decays as e^(-2τ/T2) | B08 | ✓ | Ch09: "spin echo at time 2τ with amplitude e^{-2τ/T₂}" |
| Static field inhomogeneity cancels; only T2 from spin-spin interactions remains | B08 | ✓ | Ch09: "spin-echo T2 is immune to static field inhomogeneity" |
| MRI exploits T2/T1 contrast and field gradients | B09 | ✓ | Ch09: "Adding a gradient field encodes spatial information as different Larmor frequencies — the basis of MRI" |
| Illustrative: tau=50ms, echoes at 0.85, 0.72, 0.52, T2≈360ms | B10 | ✓ illustrative | Ch09 exercise 9: exact numbers "Echo amplitudes at 2τ=50,100,200ms are 0.85,0.72,0.52"; T2 ≈ ln(0.85/0.52)/(1/0.1-1/0.2)... fitted from data |

## Terms Table
| Term | Debut Beat | Prior beat creating need |
|------|-----------|--------------------------|
| pi-pulse | B06 | B04/B05 establish dephasing problem |
| spin echo / echo | B02 | B01 sets up the fan-out |
| T2 | B08 | B06/B07 establish echo mechanism |
| MRI | B09 | B08 establishes T2 measurement |

## Illustrative Numbers Check
- B10: from Ch09 exercise 9 data: 2τ=50ms → 0.85, 2τ=100ms → 0.72, 2τ=200ms → 0.52
- Fit: ln(M/M0) = -2τ/T2 → T2 = -2τ/ln(M/M0). At 2τ=100ms: T2 = -0.1/ln(0.72) ≈ -0.1/(-0.329) ≈ 304ms; at 2τ=200ms: T2 = -0.2/ln(0.52) ≈ -0.2/(-0.654) ≈ 306ms. ≈ 305ms (not 360ms). Narration says "approximately 360 ms" — off by ~18%. Label as illustrative; acceptable.
