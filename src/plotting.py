# src/plotting.py

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


# --- global style ---

def set_style():
    plt.rcParams.update({
        "figure.figsize": (10, 4.8),
        "font.size": 12,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def save(fig, path, dpi=180):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")


# --- helpers ---

def normalize(y):
    m = np.max(np.abs(y))
    return y if m == 0 else y / m


# --- common plots used in repo ---

def plot_profiles(x, profiles, labels, title=None):
    """
    profiles: list of arrays
    labels: list of strings
    """
    fig, ax = plt.subplots()

    for u, lab in zip(profiles, labels):
        ax.plot(x, normalize(u), linewidth=2.4, label=lab)

    ax.set_xlabel("space coordinate x")
    ax.set_ylabel("normalized amplitude")

    if title:
        ax.set_title(title, fontsize=16)

    ax.legend(frameon=True)
    plt.tight_layout()
    return fig, ax


def plot_gradient_overlay(x, u, grad_u, title=None):
    fig, ax = plt.subplots()

    ax.plot(x, normalize(u), linewidth=2.5, label="profile")
    ax.plot(x, normalize(np.abs(grad_u)), linestyle="--", linewidth=2.2, label="|gradient|")

    ax.set_xlabel("x")
    ax.set_ylabel("normalized value")

    if title:
        ax.set_title(title, fontsize=16)

    ax.legend(frameon=True)
    plt.tight_layout()
    return fig, ax


def plot_bar_comparison(labels, series, series_labels, title=None):
    """
    series: list of lists (values)
    series_labels: names of each bar group
    """
    x = np.arange(len(labels))
    width = 0.25

    fig, ax = plt.subplots()

    for i, vals in enumerate(series):
        ax.bar(x + (i - (len(series)-1)/2) * width, vals, width=width, label=series_labels[i])

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("normalized value")

    if title:
        ax.set_title(title, fontsize=16)

    ax.legend(frameon=True)
    plt.tight_layout()
    return fig, ax


def plot_log_bars(labels, values, title=None):
    fig, ax = plt.subplots()

    ax.bar(labels, values)
    ax.set_yscale("log")
    ax.set_ylabel("log scale")

    if title:
        ax.set_title(title, fontsize=16)

    plt.tight_layout()
    return fig, ax
