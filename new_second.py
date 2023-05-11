def gauss_method_new(coeffs):
    print("Метод Гаусса:")
    print(f"Начальные коэффициенты:\n{coeffs}")
    print("---------------")
    
    for i, coeff_line in enumerate(coeffs):
        for j, coeff in enumerate(coeff_line):
            coeff_line[j] = float(coeff_line[j])
            
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
    print(f"Ответ: {xs}")

    return xs


if __name__ == "__main__":
    gauss_method_new([
        [1, -1, 2, -1, 1],
        [2, 1, 3, 1, 4],
        [1, 1, 1, -1, 2],
        [2, 1, 5, -2, 3]
    ])
