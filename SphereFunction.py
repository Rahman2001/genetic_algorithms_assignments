from numpy.array_api import asarray
from pymoo.problems import get_problem
from pymoo.visualization.fitness_landscape import FitnessLandscape


def sphere(X, **kwargs):
    return sum([(x**2) for x in X])

def show_plot_sphere():
    # from https://pymoo.org/problems/single/rastrigin.html
    # the Rastrigin function has range -5.12 < x < 5.12
    # The more x gets closer to maximum value, the more result will be closer to the global maxima.

    # n_var means "dimension"
    problem = get_problem("sphere", n_var=2)

    FitnessLandscape(problem, _type="surface", bounds=[[-5.12, 5.12]]).show()

    # the plot from the top
    FitnessLandscape(problem, _type="contour", colorbar=True).show()