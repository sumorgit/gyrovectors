from typing import Tuple

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib import patches
from matplotlib import pyplot as plt

import numpy as np

from gyrovectors import Array
from gyrovectors.backend import AbstractBack
from gyrovectors.gyroline import get_gyroline_value


def init_circle_figure(s: float, **kwargs) -> Tuple[Figure, Axes]:
    """Intializes the figure and plots the circle

    Args:
        s (float): radius of the ball

    Returns:
        A tuple (fig, ax) with a plot of the s-radius circle centerd on (0,0)
    """
    fig, ax = plt.subplots()

    bound = patches.Circle((0, 0), s, fill=False, **kwargs)
    ax.add_patch(bound)

    ax.set_xlim(-s, s)
    ax.set_ylim(-s, s)
    ax.set_aspect("equal")
    return fig, ax


def plot_gyroline(
    start: Array,
    end: Array,
    radius: float,
    back: AbstractBack,
    N: int,
    fig: Figure,
    ax: Axes,
    **kwargs,
) -> Tuple[Figure, Axes]:
    """Computes and plot the gyroline between two points

    Args:
        start (Array): first extremity of the gyroline
        end (Array): second extremity of the gyroline
        radius (float): radius of the ball
        back (AbstractBack): backend used for calculation
        N (int): number of points drawn

    Returns:
        A tuple (fig, ax) with a plot of the gyroline between start and end
    """

    T = np.linspace(0, 1, N)
    gyroline_values = np.empty([N, 2], dtype=np.float32)

    for i, t in enumerate(T):
        value = get_gyroline_value(start, end, t, radius, back)
        gyroline_values[i] = value

    ax.scatter(gyroline_values[..., 0], gyroline_values[..., 1], **kwargs)

    return fig, ax
