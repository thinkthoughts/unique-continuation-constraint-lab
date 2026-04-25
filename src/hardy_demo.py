# src/hardy_demo.py

import numpy as np

from .weights import gaussian, gradient, integrate


def hardy_weight(x, eps=0.12):
    """
    Regularized Hardy weight.

    Uses 1 / (x^2 + eps) instead of 1 / x^2 so finite-grid
    demonstrations remain stable near x = 0.
    """
    return 1.0 / (x**2 + eps)


def concentration_measure(u, x, eps=0.12):
    """
    Finite-grid concentration proxy:

        ∫ |u(x)|² / (x² + eps) dx
    """
    w = hardy_weight(x, eps=eps)
    return integrate(w * np.abs(u)**2, x)


def variation_cost(u, x):
    """
    Finite-grid variation proxy:

        ∫ |∇u(x)|² dx
    """
    g = gradient(u, x)
    return integrate(np.abs(g)**2, x)


def hardy_pair(u, x, eps=0.12):
    """
    Return both Hardy-style quantities:
    concentration and variation cost.
    """
    return {
        "concentration": concentration_measure(u, x, eps=eps),
        "variation_cost": variation_cost(u, x),
    }


def width_sweep(x, widths, eps=0.12, amplitude=1.0):
    """
    Sweep Gaussian width and compute concentration + variation cost.

    Smaller width means stronger localization.
    """
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


def normalize_series(y):
    """
    Normalize a 1D array to max absolute value.
    """
    y = np.asarray(y)
    m = np.max(np.abs(y))
    return y if m == 0 else y / m
