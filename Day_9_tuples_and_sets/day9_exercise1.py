# 1. Min, Avg, Max

# Write a function get_min_avg_max (sequence) that returns a tuple with three values, the smallest, the arithmetic mean, and the largest value in the string, respectively.

# Example:

# get_min_avg_max ([0,10,1,9]) -> (0,5,10)

# the incoming sequence can be a tuple or a list with numeric values.

from statistics import mean
# from statistics import median
# from statistics import mode # and so on

def get_min_avg_max(sequence):
    # return min(sequence), sum(sequence)/len(sequence), max(sequence) # one liner
    # return min(sequence), round(mean(sequence),4), max(sequence)  # one liner
    max_value = max(sequence)
    min_value = min(sequence)
    if type(sequence) == str: # we have no mean defined for strings
        ord_list = [ord(i) for i in sequence]
        return min_value, chr(int(sum(ord_list)/len(ord_list))), max_value # silly example
    mean_value = round(sum(sequence)/len(sequence), 2)
    my_tuple = (min_value, mean_value, max_value) # parenthesis are optional
    return my_tuple

print(get_min_avg_max([0,10,1,9])) #OUTPUT: (0, 5, 10)
print(get_min_avg_max([2,4,6.8])) #OUTPUT: (2, 4, 6.8)
print(get_min_avg_max([2,4,6.8,7,10,3252])) #OUTPUT: (2, 4, 6.8)
# print(get_min_avg_max("vamir"))