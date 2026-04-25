"""Shared plotting helpers."""

import matplotlib.pyplot as plt

def savefig(path):
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
