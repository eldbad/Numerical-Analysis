from itertools import combinations
from operator import mul
from functools import reduce


def poly(*args):
    sums = []
    for i in range(len(args) + 1):
        sum_ = 0
        for c in combinations(args, i):
            mult = 1
            for num in c:
                mult *= num
            sum_ += mult
        sums.append(sum_)
    
    return sums
            
            
def old_pily(*args):
    return [sum([reduce(mul, c, 1) for c in combinations(args, i)])
            for i in range(len(args)+1)]


if __name__ == "__main__":
    print(poly(2,-1))
    print(old_pily(2,-1))
    