import json
import matplotlib.pyplot as plt
import numpy as np

with open("averages.json", "r") as f:
    data = json.load(f)

average_insertion_sort_times = data['averageInsertionSortTimes']
average_merge_sort_times = data['averageMergeSortTimes']

x = [x[0] for x in average_insertion_sort_times]
y1 = [y[1] for y in average_insertion_sort_times]
y2 = [y[1] for y in average_merge_sort_times]

plt.title("Insertion Sort vs Merge Sort")

plt.xlabel("Input Size")
plt.ylabel("Time (Seconds)")


# Legend was created referencing this SO answer: https://stackoverflow.com/a/19125863
plt.scatter(x, y1, label="Insertion sort")
plt.scatter(x, y2, label="Merge sort")

plt.legend(loc="upper left")

plt.axis([0, 100, 0, .0001])

plt.show()