def get_min_avg_max(numbers):
    return min(numbers), sum(numbers) / len(numbers), max(numbers)


print(get_min_avg_max([0, 10, 1, 9]))


def get_min_med_max(sequence, debug=False):
    new_list = sorted(sequence)
    if debug:
        print(new_list)
    min_value = min(new_list)
    max_value = max(new_list)
    middle = int(len(sequence) / 2)
    if len(sequence) % 2 == 0:
        for i in range(len(new_list)):
            if type(new_list[i]) == str:  # if string - take both middle values
                median_value = new_list[middle - 1] + new_list[middle]
            else:  # if not string, div by 2
                median_value = (new_list[middle - 1] + new_list[middle]) / 2
        # print(middle)
        # print(my_list)
        result = min_value, median_value, max_value
    # print(result)
    else:  # if odd number of elements
        middle = int((len(sequence) + 1) / 2)
        median_value = new_list[middle - 1]
        result = min_value, median_value, max_value
    return result


print(get_min_med_max([2, 2, 9, 9, 4, 3]))
print(get_min_med_max([1, 5, 8, 4, 3]))
print(get_min_med_max("baaac"))
print(get_min_med_max("faaacb"))
print(get_min_med_max("Valdis"))
print(get_min_med_max("Valdis", debug=True))

# median is also available from library statistics
from statistics import median  # usually imports go up top

print(median([2, 2, 9, 9, 4, 3]))
