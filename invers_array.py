def inver_array_1(A: list):
    """
    Инвертирует массив
    :param A: Начальный массив
    :return: Инвертированный массив
    """
    B = [0]*len(A)
    b_nachalo = 0
    for i in range(len(A)-1,-1,-1):
        B[b_nachalo] = A[i]
        b_nachalo+=1
    return B

def inver_array_2(A: list):
    """
    Инвертирует массив
    :param A: Начальный массив
    :return: Инвертированный массив
    """
    B = [0]*len(A)
    for i in range(len(A)):
        B[i] = A[len(A)-1-i]
    return B

def inver_array_3(A: list):
    """
    Инвертирует массив
    :param A: Начальный массив
    :return: Инвертированный массив
    """
    for i in range(len(A)//2):
        A[i], A[len(A)-1-i] = A[len(A)-1-i], A[i]
    return A

print(inver_array_1([23,3,3,3,23,3,12,312,3,124,12,1]))
print(inver_array_2([23,3,3,3,23,3,12,312,3,124,12,1]))
print(inver_array_3([23,3,3,3,23,3,12,312,3,124,12,1]))

#тернарный оператор "простое" if A[k] else "сложное"