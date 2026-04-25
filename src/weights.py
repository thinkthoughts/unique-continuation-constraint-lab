# src/weights.py

import numpy as np


# --- basic grids ---

def make_grid(xmin=-6, xmax=6, n=4000):
    x = np.linspace(xmin, xmax, n)
    dx = x[1] - x[0]
    return x, dx


# --- core functions ---

def gaussian(x, width=1.0, center=0.0, amplitude=1.0):
    return amplitude * np.exp(-((x - center) ** 2) / (2 * width ** 2))


def normalize(u):
    m = np.max(np.abs(u))
    return u if m == 0 else u / m


# --- differential operators ---

def gradient(u, x):
    return np.gradient(u, x)


def laplacian(u, x):
    return np.gradient(np.gradient(u, x), x)


# --- integration ---

def integrate(u, x):
    return np.trapz(u, x)


# --- weights (core of repo) ---

def decay_weight(x, alpha=0.2):
    return np.exp(alpha * x**2)


def carleman_weight(x, tau=0.2):
    return np.exp(tau * x**2)


# --- measures (PDE-aligned) ---

def decay_measure(u, x, alpha=0.2):
    w = decay_weight(x, alpha)
    return integrate(w * u**2, x)


def carleman_measure(u, x, tau=0.2):
    w = carleman_weight(x, tau)
    return integrate(w * u**2, x)


def hardy_variation(u, x):
    g = gradient(u, x)
    return integrate(g**2, x)


def curvature_measure(u, x):
    lap = laplacian(u, x)
    return integrate(lap**2, x)
