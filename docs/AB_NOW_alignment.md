# AB ↔ NOW Alignment

This document maps standard PDE proof language ("AB") to the explanatory layer used in this repo ("NOW / lift5").

## Constraint pipeline

| Step | AB (standard PDE) | NOW / lift5 |
|------|------------------|-------------|
| decay | Gaussian decay at two times | sister-diagonal constraint input |
| weight | Carleman-weighted norm | same math · new scale |
| variation | Hardy-type inequality | concentration pays variation cost |
| contradiction | incompatible estimates | constraints cannot all hold simultaneously |
| conclusion | u ≡ 0 | only the zero solution remains |

## Interpretation

- **AB** = analytical structure (paper, literature)
- **NOW** = computational / visual layer (notebooks, figures)

Alignment means:
- same mathematical content
- same logical order
- different presentation (observable vs symbolic)

## Scope

This mapping:
- follows classical arguments (e.g. EKPV, Tao)
- supports the figure pipeline (Steps 1–5)
- does not introduce new mathematical claims
