from island_finder import find_islands


def test_array_1():
    array = [[0, 1, 0],
             [0, 0, 0],
             [0, 1, 1]]
    assert find_islands(array) == 2


def test_array_2():
    array = [[0, 0, 0, 1],
             [0, 0, 1, 0],
             [0, 1, 0, 0]]
    assert find_islands(array) == 3


def test_array_3():
    array = [[0, 0, 0, 1],
             [0, 0, 1, 1],
             [0, 1, 0, 1]]
    assert find_islands(array) == 2
