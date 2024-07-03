import numpy as np
from matplotlib import pyplot as plt

'''
Euler's method is a simple numerical method to solve ordinary differential equations (ODEs) with a given initial value.
It is based on the idea of approximating the curve by a sequence of line segments.
'''


def f(x):
    '''
    The function f(x) = x^2
    '''
    return x ** 2


def f_prime(x):
    '''
    The derivative of f(x) = x^2 is f'(x) = 2x
    '''
    return 2 * x


def main():
    a = -5
    b = 5
    m = 100

    x_fine = np.linspace(a, b, m + 1)
    y_f = f(x_fine)
    plt.plot(x_fine, y_f, 'b-')

    h = 1.2 # step size

    x_coarse = [a]
    y_approx = [f(a)]

    while (x_coarse[-1] + h <= b):
        y_approx.append(y_approx[-1] + h * f_prime(x_coarse[-1]))
        x_coarse.append(x_coarse[-1] + h)

    plt.plot(x_coarse, y_approx, 'r-')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
