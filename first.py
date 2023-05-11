import matplotlib.pyplot as plt
import numpy as np


def make_graph(a_coeffs, b_coeffs, c_coeffs, d_coeffs):
    """Построение графика"""
    # Данные
    x = np.linspace(-2, 2)
    ys = []
    for i in range(len(lst)):
        
    y1 = x**3
    y2 = 1.2 - 0.4 * x

    fig, ax = plt.subplots()

    # Добавление графиков
    ax.plot(x, y1, color="red")
    ax.plot(x, y2, color="blue")

    # Сетка
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.grid()

    plt.show()


if __name__ == "__main__":
    make_graph()
