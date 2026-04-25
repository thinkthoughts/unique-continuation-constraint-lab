"""Hardy-specific finite-grid demo functions."""

from __future__ import annotations

import numpy as np

try:
    from .weights import gaussian, gradient, integrate
except ImportError:
    from weights import gaussian, gradient, integrate


def hardy_weight(x, eps: float = 0.12):
    """Regularized Hardy weight 1/(x^2 + eps)."""
    return 1.0 / (x**2 + eps)


def concentration_measure(u, x, eps: float = 0.12):
    """Finite-grid concentration proxy."""
    w = hardy_weight(x, eps=eps)
    return integrate(w * np.abs(u)**2, x)


def variation_cost(u, x):
    """Finite-grid variation-cost proxy."""
    g = gradient(u, x)
    return integrate(np.abs(g)**2, x)


def hardy_pair(u, x, eps: float = 0.12):
    """Return concentration and variation cost."""
    return {
        "concentration": concentration_measure(u, x, eps=eps),
        "variation_cost": variation_cost(u, x),
    }


def width_sweep(x, widths, eps: float = 0.12, amplitude: float = 1.0):
    """Sweep Gaussian width and compute concentration + variation cost."""
    concentration = []
    variation = []
    for width in widths:
        u = gaussian(x, width=width, amplitude=amplitude)
        concentration.append(concentration_measure(u, x, eps=eps))
        variation.append(variation_cost(u, x))
    return {
        "widths": np.asarray(widths),
        "concentration": np.asarray(concentration),
        "variation_cost": np.asarray(variation),
    }
