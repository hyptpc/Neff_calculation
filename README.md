# Calculation of Effective Nucleon Number $N_{\text{eff}}(q)$

We have implemented a PWIA-based calculation for $N_{\text{eff}}(q)$ as described in Phys. Rev. C 100, 024605.

## Results

![N_eff vs q Plot](/Users/ichikawayuudai/.gemini/antigravity/brain/09c4a848-e9c6-4f8c-aecc-6503690cc8b7/neff_plot.png)

### Key Observations:
- **$^4$He ($1s \to 1s$):** The effective nucleon number is maximum at $q=0$ and decays as a Gaussian $\sim e^{-q^2 b^2 / 2}$, which is consistent with Figure 6(a) in the paper.
- **$^{12}$C ($1p \to 1s$):** For transitions with $\Delta \ell = 1$, the form factor is zero at $q=0$ and peaks at approximately $q \approx 250$ MeV/c. This demonstrates the code's ability to handle different quantum numbers.

---

## $^9$Be $\to$ $^9_\Sigma$He Transition Results

We also implemented the calculation for $^9\text{Be}(\pi^-, K^+)$ and $(K^-, \pi^+)$ reactions.

![Sticking Probability Plot for 9Be Sigma](/Users/ichikawayuudai/.gemini/antigravity/brain/09c4a848-e9c6-4f8c-aecc-6503690cc8b7/pst_9be_plot.png)

### Key Observations for $^9$Be:
- **Transition Type ($1p \to 1s$)**: Unlike the $s \to s$ case in $^4\text{He}$, this is a $p \to s$ transition ($L=1$).
- **Zero Peak**: As expected for $L=1$, the sticking probability is **zero at $q=0$** and peaks at approximately $q \approx 200$ MeV/c.
- **Reaction Comparison**:
  - **$(K^-, \pi^+)$**: Operates at lower $q$ (forward angles), where $P_{st}$ is significantly higher (closer to the peak).
  - **$(\pi^-, K^+)$**: Operates at higher $q$ ($400 \sim 500$ MeV/c), where $P_{st}$ has already decayed significantly. This explains why the "sticking" is generally harder in $(\pi, K)$ than in forward $(K, \pi)$.

---

## Implementation Details

The implementation is split into two main parts:

### 1. [neff_calc.py](file:///Users/ichikawayuudai/Work/Eff_NucleonNum/neff_calc.py)
This script contains the `NeffCalculator` class which:
- Uses Harmonic Oscillator radial wave functions.
- Performs numerical integration of the form factor $F(q) = \int r^2 dr \phi_\Lambda \phi_N j_L(q'r)$.
- Handles the recoil factor $M_C/M_A$.

### 2. [plot_neff_simple.py](file:///Users/ichikawayuudai/Work/Eff_NucleonNum/plot_neff_simple.py)
A wrapper script that calculates $N_{\text{eff}}$ for multiple $q$ values and generates the comparison plot.

---

## How to use for other nuclei
To calculate for a new target, you only need to add an entry to the `NeffCalculator` class constructor with:
- Target and Core masses.
- Size parameters $b$ (fm).
- Quantum numbers $(n, \ell)$ for the initial and final states.
- Transferred angular momentum $L$.

> [!TIP]
> The current code uses a virtual environment in `./venv`. To run the scripts manually:
> ```bash
> source venv/bin/activate
> python3 plot_neff_simple.py
> ```
