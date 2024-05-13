import numpy as np
import matplotlib.pyplot as plt


# Different representations of the Dirac delta function


def L(x, h):
    """Lorentzian curve with half-width h"""
    return np.where(h > 0, 1 / np.pi * h / (x ** 2 + h ** 2), 0)


def G(x, h):
    """Gaussian curve with standard deviation h"""
    return np.where(np.abs(x) <= h, 1 / (2 * h), 0)


def main():
    x = np.linspace(-21, 21, 1000)

    for n in np.linspace(1, 0.05, 100):
        a = 3  # x-value of the peak of the dirac delta function
        y = L(x - a, n)
        plt.plot(x, y, 'r-')
        plt.ylim(-0.1, 10.1)
        plt.grid(True)
        plt.title(f'Graph of the function L(x - {a}, {n:.2f})')
        plt.draw()
        plt.pause(0.01)
        plt.clf()

    plt.show()  # Keeps the plot open until the user closes it


if __name__ == '__main__':
    main()
