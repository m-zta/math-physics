import numpy as np
import matplotlib.pyplot as plt

# Fourier series

def init_coefficients(c):
    n = len(c)
    I = 1.0

    c[0] = I / 2.0

    for k in range(1, n):
        if (k % 2) == 1:
            I = 1.0
            c[k] = 2.0 * I / (np.pi * k)


def main():
    x = np.linspace(0, 4 * np.pi, 1000)
    y = np.zeros_like(x)

    # coefficients
    c = np.zeros(50)
    init_coefficients(c)

    for i in range(len(c)):
        y += c[i] * np.sin(i * x)


    plt.plot(x, y, color='#6413dd')
    plt.grid()
    plt.title('Fourier Series')
    plt.show()


if __name__ == '__main__':
    main()

