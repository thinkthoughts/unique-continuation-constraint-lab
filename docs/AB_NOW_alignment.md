# AB ↔ NOW Alignment

This document maps standard PDE proof language ("AB") to the repo’s explanatory layer ("NOW / lift5").

## Core pipeline

| Step | AB (standard) | NOW / lift5 |
|------|---------------|------------|
| two-time decay | Gaussian decay at t₁, t₂ | sister-diagonal constraint input |
| Carleman weight | exponential weighted norm | same math · new scale |
| Hardy inequality | ∫|u|²/|x|² ≤ C∫|∇u|² | concentration pays variation cost |
| contradiction | incompatible estimates | constraints cannot all hold simultaneously |
| zero solution | u ≡ 0 | only the zero solution remains |

## Interpretation

- AB = analytical structure (paper, literature)
- NOW = explanatory layer (notebooks, figures)
- Alignment means:
  - no change to the mathematical content
  - only a change in how structure is observed

## Scope

This mapping:
- preserves the standard argument (see EKPV, Tao)
- supports the figures and notebooks
- does not introduce new mathematical claims
