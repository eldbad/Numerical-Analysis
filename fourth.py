from itertools import combinations
from operator import mul
from functools import reduce


def calculate(lst):
    print("Полином Лагранжа")
    lagr(lst)
    print("Полином Ньютона")
    newton(lst)


def lagr(lst):
    xs = [line[0] for line in lst]
    ls = []
    for i, x in enumerate(xs):
        xs.pop(i)
        polynom = poly(*xs)
        divider = reduce(mul, [x - x_ for x_ in xs])
        ls.append([coeff / divider for coeff in polynom])
        xs.insert(i, x)

    for i, line in enumerate(ls):
        ls[i] = [coeff * lst[i][1] for coeff in line]
    
    ls_new = []
    for i, line in enumerate(ls):
        ls_new.append(sum([coeff[i] for coeff in ls]))
    
    print_answer(ls_new)

def newton(lst):
    diffs = []
    diffs.append([float(y[1]) for y in lst])
    
    i_diff = 1
    for i in range(len(lst)-1, 0, -1):
        diffs.append([])
        for j in range(i):
            difference = (diffs[i_diff-1][j] - diffs[i_diff-1][j+1]) / (lst[j][0] - lst[j+i_diff][0])
            diffs[i_diff].append(difference)
        i_diff += 1
    diffs.pop(0)
    
    xs = [-line[0] for line in lst]
    polynoms = []
    for i in range(len(xs)-1):
        polynoms.append(poly(*xs[0:i+1]))
    
    for i, line in enumerate(diffs):
        polynoms[i] = [line[0] * coeff for coeff in polynoms[i]]

    for i, polynom in enumerate(polynoms):
        [polynom.insert(0, 0.0) for i in range(1-i)]
        
    polynoms_new = []
    for i in range(len(polynoms)+1):
        polynoms_new.append(sum([coeff[i] for coeff in polynoms]))
    polynoms_new[-1] += lst[0][1]
    
    print_answer(polynoms_new)


def poly(*args):
    return [sum([reduce(mul, c, 1) for c in combinations(args, i)])
                                   for i in range(len(args)+1)]


def print_answer(results):
    print(f"Ответ: ", end="")
    for i in range(len(results) - 1, -1, -1):
        result = round(results[-(i + 1)], 2)
        operator = "+" if result >= 0 else ""
        print(operator, end="")
        if i != 0:
            print(f"{result}x^{i}", end="")
        else:
            print(f"{result}")


if __name__ == "__main__":
    calculate([
        [-2, 1],
        [1, 4],
        [4, 1]
    ])
