import numpy as np
from scipy.integrate import quad
from scipy.special import spherical_jn, factorial2
from scipy.optimize import root_scalar

class PhysicalConstants:
    """Basic physical constants and conversion factors."""
    HBARC = 197.327 # MeV*fm
    M_P = 938.272   # Proton mass (MeV/c^2)
    M_N = 939.565   # Neutron mass (MeV/c^2)
    M_L = 1115.683  # Lambda mass (MeV/c^2)
    M_S = 1197.449  # Sigma- mass (MeV/c^2)
    M_PI = 139.570  # Charged pion mass (MeV/c^2)
    M_K = 493.677   # Charged kaon mass (MeV/c^2)

def harmonic_oscillator_wf(r, n, l, b):
    """
    Radial wave function for Harmonic Oscillator.
    Normalized as \int_0^\infty r^2 dr |phi(r)|^2 = 1.
    For 1s (n=0, l=0): phi(r) = 2/(pi^1/4 * b^3/2) * exp(-r^2/(2b^2))
    """
    if n == 0 and l == 0:
        norm = 2.0 / (np.pi**0.25 * b**1.5)
        return norm * np.exp(-r**2 / (2.0 * b**2))
    elif n == 0 and l == 1:
        # Example for 1p state
        norm = np.sqrt(8.0 / (3.0 * np.pi**0.5 * b**5))
        return norm * r * np.exp(-r**2 / (2.0 * b**2))
    else:
        # Generic formula can be implemented if needed
        raise NotImplementedError("General (n,l) HO not yet implemented")

class NeffCalculator:
    def __init__(self, target_name="4He"):
        self.target_name = target_name
        self.constants = PhysicalConstants()
        
        # Configure target-specific parameters
        if target_name == "4He":
            self.m_target = 3727.379 # MeV (4He mass)
            self.m_core = 2808.391   # MeV (3H mass for p->L reaction)
            self.b_n = 1.535 # fm (Nucleon size parameter from paper)
            self.b_l = 2.233 # fm (Lambda size parameter from paper)
            self.n_n, self.l_n = 0, 0 # 1s
            self.n_l, self.l_l = 0, 0 # 1s
            self.L_transfer = 0
        elif target_name == "9Be":
            # 9Be -> 9Sigma-He (or Li depending on reaction)
            # p (1p3/2) -> Sigma (1s1/2) => L=1
            self.m_target = 8392.748 # MeV
            self.m_core = 7471.328   # MeV (8Li for p->Sigma reaction)
            self.b_n = 1.7 # fm (Default for Be, can be adjusted)
            self.b_l = 1.7 # fm
            self.n_n, self.l_n = 0, 1 # 1p
            self.n_l, self.l_l = 0, 0 # 1s
            self.L_transfer = 1
        elif target_name == "12C":
            self.m_target = 11174.86 # MeV
            self.m_core = 10252.54   # MeV (11B)
            self.b_n = 1.64
            self.b_l = 1.64
            # Usually p-shell for 12C
            self.n_n, self.l_n = 0, 1 # 1p
            self.n_l, self.l_l = 0, 0 # 1s (for ground state)
            self.L_transfer = 1
        else:
            raise ValueError(f"Unknown target: {target_name}")

    def form_factor(self, q_mev):
        """Calculate the radial integral F(q)."""
        q_fm = q_mev / self.constants.HBARC
        
        # Recoil factor q' = q * (M_core / M_target)
        q_prime = q_fm * (self.m_core / self.m_target)
        
        def integrand(r):
            phi_n = harmonic_oscillator_wf(r, self.n_n, self.l_n, self.b_n)
            phi_l = harmonic_oscillator_wf(r, self.n_l, self.l_l, self.b_l)
            jl = spherical_jn(self.L_transfer, q_prime * r)
            return r**2 * phi_l * phi_n * jl
        
        # Integrate from 0 to large enough infinity (e.g. 10*b)
        result, error = quad(integrand, 0, 20.0)
        return result

    def calculate_neff(self, q_list):
        """Calculate relative Neff for a list of q values."""
        results = []
        for q in q_list:
            ff = self.form_factor(q)
            results.append(ff**2)
        return np.array(results)

if __name__ == "__main__":
    # Quick test for 4He
    calc = NeffCalculator("4He")
    q_vals = np.linspace(0, 500, 50)
    neff = calc.calculate_neff(q_vals)
    print("q (MeV/c), Neff (Relative)")
    for i in range(0, len(q_vals), 10):
        print(f"{q_vals[i]:.1f}, {neff[i]:.4f}")
