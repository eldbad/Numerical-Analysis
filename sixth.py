def calculate(lst):
    least_squares(lst, "lin")
    least_squares(lst, "pol")


def least_squares(lst, type):
    if type not in ["lin", "pol"]:
        raise ValueError("Задан неправильный тип функции")
        
    table = []
    table.append([lst[i][0] for i in range(len(lst))])
    table.append([lst[i][1] for i in range(len(lst))])
    table.append([lst[i][0]**2 for i in range(len(lst))])
    table.append([lst[i][0] * lst[i][1] for i in range(len(lst))])
    if type == "pol":
        table.append([lst[i][0]**3 for i in range(len(lst))])
        table.append([lst[i][0]**4 for i in range(len(lst))])
        table.append([table[2][i] * lst[i][1] for i in range(len(lst))])

    sums = [sum(values) for values in table]
    
    print(f"i\tx\ty\tx^2\txy", end="")
    if type == "pol":
        print(f"\tx^3\tx^4\tx^2y")
    print()
    
    for i in range(len(table[0])):
        print(i+1, end="\t")
        for j in range(len(table)):
            print(f"{table[j][i]}", end="\t")
        print()
    print("Sum", end="\t2")
    [print(el, end="\t") for el in sums]
    print("\n")
    
    if type == "lin":
        linear_coeffs = gauss_method([
            [sums[2], sums[0], sums[3]],
            [sums[0], len(table[0]), sums[1]]
        ])
        print(f"Линейная функция примет вид: y(x) = {linear_coeffs[0]}x + {linear_coeffs[1]}")
        find_y_by_x(linear_coeffs, type)
    if type == "pol":
        polynomial_coeffs = gauss_method([
            [sums[5], sums[4], sums[2], sums[6]],
            [sums[4], sums[2], sums[0], sums[3]],
            [sums[2], sums[0], len(table[0]), sums[1]]
        ])
        print(f"Полиномиальная функция примет вид: y(x) = {polynomial_coeffs[0]}x^2 + {polynomial_coeffs[1]}x + {polynomial_coeffs[2]}")
        find_y_by_x(polynomial_coeffs, type)


def gauss_method(coeffs):
    print("Метод Гаусса:")
    print(f"Начальные коэффициенты:\n{coeffs}")
    print("---------------")

    print()
    print("Прямой ход")
    for i, coeff_line in enumerate(coeffs):
        curr_div = coeff_line[i]
        for j in range(i + 1, len(coeffs)):
            if int(curr_div) != 0:
                break
            coeffs[i], coeffs[j] = coeffs[j], coeffs[i]
            curr_div = coeffs[i][i]
        if int(curr_div) == 0:
            continue

        for j in range(i + 1, len(coeffs)):
            deduct = -(coeffs[j][i] / curr_div)
            coeffs[j] = [coeff + coeff_line[k] * deduct for k, coeff in enumerate(coeffs[j])]

        print("---------------")
        print(f"Коэффициенты на {i + 1} итерации:\n{coeffs}")

    print("---------------")
    print(f"Коэффициенты после прямого хода:\n{coeffs}")

    print()
    print("---------------")
    print("Обратный ход")
    xs = []
    for i in range(len(coeffs) - 1, -1, -1):
        summ = 0
        for j in range(i + 1, len(coeffs)):
            summ += coeffs[i][j]
        summ -= coeffs[i][-1]
        x = -(summ / coeffs[i][i])
        xs.append(x)

        print(f"x_{i + 1} = {x}")

        for j in range(i - 1, -1, -1):
            coeffs[j][i] *= x
    print()
    xs = list(reversed(xs))
    xs = [round(x, 2) for x in xs]
    print(f"Имеем коэффициенты: {xs}")
    
    return xs


def find_y_by_x(coeffs, type):
    xs = input("Введите значения x через запятую (пример: 2, 1.24, 6.89): ")
    xs = xs.split(", ")
    for i, x in enumerate(xs):
        x = float(x)
        if type == "lin":
            y = coeffs[0] * x + coeffs[1]
            print(f"x_{i + 1} = {x}; y_{i + 1} = {y}")
        if type == "pol":
            y = coeffs[0] * (x ** 2) + coeffs[1] * x + coeffs[2]
            print(f"x_{i + 1} = {x}; y_{i + 1} = {y}")
            
            
if __name__ == "__main__":
    calculate([
        [-1, -6],
        [0, -1],
        [1, 4],
        [2, 9]
    ])
