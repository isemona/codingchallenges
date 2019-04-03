## White boarding at Eventbrite

## 1. Create a temp class that inserts a temperature and returns the min, max, mean and mode

Class Temperature(object):

    def __init__(self,min):
        self.min = None
        self.max = max

    temp_lst = []
    temp_dict ={}

    def insert(temp):
        
        if temp > min:
            self.min = temp


    def min():
        return self.min

    def max():
        return self.max

    def mean:
        return sum(temp_lst)/len(temp_lst)

    def mode:
        for i in temp_lst:
            temp_dict[i] = temp_dict.get(i, 0) + 1

        most_frequent = max(temp_dict.values)

        for value in temp_dict.values:
            if value == most_frequent:
                return most_frequent


## 2. Given two dictionaries check to see if they are equal

def deeply_equal(a,b):
    for key,value in dict_1.items():
        for key,value in dict_2.items():
            if dict_1.key != dict_2.key and if dict_1.value != dict_2.value:
                return False
            return True

# test case 1 - False
# dict_1 = {a:1, b:2, c:3}
# dict_2 = {a:1, b:2}

# test case 2 - True
# dict_1 = {a:1, b:2}
# dict_2 = {a:1, b:2}

# test case 3 - False
# dict_1 = {a:1, b:2}
# dict_2 = {a:1, c:2}

