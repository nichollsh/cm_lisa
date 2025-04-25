#!/usr/bin/env python3

# Based on the demo from:
# https://matplotlib.org/stable/gallery/color/colormap_reference.html
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import lisa  # import the package to register the colormaps


def demo():

    # Create figure and adjust figure height to number of colormaps
    cmap_list = lisa.list_cmaps()
    nrows = len(cmap_list)
    figh = 1.0 + (nrows + (nrows-1)*0.1)*0.22

    fig, axs = plt.subplots(nrows=nrows, ncols=2, figsize=(6, figh))
    fig.subplots_adjust(hspace=0.2, wspace=0.05)

    axs[0,0].set_title("Discrete", fontsize=12)
    axs[0,1].set_title("Continuous", fontsize=12)

    for i in range(len(cmap_list)):
        cmap_name = cmap_list[i]

        # Add text
        ax = axs[i,0]
        ax.text(-.04, .5, cmap_name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)


        # Plot colormap discretely
        gradient = np.linspace(0, 1, len(lisa.lisa._palettes[cmap_name]))
        gradient = np.vstack((gradient, gradient))
        ax.imshow(gradient, aspect='auto', cmap=cmap_name)

        # Continuous
        ax = axs[i,1]
        gradient = np.linspace(0, 1, 256)
        gradient = np.vstack((gradient, gradient))
        ax.imshow(gradient, aspect='auto', cmap=cmap_name)


    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax[0].set_axis_off()
        ax[1].set_axis_off()

    # Save figure
    for ext in ["png", "pdf", "svg"]:
        fpath = f"lisa.{ext}"
        print(f"Saving figure to {fpath}")
        fig.savefig(fpath, dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    print("Demoing lisa colormaps")
    demo()
