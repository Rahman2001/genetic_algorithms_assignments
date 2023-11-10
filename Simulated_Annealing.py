import random
from math import exp

from matplotlib import pyplot as plt
from numpy.random.mtrand import rand, randn


def simulated_annealing(objective, bounds, n_iterations, step_size, temp, dimension):
    iter_time = []
    obtained_maxima = []

    # generate an initial point
    # we use Gaussian distribution for random number generation
    best = [bounds[:, 0] + rand() * (bounds[:, 1] - bounds[:, 0])]
    # evaluate the initial point
    best_eval = objective(best, dimension=dimension)
    # current working solution
    curr, curr_eval = best, best_eval
    # run the algorithm
    for i in range(n_iterations):
        # take a step
        candidate_solution = curr[0] + randn() * step_size
        candidate_solution = check_for_bounds(candidate_solution, bounds=bounds, initial_solution=curr, step_size=step_size)
        # evaluate candidate_solution point
        candidate_eval = objective(candidate_solution, dimension=dimension)
        print("This is candidate_solution %s and candidate_eval %s " % (candidate_solution, candidate_eval))
        # check for new best solution
        if candidate_eval[0] > best_eval[0]:
            # store new best point
            best, best_eval = candidate_solution, candidate_eval
            # report progress
            print("This is best %s and best_eval %s " % (best, best_eval))

        # difference between candidate_solution and current point evaluation
        diff = candidate_eval[0] - curr_eval[0]
        # calculate temperature for current epoch
        t = temp / float(i + 1)
        # calculate metropolis acceptance criterion
        metropolis = exp(-diff / t)
        # check if we should keep the new point
        # since we are looking for maxima, difference should be higher otherwise we rely on probabilistic dicision.
        if diff > 0 or rand() > metropolis:
            # store the new current point
            curr, curr_eval = candidate_solution, candidate_eval
            print("This is curr %s and curr_eval %s " % (curr, curr_eval))
        iter_time.append(i)
        obtained_maxima.append(best_eval)

    plt.plot(iter_time, obtained_maxima)
    plt.xlabel("Iteration time")
    plt.ylabel("Obtained value of maxima")
    plt.show()
    return [best, best_eval]

def check_for_bounds(candidate_solution, **kwargs):
    bounds = kwargs.get('bounds')
    initial_solution = kwargs.get('initial_solution')
    step_size = kwargs.get('step_size')

    # check for bounds (usually it oversteps the bounds when step size get bigger for ex.: x = 0.8)
    for bound in bounds[0, :]:
        if 0 > bound > candidate_solution[0]:
            while candidate_solution[0] < bound:
                candidate_solution = (initial_solution[0] + randn() * random.uniform(0, 1))

        if 0 < bound < candidate_solution[0]:
            while candidate_solution[0] > bound:
                candidate_solution = (initial_solution[0] + randn() * random.uniform(0, 1))

    return [candidate_solution]