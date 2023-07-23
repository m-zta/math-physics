import numpy as np
import matplotlib.pyplot as plt

def L(x, n):
    if n > 0:
        return 1 / np.pi * n / ((x)**2 + n**2)
    elif n <= 0:
        return 0

def g(x, a):
    return np.where(np.abs(x) <= a, 1/(2*a), 0)

def main():
    x = np.linspace(-21, 21, 1000)

    for n in np.linspace(2, 0.1, 200):
        a = 3 # x-value of the peak of the dirac delta function
        y = L(x - a, n)
        plt.plot(x, y)
        plt.ylim(-0.1, 10.1)
        plt.title(f'Graph of the function L(x - {a}, {n:.2f})')
        plt.draw()
        plt.pause(0.01)
        plt.clf()

    plt.show() # Keeps the plot open until the user closes it

if __name__ == '__main__':
    main()