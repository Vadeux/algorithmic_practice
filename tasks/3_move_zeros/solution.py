def move_zeros(arr):
    zeros = []
    result_list = []
    for elem in arr:
        if (elem == 0 or elem == 0.0) and (type(elem) == int or type(elem) == float):
            zeros.append(elem)
        else:
            result_list.append(elem)
    result_list.extend(zeros)
    return result_list


assert move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0]
