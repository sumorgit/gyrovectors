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

    # Initialize plot
    fig, ax = init_circle_figure(radius)
    legends = ["boundary"]

    ax.scatter(0, 0, c="black")
    legends.append("Center")

    # Initialize points
    a = np.array([0.0, 0.5])
    b = np.array([0.8, -0.2])
    supp = np.array([0.05, 0.05])

    # Plot a and b
    ax.scatter(a[0], a[1], c="b")
    legends.append("A")
    ax.scatter(b[0], b[1], c="r")
    legends.append("B")

    # At each iteration, we perform one addition and one multiplication
    W = np.empty((n_iterations, 2), np.float32)
    W[0] = mob_add(a, supp, radius, back)
    X = np.empty((n_iterations, 2), np.float32)
    X[0] = mob_multiply(mult_factor, a, radius, back)

    for i in range(1, n_iterations):
        W[i] = mob_add(W[i - 1], supp, radius, back)
        X[i] = mob_multiply(mult_factor, X[i - 1], radius, back)

    # Plot the additions and multiplications
    ax.scatter(W[..., 0], W[..., 1], c="orange", s=2)
    legends.append("Addition")

    ax.scatter(X[..., 0], X[..., 1], c="cyan", s=2)
    legends.append("Multiplication")

    # Plot the gyroline between a and b
    fig, ax = plot_gyroline(a, b, radius, back, 70, fig, ax, color="pink", s=2)

    plt.legend(legends)
    plt.show()


if __name__ == "__main__":
    main()
