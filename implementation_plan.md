# Implementation Plan - 9Be(pi-, K+) and (K-, pi+) Sigma Hypernuclei

This plan extends the current $N_{\text{eff}}$ calculation to support the $^9\text{Be}$ target and the production of $\Sigma$ hypernuclei, as described in [AIP Conf. Proc. 2319, 100005 (2021)](https://doi.org/10.1063/5.0037113).

## Goal
1. Support $^9\text{Be} \to {}^9_\Sigma\text{He}$ transition ($1p_{3/2} \to 1s_{1/2}$, $L=1$).
2. Compare Sticking Probability ($\propto N_{\text{eff}}$) for $(\pi^-, K^+)$ and $(K^-, \pi^+)$ reactions.
3. Handle $\Sigma^-$ mass and $^9\text{Be}$ specific size parameters.

## Proposed Approach

### 1. Physics for $^9\text{Be} \to {}^9_\Sigma\text{He}$
- **Initial state**: $1p$ nucleon in $^9\text{Be}$ ($n=0, \ell=1$).
- **Final state**: $1s$ Sigma in $^9_\Sigma\text{He}$ ($n=0, \ell=0$).
- **Transferred angular momentum**: $L=1$ (due to $p \to s$ transition).
- **Size parameters**: Typically $b \approx 1.6 \sim 1.7$ fm for $^9\text{Be}$.
- **Masses**:
  - $M(^{9}\text{Be}) \approx 8392.7$ MeV
  - $M(^{8}\text{Li}) \approx 7471.3$ MeV (Core)
  - $M(\Sigma^-) \approx 1197.4$ MeV

### 2. Implementation Updates
- **`neff_calc.py`**:
  - Add $n=0, \ell=1$ to `harmonic_oscillator_wf`.
  - Add `9Be` configuration to `NeffCalculator`.
  - Support automatic $L$ selection based on $\ell_N$ and $\ell_\Lambda$.
- **`plot_9be_sigma.py`**:
  - New script to plot $N_{\text{eff}}(q)$ for the $L=1$ case.
  - Highlight the relevant $q$ ranges for $(\pi, K)$ and $(K, \pi)$.

## Verification Plan
- Check that $N_{\text{eff}}(0) = 0$ for $L=1$ transitions.
- Compare the peak value position with theoretical expectations ($q \approx \sqrt{L}/b$).

## Open Questions
- **Size Parameter**: Does the paper 100005_1_online.pdf specify a particular $b$ value for $^9\text{Be}$? (I will use $1.7$ fm as a default if not specified).
- **Normalization**: Since $^9\text{Be}$ has 4 protons, should we set the overall factor to $Z=4$ or focus on the relative sticking probability?
