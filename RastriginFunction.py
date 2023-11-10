
import math

import numpy as np
from pymoo.problems import get_problem
from pymoo.visualization.fitness_landscape import FitnessLandscape


def show_plot_rastrigin():

    # from https://pymoo.org/problems/single/rastrigin.html
    # the Rastrigin function has range -5.12 < x < 5.12
    # The more x gets closer to maximum value, the more result will be closer to the global maxima.

    # n_var means "dimension"
    problem = get_problem("rastrigin", n_var=2)

    FitnessLandscape(problem, _type="surface").show()

    # the plot from the top
    FitnessLandscape(problem, _type="contour", colorbar=True).show()

def rastrigin(X, **kwargs):
    A = 10
    dimension = kwargs.get('dimension', 2)
    return A*dimension + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X])

