# unique-continuation-constraint-lab

Constraint-based visualization and notebooks for unique continuation in Schrödinger equations.

**same math · lifted clarity**

---

## Start here

Web bridge note:

https://cosineconstraint.app/colab/2026_04_24_schrodinger_unique_continuation_pipeline.html

This repo turns that after-seminar bridge into a reproducible lab structure:

```text
two-time decay
→ Carleman weight
→ Hardy-type inequality
→ AB-NOW alignment
→ contradiction
→ zero solution
```

No new mathematics is claimed here. The goal is to preserve the standard proof structure while making the pipeline easier to inspect, reproduce, and eventually write up as an arXiv5867-ready paper.

---

## Repo structure

```text
unique-continuation-constraint-lab/
  README.md
  paper/
    main.tex
    references.bib
    sections/
      01_intro.tex
      02_theorem_and_assumptions.tex
      03_carleman_weights.tex
      04_hardy_type_inequalities.tex
      05_contradiction_chain.tex
      06_cgcs_translation.tex
  notebooks/
    01_decay_weight_visualization.ipynb
    02_hardy_gate_demo.ipynb
    03_contradiction_pipeline.ipynb
  src/
    weights.py
    hardy_demo.py
    plotting.py
  figures/
    uc_pipeline_v3_standard_vs_now.png
    step1_two_time_decay.png
    step2_exponential_weight.png
    step3_hardy_variation_cost.png
    step4_ab_now_alignment.png
  docs/
    glossary.md
    AB_NOW_alignment.md
```

---

## Core mathematical context

Classical model:

\[
i\partial_t u = -\Delta u + V(x)u.
\]

Two-time decay assumption:

\[
|u(x,t_1)|, |u(x,t_2)| \le C e^{-a|x|^2}.
\]

For sufficiently strong decay under the theorem hypotheses:

\[
u(x,t) \equiv 0.
\]

---

## Language note

This repo uses a light CGCS translation layer:

- **expand**: initial spread of structure
- **extend (step)**: continue one step across the pipeline
- **resist (collapse)**: survive constraint pressure without contradiction

These are interpretive aids. Standard PDE language remains primary.

---

## Current status

- [x] after-seminar bridge page
- [x] Notebook 02 proof-aligned pipeline
- [x] figure set planned
- [ ] dedicated notebooks split by step
- [ ] full paper draft
- [ ] references filled from standard sources

---

**same math · lifted clarity**
