import json

with open("times.json", "r") as f:
    data = json.load(f)

insertion_sort_times = data['insertionSortTimes']
merge_sort_times = data['mergeSortTimes']

insertion_sort_times_grouped_by_n = {}
merge_sort_times_grouped_by_n = {}

for n, time in insertion_sort_times:
    if n not in insertion_sort_times_grouped_by_n:
        insertion_sort_times_grouped_by_n[n] = []

    insertion_sort_times_grouped_by_n[n].append(time)

for n, time in merge_sort_times:
    if n not in merge_sort_times_grouped_by_n:
        merge_sort_times_grouped_by_n[n] = []

    merge_sort_times_grouped_by_n[n].append(time)

average_insertion_sort_times = []
average_merge_sort_times = []

for n, times in insertion_sort_times_grouped_by_n.items():
    average_insertion_sort_times.append((n, sum(times) / len(times)))

for n, times in merge_sort_times_grouped_by_n.items():
    average_merge_sort_times.append((n, sum(times) / len(times)))

averages = {'averageInsertionSortTimes': average_insertion_sort_times, 'averageMergeSortTimes': average_merge_sort_times}

with open("averages.json", "w") as f:
    json.dump(averages, f)
