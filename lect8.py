def gen_numbers(N:int, M:int, prefix = None):
    prefix = prefix or []
    if M==0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        gen_numbers(N, M-1, prefix)
        prefix.pop()

# gen_numbers(2,5)

def search_in(number, prefix):
    """Ищет число number и возвращает True,
       если оно есть"""
    for i in range(len(prefix)):
        if prefix[i] == number:
            return True
    return False


def gen_permutations(N:int, M: int=-1 , prefix = None):
    """Генерация  всех перестановаок N чисел в M позициях,
    с префиксом prefix"""
    M = N if M == -1 else M #по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M==0:
        print(prefix)
        return
    for number in range(1,N+1):
        if search_in(number, prefix):
            continue
        prefix.append(number)
        gen_permutations(N,M-1,prefix)
        prefix.pop()

gen_permutations(3,3)