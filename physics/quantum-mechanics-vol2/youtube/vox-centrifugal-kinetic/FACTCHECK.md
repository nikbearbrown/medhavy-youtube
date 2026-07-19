# FACTCHECK — vox-centrifugal-kinetic

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01–B03 | Centrifugal barrier repels electron from nucleus, sits on potential side, has shape of potential | ✓ | Ch.05: V_eff = V(r) + ℏ²ℓ(ℓ+1)/2mr²; term diverges at r=0, falls as 1/r² |
| B02 | For s-orbital (ℓ=0), centrifugal term vanishes | ✓ | ℏ²·0·1/2mr² = 0 when ℓ=0 |
| B06 | 3D kinetic energy splits into radial + angular L²/2mr² | ✓ | Ch.05: T = T_radial + L²/2mr²; standard separation in spherical coords |
| B07 | L² eigenvalue is ℏ²ℓ(ℓ+1); angular KE becomes ℏ²ℓ(ℓ+1)/2mr² | ✓ | Ch.05: L²|ℓm⟩ = ℏ²ℓ(ℓ+1)|ℓm⟩; plugging in gives the centrifugal term |
| B08 | After rearranging radial equation, KE term sits on V(r) side | ✓ | Ch.05: "V_eff = V(r) + ℏ²ℓ(ℓ+1)/(2mr²)" — centrifugal term added to potential |
| B08 | The repulsion is the cost of spinning: electron can't get close without more angular KE | ✓ (framing) | Ch.05: "It pushes probability away from the origin" — mechanism is rotational KE |
| B09 | Bigger ℓ → higher floor in V_eff → larger characteristic radius | ✓ | Ch.05 effective potential plots (Fig 5.3): higher ℓ shifts minimum outward |
| B08–B09 | "Centrifugal term is not a force, it is kinetic" | ✓ | Ch.05 verbatim: "The centrifugal term is not a force pushing the electron outward. It is a kinetic energy contribution — specifically, the angular kinetic energy L̂²/2mr² evaluated in an eigenstate of L̂²." |

## Terms table

| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| centrifugal barrier | B01 | — (hook) |
| effective potential V_eff | B03 | B02 (two terms shown side by side) |
| radial equation | B05 | B04 (THE QUESTION frames it) |
| L²/2mr² / angular kinetic energy | B06 | B05 (need for mechanism established) |
| separation of variables | B06 | B06 (mechanism explanation) |
| ℓ(ℓ+1) eigenvalue | B07 | B06 (operator projected) |
