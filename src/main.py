from libs.algos import *

def main():
    numbers = []
    with open("phw_input.txt", "r") as f:
        numbers = f.readline().split(",")
        numbers = [int(i) for i in numbers]
    res = run_algorithms(numbers)
    print(res)

def run_algorithms(arr: list[int]):
    res_1 = algo_1(arr)
    res_2 = algo_2(arr)
    res_3 = algo_3(arr, 0, len(arr) - 1)
    res_4 = algo_4(arr)
    return res_1, res_2, res_3, res_4

if __name__ == "__main__":
    main()
