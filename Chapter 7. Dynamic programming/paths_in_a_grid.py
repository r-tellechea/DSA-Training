class Grid ():
    def __init__ (self, table):
        self.weight_table = []
        self.x_size = len(table)
        self.y_size = len(table[0])
        self.sum_array = [[None] * self.y_size] * self.x_size

        # Copy the weight table
        for index_1 in range(self.x_size):
            self.weight_table.append([])
            for index_2 in range(self.y_size):
                self.weight_table[index_1].append(table[index_1][index_2])

    def lower_path_sum (self):
        return self.max_sum_at(self.x_size - 1, self.y_size - 1)

    def max_sum_at (self, i, j):
        if self.sum_array[i][j] != None:
            return self.sum_array[i][j]
        else:
            max_candidates = [0]
            if i != 0:
                max_candidates.append(self.max_sum_at(i-1, j))
            if j != 0:
                max_candidates.append(self.max_sum_at(i, j-1))
            return max(max_candidates) + self.weight_table[i][j]

