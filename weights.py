"""Carleman-weight toy functions for visualization notebooks."""

import numpy as np

def gaussian(x, center=0.0, width=1.0, amplitude=1.0):
    return amplitude * np.exp(-((x - center) ** 2) / (2 * width ** 2))

def carleman_weight(x, tau=1.0, center=0.0):
    return np.exp(tau * (x - center) ** 2)

def weighted_signal(u, weight):
    return u * weight
