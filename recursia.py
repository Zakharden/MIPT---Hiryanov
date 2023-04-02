# def matryoshka(n):
#     if n==1:
#         print("Матрешечка")
#     else:
#         print("Верх матрешки n=", n)
#         matryoshka(n-1)
#         print("низ матрешки n=", n)
#
# matryoshka(5)

# import graphics as gr
#
# window = gr.GraphWin("Russian game", 600, 600)
# alpha = 0.1
#
#
# def fractal_rectangle(A, B, C, D, deep=10):
#     if deep < 1:
#         return
#     for M, N in (A, B), (B, C), (C, D), (D, A):
#         gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
#     A1 = (A[0] * (1-alpha) + B[0]*alpha, A[1] * (1-alpha) + B[1]*alpha)
#     B1 = (B[0] * (1-alpha) + C[0]*alpha, B[1] * (1-alpha) + C[1]*alpha)
#     C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
#     C1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
#     fractal_rectangle(A1, B1, C1, D1, deep - 1)
#
# fractal_rectangle((100, 100), (500,100), (500,500), (100,500))

# my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))
# my_rectangle.draw(window)

def factorial(n: int):
    assert n >= 0, "Факториал отрицательного не определен"
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(10))


def gcd(a, b):  # в тупую
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b), a > b
    else:  # a < b
        return gcd(a, b - a), b > a


# короткий вариант
def gcd_good(a, b):
    return a if b == 0 else gcd_good(b, a%b)

print(gcd(12,4))
print(gcd_good(68,17))


def pow_a(a, n):
    if n==0:
        return 1
    elif n%2==0: #четн ая степень
        return pow_a(a**2, n//2)
    else:
        return pow_a(a,n-1)*a
    #быстрое возведение в степень

print(pow_a(-2, 12))
print(pow_a(0, 3))
print(pow_a(12, 2))