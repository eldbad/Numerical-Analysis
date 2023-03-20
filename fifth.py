def calculate(lst):
    cube_poly(lst)


def cube_poly(lst):
    x_diff = [round(lst[i][0] - lst[i-1][0], 4) for i in range(1, len(lst))]
    second_coeffs = [2 * (x_diff[i-1] + x_diff[i]) for i in range(1, len(x_diff))]
    
    y_diff = [round(lst[i][1] - lst[i-1][1], 4) for i in range(1, len(lst))]
    
    d_list = [3 * (y_diff[i] / x_diff[i] - y_diff[i-1] / x_diff[i-1]) for i in range(1, len(y_diff))]
    print(x_diff)
    print(second_coeffs)
    print(y_diff)
    print(d_list)
    
    
    coeffs_tri = []
    coeffs_tri.append([0.0, second_coeffs[0], x_diff[1]])
    for i in range(1, len(second_coeffs)-1):
        coeffs_tri.append([])
        coeffs_tri[i].append(x_diff[i])
        coeffs_tri[i].append(second_coeffs[i])
        coeffs_tri[i].append(x_diff[i])

    coeffs_tri.append([x_diff[-1], second_coeffs[-1], 0.0])
    
    for i, coeff in enumerate(coeffs_tri):
        coeff.append(d_list[i])

    print(coeffs_tri)
    c_coeffs = tridiagonal_matrix_algorithm_copy(coeffs_tri)
    c_coeffs.insert(0, 0.0)
    print(c_coeffs)
    
    a_coeffs = [lst[i][1] for i in range(0, len(lst)-1)]
    print(a_coeffs)
    
    b_coeffs = [y_diff[i] / x_diff[i] - x_diff[i] * (c_coeffs[i+1] + 2 * c_coeffs[i]) / 3 for i in range(len(c_coeffs)-1)]
    b_coeffs.append(y_diff[-1] / x_diff[-1] - 2 * x_diff[-1] * c_coeffs[-1] / 3)
    d_coeffs = [(c_coeffs[i+1] - c_coeffs[i]) / 3 * x_diff[i] for i in range(len(c_coeffs)-1)]
    d_coeffs.append(c_coeffs[-1] / -3 * x_diff[-1])
    
    print(b_coeffs)
    print(d_coeffs)
    
    for i in range(len(c_coeffs)):
        bo = round(a_coeffs[i] + b_coeffs[i] * x_diff[i] + c_coeffs[i] * (x_diff[i]**2) + d_coeffs[i] * (x_diff[i]**3), 1) == lst[i+1][1]
        print(bo)
    
    xs = []
    for i in range(len(a_coeffs)):
        x = float(input("Введите x: "))
        
        if x < lst[0][0] or x > lst[-1][0]:
            print("x лежит не в интервале")
            i -= 1
            continue
        
        xs.append(x)
        
    xs.sort()
    print(xs)
    
    fs = []
    for x in xs:
        k = 0
        for i in range(1, len(lst)):
            if lst[i-1][0] <= x <= lst[i][0]:
                k = i-1
                break
        
        f = a_coeffs[k] + b_coeffs[k] * (x - lst[k][0]) + c_coeffs[k] * (x - lst[k][0])**2 + d_coeffs[k] * (x - lst[k][0])**3
        fs.append(f)
    
    print(fs)


def tridiagonal_matrix_algorithm_copy(abcd):
    UV = []
    U = 1
    V = 1
    for i, line in enumerate(abcd):
        UV.append([])
        UV[i].append(-(line[2] / (line[0] * U + line[1])))
        UV[i].append((line[3] - line[0] * V) / (line[0] * U + line[1]))

        U = UV[i][0]
        V = UV[i][1]
        print(f"U_{i + 1} = {U}; V_{i + 1} = {V}")

    xs = []
    x = 1
    for i in range(len(UV) - 1, -1, -1):
        x = UV[i][0] * x + UV[i][1]
        xs.append(x)
        print(f"x_{i + 1}={x}")
    xs = list(reversed(xs))

    print()
    print("Вычисляем невязки")
    for i, x in enumerate(xs):
        first = xs[i-1] if i >= 0 else 0.0
        last = xs[i+1] if i < len(xs)-1 else 0.0
        r = abcd[i][-1] - abcd[i][0] * first - abcd[i][1] * x - abcd[i][2] * last
        print(f"r_{i + 1} = {r}")

    return xs


if __name__ == "__main__":
    calculate([
        [1.0, 1.1],
        [1.2, 2.2],
        [1.4, 3.2],
        [1.6, 4.2],
        [1.8, 5.1],
        [2.0, 5.9]
    ])
 