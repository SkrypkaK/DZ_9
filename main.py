import matplotlib.pyplot as plt
import numpy as np

from src.homework import cool_piecewise_function


def plot_my_cool_function():
    x_values = np.linspace(-10, 5, 500)
    y_values = [cool_piecewise_function(x) for x in x_values]

    fig, ax = plt.subplots()
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(x_values, y_values)
    plt.show()


if __name__ == '__main__':
    plot_my_cool_function()
