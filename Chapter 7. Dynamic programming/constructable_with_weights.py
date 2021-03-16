class Weights ():
    def __init__ (self, weight_list):
        self.weight_list = []
        self.size = len(weight_list)
        for element in weight_list:
            self.weight_list.append(element)

        self._possible_map = {(0,0) : True}

    def _possible (self, target, index):
        if target < 0:
            return False
        elif target != 0 and index == 0:
            return False
        elif (target, index) in self._possible_map:
            return self._possible_map[(target, index)]
        else:
            chosing     = self._possible(target - self.weight_list[index - 1], index - 1)
            not_chosing = self._possible(target, index - 1)
            self._possible_map[(target, index)] = chosing or not_chosing
            return self._possible_map[(target, index)]

    def constructable (self, target):
        return self._possible(target, self.size)

w = Weights([1,3,3,5])
for i in range(13):
    print(f"Value: {i}. Constructable: {w.constructable(i)}")