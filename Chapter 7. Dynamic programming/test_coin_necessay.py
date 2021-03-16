from coin_problem import CoinProblem

coin_problem = CoinProblem([1,3,4])

pass_test = True 
solution_array = [0,1,2,1,1,2,2,2,2,3,3]

for index in range(len(solution_array)):
    if solution_array[index] != coin_problem.number_of_coins_to_sum_target(index):
        pass_test = False
        break

if pass_test:
    print("Success!")
else:
    print("Fail!")