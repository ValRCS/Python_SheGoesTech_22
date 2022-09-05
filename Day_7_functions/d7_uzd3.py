################### 3 UZD ###################################################

def get_city_year(population_now, perc, delta, population_to_reach, verbose=False):
    perc = perc / 100
    years = 0
    population_prev = population_now
    if population_now < population_to_reach:
        # if delta < 0:
        #     if population_now * perc < delta * -1:
        #         return -1
        while population_now < population_to_reach:
            population_now = population_now + (population_now * perc) + delta
            if round(population_now,2) <= round(population_prev,2):
                print("Population is not increasing, loop imminent")
                return -1  # early return if population is not increasing
            population_prev = population_now
            years = years + 1
            if verbose:
                print(population_now, population_to_reach, years)

    elif population_now > population_to_reach:
        if delta < 0:
            if population_now * perc > delta:
                return -1
        else:
            return -1
        while population_now > population_to_reach:
            population_now = population_now + (population_now * perc) + delta
            years = years + 1

    return years


print(get_city_year(1000, 2, 50, 1200))
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1000, 2, -50, 1000))  # base case
print(get_city_year(1500, 5, 100, 5000)) # should be 15
print(get_city_year(1_500_000, 2.5, 10_000, 2_000_000)) # should be 10

print(get_city_year(1000, -4, 50, 2_000, verbose=True))  # we will get a loop here


# population_now = int(float(input("What is population now: ")))
# percentage = float(input("What is growth percent: "))
# delta = int(float(input("Number of people leaving/arriving: ")))
# population_to_reach = int(float(input("What population are we looking for: ")))
#
# answer = get_city_year(population_now, percentage, delta, population_to_reach)
# if answer < 0:
#     print("Impossible")
# else:
#     print(f"It will take {answer} years")
