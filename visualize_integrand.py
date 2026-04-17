import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spherical_jn
from neff_calc import NeffCalculator, harmonic_oscillator_wf, PhysicalConstants

def visualize():
    calc = NeffCalculator("4He")
    constants = PhysicalConstants()
    r = np.linspace(0, 10, 500)
    
    # 1. Radial Wave Functions
    phi_n = harmonic_oscillator_wf(r, calc.n_n, calc.l_n, calc.b_n)
    phi_l = harmonic_oscillator_wf(r, calc.n_l, calc.l_l, calc.b_l)
    
    # 2. Setup plotting
    fig, axes = plt.subplots(3, 1, figsize=(8, 12), sharex=True)
    
    # Plot 1: Wave Functions
    axes[0].plot(r, phi_n, label=fr"Nucleon $\phi_N$ (b={calc.b_n} fm)", lw=2)
    axes[0].plot(r, phi_l, label=fr"$\Lambda$ $\phi_\Lambda$ (b={calc.b_l} fm)", lw=2)
    axes[0].set_ylabel("Wave Function $\phi(r)$")
    axes[0].set_title("1. Radial Wave Functions (Harmonic Oscillator)")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Plot 2: Bessel Functions for different q
    q_test = [0, 200, 400] # MeV/c
    q_recoil = [q / constants.HBARC * (calc.m_core / calc.m_target) for q in q_test]
    
    colors = ['black', 'blue', 'red']
    for q, qr, c in zip(q_test, q_recoil, colors):
        jl = spherical_jn(calc.L_transfer, qr * r)
        axes[1].plot(r, jl, label=f"q = {q} MeV/c", color=c, lw=2)
    axes[1].set_ylabel(f"Bessel Function $j_{calc.L_transfer}(q'r)$")
    axes[1].set_title(f"2. Spherical Bessel Function (order L={calc.L_transfer})")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    # Plot 3: The Integrand (r^2 * phi_n * phi_l * jl)
    for q, qr, c in zip(q_test, q_recoil, colors):
        jl = spherical_jn(calc.L_transfer, qr * r)
        integrand = r**2 * phi_n * phi_l * jl
        area = np.trapz(integrand, r) # Numerical integral for label
        axes[2].plot(r, integrand, label=f"q = {q} MeV/c (Area={area:.3f})", color=c, lw=2)
        axes[2].fill_between(r, integrand, color=c, alpha=0.1)
        
    axes[2].set_xlabel("Radius r (fm)")
    axes[2].set_ylabel("Integrand $r^2 \phi_N \phi_\Lambda j_L$")
    axes[2].set_title("3. The Integrand (The area under these curves = Form Factor F(q))")
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("integrand_visual.png", dpi=300)
    print("Visualization saved to integrand_visual.png")

if __name__ == "__main__":
    visualize()
