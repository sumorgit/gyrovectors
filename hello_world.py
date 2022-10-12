from matplotlib import pyplot as plt
import numpy as np

from gyrovectors.backend import get_backend
from gyrovectors.linalg import mob_add, mob_multiply
from gyrovectors.plots import init_circle_figure, plot_gyroline


def main():

    # Select backend, other backend are not installed by default
    back = get_backend("numpy")

    # Hyperparameters
    radius = 1  # radius of the circle
    n_iterations = 100  # number of times the operations are applied
    mult_factor = 1.1  # factor by which we want to multiply

    init_size = 20  # plotting only, initial size of the points

    # Initialize plot
    fig, ax = init_circle_figure(radius)
    ax.scatter(0, 0, c="black")

    # Initialize points
    a = np.array([0.0, 0.5])
    b = np.array([0.8, -0.2])
    supp = np.array([0.05, 0.05])

    # Plot a and b
    ax.scatter(a[0], a[1], c="b")
    ax.scatter(b[0], b[1], c="r")

    # At each iteration, we perform one addition and one multiplication
    w = mob_add(a, supp, radius, back)
    ax.scatter(w[0], w[1], c="orange", s=init_size)

    x = mob_multiply(mult_factor, a, radius, back)
    ax.scatter(x[0], x[1], c="cyan", s=init_size)

    for i in range(2, n_iterations + 1):
        w = mob_add(w, supp, radius, back)
        ax.scatter(w[0], w[1], c="orange", s=init_size / i)

        x = mob_multiply(mult_factor, x, radius, back)
        ax.scatter(x[0], x[1], c="cyan", s=init_size / i)

    # Plot the gyroline between a and b
    fig, ax = plot_gyroline(a, b, radius, back, 70, fig, ax, color="pink", s=2)

    plt.show()


if __name__ == "__main__":
    main()
