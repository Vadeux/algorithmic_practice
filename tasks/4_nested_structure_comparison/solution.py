def same_structure_as(original, other):
    if type(original) != type(other) or len(original) != len(other):
        return False
    for i in range(len(original)):
        if type(original[i]) != type(other[i]) and type(original[i]) == list and type(other) == list:
            return False
        elif type(original[i]) == type(other[i]) and type(original[i]) == list:
            return same_structure_as(original[i], other[i])
    return True


assert same_structure_as([1, 1, 1], [2, 2, 2]) is True
assert same_structure_as([1, [1, 1]], [2, [2, 2]]) is True

assert same_structure_as([1, [1, 1]], [[2, 2], 2]) is False
assert same_structure_as([1, [1, 1]], [[2], 2]) is False

assert same_structure_as([[[], []]], [[[], []]]) is True

assert same_structure_as([[[], []]], [[1, 1]]) is False
