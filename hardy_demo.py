"""Toy Hardy-style concentration / variation-cost proxies."""

import numpy as np

def concentration_proxy(width):
    width = np.asarray(width)
    return 1.0 / (1.0 + width)

def gradient_cost_proxy(width):
    width = np.asarray(width)
    return 1.0 / np.maximum(width, 1e-9)
