from constants import FOOD_PER_INDIVIDUAL , INDIVIDUALS_PER_GROUP, GROWTH_PER_GROUP, DECLINE_PER_GROUP

def simulation_day(initial_population, initial_food , food_per_day):
    #== Start of day ===
    number_group = initial_food // INDIVIDUALS_PER_GROUP
    excess_food = initial_food - initial_population * FOOD_PER_INDIVIDUAL

    print(
        initial_population, "individuals\n",
        initial_food, "food\n",
        excess_food, "excess food"
        )
    print("There are", number_group, "group")
          
        
    will_grow = excess_food > 0
    will_shrink = excess_food < 0

    if will_grow:
        new_population = initial_population + number_group * GROWTH_PER_GROUP
        print( "Population grows to", new_population)
    elif will_shrink:
        new_population = initial_population - number_group * DECLINE_PER_GROUP
        print( "Population shrinks to", new_population)
    else:
        new_population = initial_population
        print( "Population is stable", new_population, "individuals")
        
    # Deal with the food for the next day
    new_food = food_per_day
    if excess_food > 0:
    #Add leftove food fo the next day
        new_food = new_food + excess_food
    
# ===Ready for the next day ==
    return(new_population,new_food)