import timeit
import random
import copy
import json
from sorts import *


def random_list(n):
    """Return list containing n random values in the range of 1 to 1000 inclusive"""
    arr = []
    for i in range(n):
        arr.append(random.randint(1,1000))
    return arr

if __name__ == '__main__':
    unsorted_lists = []
    # generate 1,00 lists of size n for each n in the range of 1 to 1000 inclusive
    for i in range(1, 1001):  # determines the range of list sizes
        for j in range(100):  # how many lists to generate for each size
            unsorted_lists.append(random_list(i))

    # create a deepcopy of the unsorted lists so that both sorts can run on different unsorted copies of the same lists
    unsorted_lists_copy = copy.deepcopy(unsorted_lists)

    insertion_sort_times = []
    merge_sort_times = []
    
    for arr in unsorted_lists:
        time = timeit.timeit('insertionSort(arr)', globals=globals(), number=1)
        insertion_sort_times.append((len(arr), time))

    for arr in unsorted_lists_copy:
        time = timeit.timeit('mergeSort(arr)', globals=globals(), number=1)
        merge_sort_times.append((len(arr), time))

    times = {'insertionSortTimes': insertion_sort_times, 'mergeSortTimes': merge_sort_times}
        
    with open("times.json", "w") as f:
        json.dump(times, f)


