"""Core finite-grid weights and PDE-style measures.

This module keeps the notebooks small by centralizing:
- grids
- Gaussian candidate profiles
- decay / Carleman weights
- finite-difference derivatives
- weighted norm and variation measures
"""

from __future__ import annotations

import numpy as np


def make_grid(xmin: float = -6.0, xmax: float = 6.0, n: int = 4000):
    """Return a 1D grid and spacing."""
    x = np.linspace(xmin, xmax, n)
    dx = x[1] - x[0]
    return x, dx


def gaussian(x, center: float = 0.0, width: float = 1.0, amplitude: float = 1.0):
    """Gaussian candidate profile."""
    width = max(float(width), 1e-12)
    return amplitude * np.exp(-((x - center) ** 2) / (2 * width ** 2))


def normalize(u):
    """Normalize by max absolute value without changing an all-zero array."""
    m = np.max(np.abs(u))
    return u if m == 0 else u / m


def gradient(u, x):
    """Finite-difference gradient."""
    return np.gradient(u, x)


def laplacian(u, x):
    """Finite-difference 1D Laplacian."""
    return np.gradient(np.gradient(u, x), x)


def integrate(y, x):
    """Finite-grid integral."""
    return np.trapz(y, x)


def gaussian_decay_envelope(x, C: float = 1.0, a: float = 0.4):
    """Gaussian envelope C exp(-a |x|^2)."""
    return C * np.exp(-a * x**2)


def decay_weight(x, alpha: float = 0.2):
    """Growth weight for testing Gaussian decay."""
    return np.exp(alpha * x**2)


def carleman_weight(x, tau: float = 0.2, center: float = 0.0, normalize_weight: bool = False):
    """Simple exponential Carleman-style weight."""
    w = np.exp(tau * (x - center) ** 2)
    if normalize_weight:
        m = np.max(np.abs(w))
        return w if m == 0 else w / m
    return w


def bounded_weight_lens(x, tau: float = 0.22, floor: float = 0.45, height: float = 0.70):
    """Readable bounded weighting lens for visualization."""
    return floor + height * np.exp(-tau * x**2)


def weighted_signal(u, w):
    """Apply a weight to a candidate profile."""
    return w * u


def decay_measure(u, x, alpha: float = 0.2):
    """Finite-grid decay-weighted L2 measure."""
    w = decay_weight(x, alpha=alpha)
    return integrate(w * np.abs(u)**2, x)


def carleman_measure(u, x, tau: float = 0.2):
    """Finite-grid Carleman-weighted L2 measure."""
    w = carleman_weight(x, tau=tau)
    return integrate(w * np.abs(u)**2, x)


def hardy_variation(u, x):
    """Finite-grid gradient / variation cost."""
    g = gradient(u, x)
    return integrate(np.abs(g)**2, x)


def curvature_measure(u, x):
    """Finite-grid curvature proxy."""
    lap = laplacian(u, x)
    return integrate(np.abs(lap)**2, x)
