def tridiagonal_matrix_algorithm(*args):
    coeffs = find_coeffs_from_str(*args)
    print(f"Начальные коэффициенты:\n{coeffs}")

    print("---------------")
    print("Составление таблицы")
    abcd = []
    for i, line in enumerate(coeffs):
        abcd.append([])
        
        abcd[i].append(line[i-1])
        abcd[i].append(line[i])
        abcd[i].append(line[i+1])
    abcd[0][0] = 0.0
    abcd[-1][-1] = 0.0
    for i, line in enumerate(abcd):
        line.append(coeffs[i][-1])
        
    for line in abcd:
        for el in line:
            print(el, end="    ")
        print()
    print()


    print("Определяем прогоночные коэффициенты")
    UV = []
    U = 1
    V = 1
    for i, line in enumerate(abcd):
        UV.append([])
        UV[i].append(-(line[2] / (line[0] * U + line[1])))
        UV[i].append((line[3] - line[0] * V) / (line[0] * U + line[1]))
        
        U = UV[i][0]
        V = UV[i][1]
        print(f"U_{i+1} = {U}; V_{i+1} = {V}")
    
    xs = []
    x = 1
    for i in range(len(UV)-1, -1, -1):
        x = UV[i][0] * x + UV[i][1]
        xs.append(x)
        print(f"x_{i+1}={x}")
    xs = list(reversed(xs))
    
    print()
    print("Вычисляем невязки")
    for i, x in enumerate(xs):
        r = coeffs[i][-1] - coeffs[i][0] * xs[0] - coeffs[i][1] * xs[1] - coeffs[i][2] * xs[2] - coeffs[i][3] * xs[3]
        print(f"r_{i+1} = {r}")
    
    print()
    print(f"Ответ: {xs}")


def find_coeffs_from_str(*args):
    coeffs = []

    for i, f in enumerate(args):
        lst = [0.0] * (len(args) + 1)
        coeffs.append(lst)
        f = iter(f)
        number = ""
        for symb in f:
            if symb == "x":
                x_num = next(f)
                if number == "":
                    number = "1"
                if number == "+" or number == "-":
                    number += "1"
                coeffs[i][int(x_num)-1] = float(number)
                number = ""
            else:
                number += symb
        coeffs[i][-1] = float(number[1:])
        
    return coeffs


if __name__ == '__main__':
    tridiagonal_matrix_algorithm(
        "3x1+2x2=9",
        "-x1-5x2+3x3=-18",
        "-2x2+7x3+4x4=-6",
        "3x3+5x4=-6"
    )