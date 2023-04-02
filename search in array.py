def search_array(A: list, N: int, x: int):
    """
    Поиск числа x в массиве
    :param A:  Массив
    :param N: Длина массива
    :param x: Число, которое ищут
    :return: индекс числа или -1 (если числа нет). Если несколько x
    в массиве выводить 1ый по порядку.
    """
    for i in range(N):
        if A[i] == x:
            return i
    return -1


def test_search_array():
    A1 = [1, 2, 3, 4, 5]
    if search_array(A1, 5, 8) == -1:
        print("Test 1 - ok")
    else:
        print("Test 1 - fail")
    A2 = [1, 2, 3, 4, 5]
    if search_array(A2, 5, 3) == 2:
        print("Test 2 - ok")
    else:
        print("Test 2 - fail")
    A3 = [1, 2, 3, 3, 3]
    if search_array(A2, 5, 3) == 1:
        print("Test 2 - ok")
    else:
        print("Test 2 - fail")


print(search_array([2, 123, 2, 31, 312, 4, 325, 253, 25, 3425, 41, 22],
                   len([2, 123, 2, 31, 312, 4, 325, 253, 25, 3425, 41, 22]), 312))
test_search_array()
