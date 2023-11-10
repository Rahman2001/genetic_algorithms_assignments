
from numpy.array_api import asarray

import Hill_Climbing_with_Random_Restart
import Random_Search
import Simulated_Annealing
from SphereFunction import sphere
import Steepest_Ascent_Hill_Climbing
from RastriginFunction import rastrigin, show_plot_rastrigin

# Z = rastrigin
S = sphere
bounds = asarray([[-5.12, 5.12]])
# -----------------------------------This is Rastrigin function in Steepest-Hill Climbing--------------------------


# st_ac_hill_cl = Steepest_Ascent_Hill_Climbing
# solution_point, solution_point_eval = st_ac_hill_cl.hill_climbing(Z, bounds, 100, 0.4, 3)
# show_plot_rastrigin()
#----------------------------------------------------------------------------------------------------------

#------------------------------------This is Rastrigin function in Random Search------------------------------------
# rand_src = Random_Search
# best = rand_src.random_search(Z, bounds, 100, 3)
# print(best)
#-------------------------------------------------------------------------------------------------------------------

#------------------------------------This is Rastrigin function in Hill-Climbing with Random Restart-------------------
# hill_cl_rand_res = Hill_Climbing_with_Random_Restart
# hill_cl_rand_res.hill_climbing_with_random_restart(Z, bounds, 100, 0.2, 3)

#----------------------------------------------------------------------------------------------------------------------

#-------------------------------------This is Rastrigin function in Simulated Annealing--------------------------------
# sm_ann = Simulated_Annealing
# sm_ann.simulated_annealing(Z, bounds, 100, 0.4, 100, 3)

#----------------------------------------------------------------------------------------------------------------------

#-------------------------------------This is Sphere function in Steepest-Ascent Hill-Climbing-------------------------
# sph_func.show_plot_sphere()
# st_hill = Steepest_Ascent_Hill_Climbing
# st_hill.hill_climbing(S, bounds, 100, 0.4, 3)
#----------------------------------------------------------------------------------------------------------------------

#---------------------------------------This is Sphere function in Random Search---------------------------------------
# rand_sr = Random_Search
# rand_sr.random_search(S, bounds, 100, 3)
#---------------------------------------------------------------------------------------------------------------------

#---------------------------------------This is Sphere function in Simulated Annealing-------------------------------
# sim_ann = Simulated_Annealing
# sim_ann.simulated_annealing(S, bounds, 100, 0.4, 100, 3)
#---------------------------------------------------------------------------------------------------------------------

#---------------------------------------This is Hill-Climbing with Random-Restart------------------------------------
hill_rand = Hill_Climbing_with_Random_Restart
hill_rand.hill_climbing_with_random_restart(S, bounds, 100, 0.4, 3)