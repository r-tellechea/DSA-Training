from coin_problem import CoinProblem

coin_problem = CoinProblem([1,3,4])

pass_test = True 
solution_array = [1, 1, 1, 2, 4, 6, 9, 15, 25, 40, 64]

for index in range(len(solution_array)):
    if solution_array[index] != coin_problem.count_number_of_sum_solutions(index):
        pass_test = False
        break

if pass_test:
    print("Success!")
else:
    print("Fail!")