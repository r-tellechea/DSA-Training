class CoinProblem():
    def __init__ (self, coin_set):
        self.coin_set = coin_set
        self.coin_set.sort()

        self.coin_count = {0 : 0} # No coin is necessary to sum 0
        self.coin_solutions = {0 : 1} # There is only 1 way to sum 0
    
    def number_of_coins_to_sum_target (self, target):
        if target in self.coin_count:
            return self.coin_count[target]
        # If target is not in the dictionary we calculate it:
        min_coin_number = 0
        for coin in self.coin_set:
            lower_target = target - coin
            if lower_target >= 0:
                if min_coin_number == 0:
                    min_coin_number = 1 + self.number_of_coins_to_sum_target(lower_target)
                else:
                    min_coin_number = min(min_coin_number, 1 + self.number_of_coins_to_sum_target(lower_target))
        self.coin_count[target] = min_coin_number
        return min_coin_number

    def count_number_of_sum_solutions (self, target):
        if target in self.coin_solutions:
            return self.coin_solutions[target]
        
        solutions_count = 0
        for coin in self.coin_set:
            lower_target = target - coin
            if lower_target >= 0:
                solutions_count += self.count_number_of_sum_solutions(lower_target)
        
        self.coin_solutions[target] = solutions_count
        return solutions_count