import numpy as np
from typing import List


x_directions = [-1, 0, 1, 0]
y_directions = [0, 1, 0, -1]


def is_valid(visited_array: np.ndarray, node_x: int, node_y: int) -> bool:
    if 0 <= node_x < visited_array.shape[0] and \
            0 <= node_y < visited_array.shape[1] and \
            visited_array[node_x, node_y] == False:
        return True
    else:
        return False


def find_neighbors(input_array: np.ndarray, visited_array: np.ndarray, node_x: int, node_y: int) -> np.ndarray:
    for i, j in zip(x_directions, y_directions):
        neighbor_x, neighbor_y = node_x+i, node_y+j
        valid = is_valid(visited_array, neighbor_x, neighbor_y)
        if not valid:
            continue
        visited_array[neighbor_x, neighbor_y] = True
        if input_array[neighbor_x, neighbor_y] == 1:
            visited_array = find_neighbors(input_array, visited_array, neighbor_x, neighbor_y)
    return visited_array


def find_islands(input_array: List[List[int]]) -> int:
    input_array = np.array(input_array)
    visited_array = np.zeros(input_array.shape, dtype=bool)
    candidates = np.array(np.where(input_array == 1)).T
    n_islands = 0
    for candidate in candidates:
        candidate_x, candidate_y = candidate
        valid = is_valid(visited_array, candidate_x, candidate_y)
        if not valid:
            continue
        visited_array = find_neighbors(input_array, visited_array, candidate_x, candidate_y)
        n_islands += 1
    return n_islands
