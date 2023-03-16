def gauss_method(*args):
    coeffs = find_coeffs_from_str(*args)
    print(f"Начальные коэффициенты:\n{coeffs}")
    print("---------------")

    print()
    print("Прямой ход")
    for i, coeff_line in enumerate(coeffs):
        curr_div = coeff_line[i]
        for j in range(i+1, len(coeffs)):
            if int(curr_div) != 0:
                break
            coeffs[i], coeffs[j] = coeffs[j], coeffs[i]
            curr_div = coeffs[i][i]
        if int(curr_div) == 0:
            continue

        for j in range(i+1, len(coeffs)):
            deduct = -(coeffs[j][i] / curr_div)
            coeffs[j] = [coeff + coeff_line[k] * deduct for k, coeff in enumerate(coeffs[j])]
        
        print("---------------")
        print(f"Коэффициенты на {i+1} итерации:\n{coeffs}")
        
    print("---------------")
    print(f"Коэффициенты после прямого хода:\n{coeffs}")

    print()
    print("---------------")
    print("Обратный ход")
    xs = []
    for i in range(len(coeffs)-1, -1, -1):
        summ = 0
        for j in range(i+1, len(coeffs)):
            summ += coeffs[i][j]
        summ -= coeffs[i][-1]
        x = -(summ/coeffs[i][i])
        xs.append(x)
        
        print(f"x_{i+1} = {x}")
        
        for j in range(i-1, -1, -1):
            coeffs[j][i] *= x
    print()
    xs = list(reversed(xs))
    print(f"Ответ: {xs}")


def find_coeffs_from_str(*args):
    import re
    coeffs = []

    for i, f in enumerate(args):
        coeffs.append([])
        for p in re.split(r"x\d+", f):
            coeffs[i].append(1 if p == '+' else float(p.replace('=', '')))

    return coeffs


if __name__ == '__main__':
    gauss_method(
        "2x1+x2+x3+x4=1",
        "2x1+2x2+2x3+3x4=-1",
        "4x1+3x2+3x3+3x4=1",
        "6x1+4x2+5x3+2x4=4"
    )
