import numpy as np
import matplotlib.pyplot as plt
from neff_calc import NeffCalculator

def plot_fig6_reproduce():
    q_vals = np.linspace(0, 800, 100)
    
    # 1. Standard calculation (with recoil 0.75, paper b values)
    calc = NeffCalculator("4He")
    neff_with_recoil = calc.calculate_neff(q_vals) * 2.0 # Z=2
    
    # 2. Calculation without recoil (M_C/M_A = 1.0)
    # Temporarily override recoil logic for comparison
    original_m_core = calc.m_core
    calc.m_core = calc.m_target # Forces M_C/M_A = 1.0
    neff_no_recoil = calc.calculate_neff(q_vals) * 2.0
    calc.m_core = original_m_core # Restore
    
    # 3. Add CM Correction factor to the "with recoil" case
    # f_cm = exp(q^2 * b^2 / (4A))
    q_fm = q_vals / 197.327
    b_avg = (calc.b_n + calc.b_l) / 2.0
    f_cm = np.exp( (q_fm**2 * b_avg**2) / (4.0 * 4.0) )
    neff_cm_corr = neff_with_recoil * (f_cm**2)

    plt.figure(figsize=(7, 8))
    plt.semilogy(q_vals, neff_no_recoil, 'k--', label="PWIA (No Recoil, $M_C/M_A=1$)")
    plt.semilogy(q_vals, neff_with_recoil, 'b-', label="PWIA (With Recoil, $M_C/M_A=0.75$)")
    plt.semilogy(q_vals, neff_cm_corr, 'r:', label="PWIA (With Recoil + CM Corr)")
    
    plt.ylim(1e-5, 5)
    plt.xlim(0, 800)
    plt.xlabel("Momentum Transfer q (MeV/c)", fontsize=12)
    plt.ylabel("Effective Nucleon Number $N_{eff}$", fontsize=12)
    plt.title(r"$^4$He($\pi^+$, $K^+$)$^4_\Lambda$He $N_{eff}$ (Log Scale)", fontsize=14)
    plt.grid(True, which="both", alpha=0.3)
    plt.legend()
    
    plt.savefig("neff_log_plot.png", dpi=300)
    print("Log plot saved to neff_log_plot.png")

if __name__ == "__main__":
    plot_fig6_reproduce()
