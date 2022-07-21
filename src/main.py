from libs import generators, algos

def main():
    #get first line from file and run algorithms on the list
    numbers = []
    with open("phw_input.txt", "r") as f:
        numbers = f.readline().split(",")
        numbers = [int(i) for i in numbers]
    res = algos.run_algorithms(numbers)
    #print answers
    algos.print_answers(res)

    #generate the matrix of times for 19 lists
    matrix = generators.generate_time_matrix()
    #write matrix to file
    with open("ethanwilkes_colespencer_phw_output.txt", "w") as f:
        f.write("algorithm-1,algorithm-2,algorithm-3,algorithm-4,n^3,n^2,nLogn,n\n")
        for row in matrix:
            f.write(",".join(str(i) for i in row))
            f.write("\n")

if __name__ == "__main__":
    main()
