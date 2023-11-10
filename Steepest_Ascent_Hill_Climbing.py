import numpy as np
from matplotlib import pyplot as plt
from numpy.random.mtrand import randn, rand


# hill climbing local search algorithm
def hill_climbing(objective_func, bounds, n_iterations, step_size, dimension):
    # get x and y variables for plot
    obtaining_maxima = []
    iter_time = []

    # generate an initial point by choosing random point in the given bounds
    initial_solution = [bounds[:, 0] + rand() * (bounds[:, 1] - bounds[:, 0])]
    print("This is initial_solution: ", initial_solution)

    # evaluate the initial point
    initial_solution_eval = objective_func(initial_solution, dimension=dimension)
    # run the hill climb
    for i in range(n_iterations):

        candidate_solution = []
        for _ in range(dimension*2-1):
            solution = initial_solution[0]
            potential_candidate = (solution + randn() * step_size)

            # check if random guess does not overstep the boundaries of function
            for bound in bounds:
                if bound < 0 & potential_candidate < 0 & potential_candidate < bound:
                    while potential_candidate < bound:
                        potential_candidate = (solution + randn() * step_size)

                if bound > 0 & potential_candidate >= 0 & potential_candidate > bound:
                    while potential_candidate > bound:
                        potential_candidate = (solution + randn() * step_size)

            candidate_solution.append(potential_candidate)

        print("These are potential candidate solutions: ", candidate_solution)
        candidate_solution = choose_best_candidate(candidate_solution, objective_function=objective_func,
                                                   dimension=dimension)
        print("This is chosen candidate_solution: ", candidate_solution)
        # evaluate candidate point
        candidate_eval = [objective_func(candidate_solution, dimension=dimension)]
        # check if we should keep the new point
        print("This is candidate eval: ", candidate_eval)
        print("This is initial_solution_eval: ", initial_solution_eval)
        if candidate_eval[0] > initial_solution_eval[0]:

            # store the new point
            initial_solution, initial_solution_eval = candidate_solution, candidate_eval
            # report progress
            print('>%d_iteration, updated initial_sols (%s) = %.5f (initial_sol_eval)\n' %
                  (i, initial_solution, initial_solution_eval[0]))

        obtaining_maxima.append(initial_solution_eval)
        iter_time.append(i)

    plt.plot(iter_time, obtaining_maxima)
    plt.xlabel("Iteration time")
    plt.ylabel("Obtained values of maxima")
    plt.show()
    return [initial_solution, initial_solution_eval]

def choose_best_candidate(candidates, objective_function, dimension):
    best = np.array([-10000])
    for candidate in candidates:
        temp = np.array([objective_function(candidate, dimension=dimension)])
        print(temp)
        if temp[0] > best[0]:
            best = np.array(candidate)
    return [best]
