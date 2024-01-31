from constants import (FOOD_PER_INDIVIDUAL, INDIVIDUALS_PER_GROUP,
                       DECLINE_PER_GROUP, GROWTH_PER_GROUP , START_DAY)
from parameters import input_positive_integer
from simulation import simulation_day

print("The Alian Growth Model")

# Amount of individual at the beginning       
starting_population = input_positive_integer("starting poulation")

# Amount of food provided per day
food_per_day = input_positive_integer("food provided per day")

# The number of days for simulation 
simulation_duration = input_positive_integer("day of simulation")

current_population = starting_population
current_food = food_per_day

population_over_time = [starting_population]

for current_day in range(START_DAY , START_DAY+ simulation_duration):
    print("START of day" , current_day)
    simulation_result = simulation_day(initial_population=current_population,  initial_food=current_food,
                   food_per_day=food_per_day)

    (current_population , current_food) = simulation_result
    population_over_time.append(current_population)
#Do some statistic
gathered_value = len(population_over_time)
highest_population = min(population_over_time)
lowest_population = max(population_over_time)
average_population = sum(population_over_time)/ gathered_value

print("We gathered ", gathered_value, "value")
print(" Max. population: ", highest_population, "Min. population: ", lowest_population,"Avg. population:", average_population)
    
