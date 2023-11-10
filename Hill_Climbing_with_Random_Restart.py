import random

from matplotlib import pyplot as plt
from numpy.random.mtrand import rand, randn


def hill_climbing_with_random_restart(objective_func, bounds, n_iterations, step_size, dimension):
    obtained_sol = []
    iter_time = []
    line_number = 1
    # choose initial point in the given bounds
    initial_solution = [bounds[:, 0] + rand() * (bounds[:, 1] - bounds[:, 0])]

    # evaluate the initial point
    initial_solution_eval = objective_func(initial_solution, dimension=dimension)

    for i in range(n_iterations):

        candidate_solution = (initial_solution[0] + randn() * step_size)
        candidate_solution = check_for_bounds(candidate_solution, bounds=bounds,
                                              initial_solution=initial_solution, step_size=step_size)

        print("This is candidate solution: ", candidate_solution)

        # evaluate candidate point
        candidate_eval = objective_func(candidate_solution, dimension=dimension)

        print("This is candidate eval: ", candidate_eval)
        print("This is initial_solution_eval: ", initial_solution_eval)

        print('This is outer plot [iter_time] %s and [obtained_sol] %s: ' % (iter_time, obtained_sol))

        if candidate_eval[0] > initial_solution_eval[0]:

            # store the new point
            initial_solution, initial_solution_eval = candidate_solution, candidate_eval

            print('>%d_iteration, updated initial_sols (%s) = %.5f (initial_sol_eval)\n' %
                  (i, initial_solution, initial_solution_eval[0]))

        else:
            # hill_climbing has 3 chances/iterations to get better candidate solution
            # otherwise random restart will be performed
            for j in range(50):
                candidate_solution = (initial_solution[0] + randn() * step_size)
                candidate_solution = check_for_bounds(candidate_solution, bounds=bounds,
                                                      initial_solution=initial_solution, step_size=step_size)
                candidate_eval = objective_func(candidate_solution, dimension=dimension)

                if candidate_eval[0] >= initial_solution_eval[0]:
                    # iter_time.append(i)
                    # obtained_sol.append(candidate_eval[0])

                    initial_solution, initial_solution_eval = candidate_solution, candidate_eval

                    print("This is new candidate solution and evaluation: %s %s" % (candidate_solution, candidate_eval))
                    print('>%d_iteration_chance, updated initial_sol (%s) = %.5f (initial_sol_eval)\n' %
                          (j, initial_solution, initial_solution_eval[0]))
                    break

            # if candidate solution is still not better, then restart the initial point randomly.
            if candidate_eval[0] < initial_solution_eval[0]:
                plt.plot(iter_time, obtained_sol, label='line ' + str(line_number))
                line_number = line_number + 1
                obtained_sol.clear()
                iter_time.clear()

                initial_solution = [random.uniform(bounds[:, 0], bounds[:, 1])]
                initial_solution_eval = objective_func(initial_solution, dimension=dimension)
                obtained_sol.append(initial_solution_eval[0])
                iter_time.append(i)
                print("This is new [iter_time] %s [obtained_sol] %s: " % (iter_time, obtained_sol))

                print("'>%d_iteration, Restarted initial_sol (%s) = %.5f (initial_sol_eval)\n" %
                      (i, initial_solution, initial_solution_eval[0]))

        iter_time.append(i)
        obtained_sol.append(initial_solution_eval[0])

    plt.plot(iter_time, obtained_sol, label='line ' + str(line_number))
    plt.xlabel("Iteration time")
    plt.ylabel("Obtained value of maxima")
    plt.show()

    return [initial_solution, initial_solution_eval]


def check_for_bounds(candidate_solution, **kwargs):
    bounds = kwargs.get('bounds')
    initial_solution = kwargs.get('initial_solution')
    step_size = kwargs.get('step_size')

    # check for bounds (usually it oversteps the bounds when step size get bigger for ex.: x = 0.8)
    for bound in bounds[0, :]:
        if 0 > bound > candidate_solution[0]:
            while candidate_solution[0] < bound:
                candidate_solution = (initial_solution[0] + randn() * step_size)

        if 0 < bound < candidate_solution[0]:
            while candidate_solution[0] > bound:
                candidate_solution = (initial_solution[0] + randn() * step_size)

    return [candidate_solution]

