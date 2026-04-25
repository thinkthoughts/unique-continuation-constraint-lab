"""Shared plotting helpers for unique-continuation-constraint-lab."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def set_style():
    """Apply shared Matplotlib styling."""
    plt.rcParams.update({
        "figure.figsize": (10, 4.8),
        "font.size": 12,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def ensure_fig_dir(path="figures"):
    """Return a figure directory, supporting repo-root and notebooks/ execution."""
    candidates = [Path("../figures"), Path(path)]
    for candidate in candidates:
        if candidate.exists():
            candidate.mkdir(parents=True, exist_ok=True)
            return candidate
    candidates[0].mkdir(parents=True, exist_ok=True)
    return candidates[0]


def save(fig, path, dpi: int = 180):
    """Save a figure with consistent settings."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")


def add_caption(ax, text, y=-0.22):
    """Add a consistent caption box below an axis."""
    ax.text(
        0.02, y, text,
        transform=ax.transAxes,
        fontsize=11,
        color="0.25",
        bbox=dict(boxstyle="round,pad=0.45", fc="white", ec="0.75"),
    )


def plot_alignment_bars(labels, scores, title, target=0.96):
    """Plot local CGCS alignment bars."""
    gate_45 = 1 / np.sqrt(2)
    fig, ax = plt.subplots(figsize=(10, 4.8))
    bars = ax.bar(labels, scores)
    ax.axhline(target, linestyle="--", linewidth=2, label="max-CGCS target 0.96")
    ax.axhline(gate_45, linestyle=":", linewidth=2, label=r"45° gate $1/\sqrt{1^2+1^2}$")

    for bar, score in zip(bars, scores):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            score + 0.015,
            f"{score:.3f}",
            ha="center",
            va="bottom",
            fontsize=11,
        )

    ax.set_ylim(0, 1.05)
    ax.set_ylabel("local CGCS")
    ax.set_title(title, fontsize=18, pad=14)
    ax.legend(loc="lower right")
    return fig, ax
