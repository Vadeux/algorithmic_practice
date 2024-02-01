def sum_of_intervals(list_of_intervals: list) -> int:
    final_list = []
    for interval in list_of_intervals:
        for elem in range(interval[0], interval[1]):
            final_list.append(elem)
    return len(set(final_list))


input_1 = [
   [1, 4],
   [7, 10],
   [3, 5]
]
assert sum_of_intervals(input_1) == 7

input_2 = [
   [1, 2],
   [6, 10],
   [11, 15]
]
assert sum_of_intervals(input_2) == 9

input_3 = [
   [1, 4],
   [7, 10],
   [3, 5]
]
assert sum_of_intervals(input_3) == 7

input_4 = [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
]
assert sum_of_intervals(input_4) == 19

input_5 = [
   [0, 20],
   [-100000000, 10],
   [30, 40]
]
assert sum_of_intervals(input_5) == 100000030
