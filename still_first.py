def calculate(func, a, b):
    # Метод деления отрезка пополам
    cut_section_method(func, a, b)

    print()

    # Метод Ньютона
    newton_method(func, lambda x: 3*(x**2) + 0.4, lambda x: 6*x, a, b)


def cut_section_method(func, a, b):
    print("-----Метод деления отрезка пополам-----")

    # Значения функции на концах отрезка
    f_a = func(a)
    f_b = func(b)
    print(f"F(a) = {f_a}, F(b) = {f_b}")
    print()

    # Проверка различия знаков этих значений
    if not f_a * f_b < 0:
        print("Значения функций на границах имеют одинаковые знаки")
        print("Условие не выполнено")
        return

    # Приближение
    i = 1
    while True:
        print("---------------")
        print(f"Приближение {i}:")

        # Середина отрезка
        x = (a + b) / 2
        print(f"a = {a}, b = {b}, x{i} = (a + b) / 2 = {x}")

        # Погрешность
        error = abs(b - a)
        print(f"Погрешность: |b - a| = {error}")
        if error < 0.01:
            break

        # Значения функций на концах и в центре отрезка
        f_a = func(a)
        f_b = func(b)
        f_x = func(x)

        # Определение следующей границы
        if f_a * f_x < 0:
            b = x
        elif f_b * f_x < 0:
            a = x
        else:
            print("Ошибка в вычислениях")
            return

        print(f"F(a) = {f_a}, F(x{i}) = {f_x}, F(b) = {f_b}")
        print(f"Корень находится в интервале [{a};{b}]")
        i += 1

    print("---------------")
    print(f"Ответ:{x}")
    print("---------------")


def newton_method(func, first_deriv, second_deriv, a, b):
    print("-----Метод Ньютона-----")

    # Определение начальной точки касания
    if func(a) * second_deriv(a) > 0:
        x = a
    elif func(b) * second_deriv(b) > 0:
        x = b
    else:
        print("Ни одно из условий для границ отрезка не выполнено")
        return

    print(f"x0 = {x}")

    # Приближение
    i = 1
    while abs(func(x)) >= 0.01:
        print("---------------")
        # Нахождение x_k
        x = x - func(x)/first_deriv(x)
        print(f"Приближение {i}:")
        print(f"x{i} = {x}")
        print(f"|F(x{i})| = {func(x)}")
        i += 1

    print("---------------")
    print(f"Ответ: {x}")
    print("---------------")


# Начало программы
if __name__ == "__main__":
    # Отправляем функцию в метод для рассчётов
    calculate(lambda x: x**3 + 0.4*x - 1.2, 0.5, 1)
