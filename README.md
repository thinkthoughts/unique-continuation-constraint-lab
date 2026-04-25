# unique-continuation-constraint-lab

Constraint-based visualization of Schrödinger unique continuation.

**same math · lifted clarity**

---

## 🔗 Start here

👉 https://cosineconstraint.app/colab/2026_04_24_schrodinger_unique_continuation_pipeline.html

This page is the primary entry point:
- full constraint pipeline
- diagrams (decay → weight → Hardy → contradiction → zero solution)
- aligned with standard PDE structure

---

## 🧠 What this repo does

This repo presents **standard unique continuation results** for Schrödinger equations as a **constraint-aligned pipeline**:

```
two-time decay
→ Carleman weight
→ Hardy-type inequality
→ contradiction
→ zero solution
```

No new mathematics is proposed.

The goal is to:
- preserve the original proofs
- make structure easier to follow
- support entry-level → advanced readers

---

## 📦 Contents

```
notebooks/
  02_unique_continuation_pipeline.ipynb

figures/
  uc_pipeline_v3_standard_vs_now.png
  step1_two_time_decay.png
  step2_exponential_weight.png
  step3_hardy_variation_cost.png
  step4_ab_now_alignment.png

docs/
  glossary.md
```

---

## 🔬 Mathematical context

We follow the classical result (Escauriaza–Kenig–Ponce–Vega):

i∂ₜu = −Δu + V(x)u

If:

|u(x,t₁)|, |u(x,t₂)| ≤ Ce^{-a|x|²}

for sufficiently large a, then:

u(x,t) ≡ 0

---

## 🧩 Key idea

Instead of presenting the proof only symbolically, we show:

- how decay interacts with constraints
- how weights amplify structure
- how Hardy-type bounds restrict concentration
- why non-zero solutions cannot satisfy all constraints

Result:

Only the zero solution remains under all constraints.

---

## 🧠 Language note

This repo introduces a light translation layer:

- extend (step) → structure persists across steps  
- resist (collapse) → structure survives constraints  

These are interpretive aids, not replacements for standard terminology.

---

## 🚀 Next steps

- expand to higher-order and variable-coefficient Schrödinger
- add full paper (paper/main.tex)
- connect to additional PDE seminars

---

## 📬 Contact

If anything looks incorrect or unclear, corrections are welcome.

---

**same math · lifted clarity**
