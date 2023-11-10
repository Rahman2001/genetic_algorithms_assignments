from matplotlib import pyplot as plt
from numpy.random.mtrand import rand


def random_search(objective_func, bounds, n_iterations, dimension):
    best = [bounds[:, 0] + rand() * (bounds[:, 1] - bounds[:, 0])]
    obtained_as_best = []
    iter_time = []

    # sample 0f 100 inputs
    candidate_sol = bounds[:, 0] + rand(n_iterations) * (bounds[:, 1] - bounds[:, 0])

    for candidate in range(candidate_sol.size):
        S = objective_func([candidate_sol[candidate]], dimension=dimension)
        iter_time.append(candidate)
        if S > best:
            best = S
        obtained_as_best.append(best)

    plt.plot(iter_time, obtained_as_best)
    plt.xlabel("Iteration time")
    plt.ylabel("Obtained as best")
    plt.show()
    return best
