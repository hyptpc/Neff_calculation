import numpy as np
import matplotlib.pyplot as plt
from neff_calc import NeffCalculator

def plot_fig6_equivalent():
    # 4He calculation
    calc_he4 = NeffCalculator("4He")
    q_vals = np.linspace(0, 600, 100)
    neff_he4 = calc_he4.calculate_neff(q_vals)
    
    # 12C calculation (as an example of scalability)
    calc_c12 = NeffCalculator("12C")
    neff_c12 = calc_c12.calculate_neff(q_vals)

    # Normalize by the peak value to avoid division by zero
    val_he4 = neff_he4[0] if neff_he4[0] > 0 else 1.0
    neff_he4_norm = neff_he4 / val_he4
    
    peak_c12 = np.max(neff_c12) if np.max(neff_c12) > 0 else 1.0
    neff_c12_norm = neff_c12 / peak_c12

    plt.figure(figsize=(8, 6))
    plt.plot(q_vals, neff_he4_norm, label=r"$^4$He ($1s \to 1s$)", lw=2)
    plt.plot(q_vals, neff_c12_norm, label=r"$^{12}$C ($1p \to 1s$, Peak Norm.)", lw=2, linestyle='--')
    
    plt.xlabel("Momentum Transfer q (MeV/c)", fontsize=12)
    plt.ylabel("Relative Effective Nucleon Number N_eff(q)", fontsize=12)
    plt.title("Effective Nucleon Number (PWIA, HO wave functions)", fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig("neff_plot.png", dpi=300)
    print("Plot saved to neff_plot.png")

if __name__ == "__main__":
    plot_fig6_equivalent()
