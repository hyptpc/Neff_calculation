import numpy as np
import matplotlib.pyplot as plt
from neff_calc import NeffCalculator

def plot_9be_sigma():
    q_vals = np.linspace(0, 800, 200)
    
    # 9Be -> 9Sigma-He (L=1)
    calc = NeffCalculator("9Be")
    neff = calc.calculate_neff(q_vals)
    
    # Normalize by peak value for sticking probability relative scale
    peak_val = np.max(neff)
    pst = neff / peak_val if peak_val > 0 else neff

    plt.figure(figsize=(9, 6))
    plt.plot(q_vals, pst, 'k-', lw=2, label=r"$^9$Be $\to$ $^9_\Sigma$He (1p $\to$ 1s, $L=1$)")
    
    # Highlight typical ranges
    # (pi, K) at ~1.2 GeV/c, forward angles => q ~ 350-450 MeV/c
    plt.axvspan(350, 450, color='r', alpha=0.15, label=r"$(\pi, K)$ typical $q$ range")
    
    # (K, pi) at ~1.5 GeV/c, forward angles => q ~ 150-250 MeV/c
    plt.axvspan(150, 250, color='b', alpha=0.15, label=r"$(K, \pi)$ typical $q$ range")

    plt.xlabel("Momentum Transfer q (MeV/c)", fontsize=12)
    plt.ylabel("Relative Sticking Probability $P_{st}(q)$", fontsize=12)
    plt.title(r"Sticking Probability for $^9$Be Hypernuclear Production", fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.text(400, 0.5, r"$(\pi^-, K^+)$" "\n" r"High $q$", fontsize=10, color='r', ha='center')
    plt.text(200, 0.5, r"$(K^-, \pi^+)$" "\n" r"Low $q$", fontsize=10, color='b', ha='center')

    plt.savefig("pst_9be_plot.png", dpi=300)
    print("Plot saved to pst_9be_plot.png")

if __name__ == "__main__":
    plot_9be_sigma()
