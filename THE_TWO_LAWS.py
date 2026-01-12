"""
THE TWO LAWS (RAW DEFINITIONS)
==============================
These are the exact operational formulas used to validate the 
Semantic Tolerance Theory across N=200 datasets.
"""

import numpy as np

def law_1_physical_entropy(R, eta=0.38, R0=0.20):
    """
    THE PHYSICAL LAW (ENTROPY DOMINANCE)
    ------------------------------------
    Describes information collapse in systems lacking internal structure
    (Physical/Inert Regime).
    
    Formula: I(R) = eta * R * (1 - exp(-R/R0))
    
    Where:
    - R:   Noise Ratio (sigma / sigma_max)
    - I:   Remaining Semantic Information (0-1)
    - eta: Efficiency Factor (Empirical ~0.38 for unstructured data)
    - R0:  Scale Constant (Empirical ~0.20)
    """
    return eta * R * (1 - np.exp(-R / R0))


def law_2_metaphysical_safety(Margin_M):
    """
    THE METAPHYSICAL LAW (SEMANTIC TOLERANCE)
    -----------------------------------------
    Predicts the Critical Noise Threshold (Sigma_c) based on Geometric Margin
    (Metaphysical/Structured Regime).
    
    Formula: Sigma_c = 2 * (M - 1.5)
    
    Where:
    - M:       Geometric Margin (R_dmax or Class Separation)
    - Sigma_c: Critical Noise limit before semantic collapse
    - 1.5:     The Phase Transition Threshold (Empirical Constant)
    
    Condition:
    - If M < 1.5: System is Physical (Inert). Sigma_c = 0 (No resistance).
    - If M > 1.5: System is Metaphysical (Structured). Resistance scales linearly with M.
    """
    # The Safety Formula
    sigma_c = 2.0 * (Margin_M - 1.5)
    
    # Clip at 0 (Cannot have negative resistance)
    return np.maximum(sigma_c, 0.0)


def classify_regime(Margin_M):
    """
    THE REGIME CLASSIFIER
    ---------------------
    Determines if a system is Physical or Metaphysical.
    """
    if Margin_M > 1.5:
        return "Metaphysical (Structured)"
    else:
        return "Physical (Inert)"
