# 3. City Population
# The city has a known population p0
# A percentage of population perc is added each year
# Every year a certain number of delta also arrive (or leave)
# We need to know when (if at all) the city will reach a population of p
# Write a function get_city_year (p0, perc, delta, p) that returns the years (full) when p is reached.
# If p cannot be reached, then we return -1
#

# neat recursive solution
# def get_city_year(p0, perc, delta, p, years=1):
#     predicted_p = p0 + p0 * (perc / 100) + delta
#     if p0 > predicted_p:
#         return -1
#     if predicted_p >= p:
#         return years
#     else:
#         return get_city_year(predicted_p, perc, delta, p, years + 1)  # return 1 sounds like a bad idea here


def get_city_year(p0=0, perc=0, delta=0, p=0):
    percents = perc * 0.01
    new_pop = 0.0
    years = 0
    while new_pop < p:  # p is our target population
        new_pop = p0 + (p0 * percents) + delta
        if new_pop <= p0:
            return -1
            break
        p0 = new_pop
        years += 1

    return years

print(get_city_year(1000, 2, 50, 1200))
# print(get_city_year(1500, 5, 100, 5000))
# # how about slow growth?
# print(get_city_year(1000, 0.1, 0, 5000000))
# print(get_city_year(1000, 0, 0, 5000))
# print(get_city_year(1000, 0, -50, 5000))
# print(get_city_year(1000, -2, 25, 5000))
