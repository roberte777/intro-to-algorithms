from .algo_1 import algo_1
from .algo_2 import algo_2
from .algo_3 import algo_3
from .algo_4 import algo_4

def run_algorithms(arr: list[int]):
    res_1 = algo_1(arr)
    res_2 = algo_2(arr)
    res_3 = algo_3(arr, 0, len(arr) - 1)
    res_4 = algo_4(arr)
    return res_1, res_2, res_3, res_4

def print_answers(results: tuple):
    for i, result in enumerate(results):
        print(f"algorithm-{i+1}: {result};")
