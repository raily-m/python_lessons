def test_recursion(value):
    if value != 0:
        test_recursion(value -1)

    print(f"Конец функции {value}")
    return value

test_recursion(3)