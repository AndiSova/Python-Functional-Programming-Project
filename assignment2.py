from itertools import permutations
from functools import reduce

input = input()

tupleList = list(permutations(input))

permList = map(lambda tupl: reduce(lambda a, b: a + b, tupl), tupleList)

with open("dictionary.txt", "r") as file:
    dictionary = file.read().split()
    result = filter(lambda w: w in dictionary, permList)
    print(list(result))
