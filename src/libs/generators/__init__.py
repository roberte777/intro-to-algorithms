import random
import time
from functools import partial
from libs.algos import *

def generate_random_list(size: int) -> list[int]:
    return [random.randint(-100, 100) for i in range(size)]

def generate_19_lists() -> list[list[int]]:
    res = []
    for i in range(10, 105, 5):
        res.append(generate_random_list(i))
    return res

def generate_time_matrix():
    #run algorithms on random lists
    lists = generate_19_lists()
    algos = [algo_1, algo_2, algo_3, algo_4]
    #for every list, run algorithms 500 times
    results = []
    for list in lists:
        algos[2] = partial(algo_3, L=0, U=len(list) - 1)
        times = []
        for algo in algos:
            res = []
            for _ in range(500):
                #run algorithm and calculate time
                start = time.time()
                algo(list)
                end = time.time()
                res.append(end - start)
            #calculate average time
            times.append(sum(res) / len(res))
        times.append("n^3")
        times.append("n^2")
        times.append("nLogn")
        times.append("n")
        results.append(times)
    return results
