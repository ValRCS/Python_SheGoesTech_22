def get_min_avg_max(sequence):
    return min(sequence), sum(sequence) / len(sequence), max(sequence)


res = get_min_avg_max([1, 4, 7, 8, 99, 234])
print(res, type(res))


def get_min_med_max(value_list):
    sorted_list = sorted(value_list)
    print(sorted_list)
    median_index = len(sorted_list) / 2

    if not median_index % 1 == 0:
        median_index = int((len(sorted_list) - 1) / 2)
        median = sorted_list[median_index]
    else:  # to support string here you would have to check type of items in here
        if type(sorted_list[int(median_index) - 1]) is str:
            median = sorted_list[int(median_index) - 1] + sorted_list[int(median_index)] # so we put the middle stings together
        else: # numeric types but we could actually check
            median = (sorted_list[int(median_index) - 1] + sorted_list[int(median_index)]) / 2

    return min(value_list), median, max(value_list)


print(get_min_med_max([1, 5, 8, 4, 3]))
print(get_min_med_max ([2,2,9,9,4,3]))
print(get_min_med_max ("baaac"))
print(get_min_med_max ("faaacb") )
