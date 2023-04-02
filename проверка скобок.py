import stack_create as A_stack


stroka = input("Введите строку со скобками: ")

def check_string(stroka):
    shet=0
    for symb in stroka:
        if symb=="(":
            shet+=1
        if symb == ")":
            shet-=1
        if shet <0:
            return print("Неправильная последовательность")
    return print("Последовательность - ОК!")

check_string(stroka)
#через стэк для разных скобок

def is_braces_sequence_correct(stroka):
    """Проверяет корректность скобочной последовательности"""
    for brace in stroka:
        if brace in "()[]":
            continue
        if brace in "([":
            A_stack.push(barce)
        else:
            assert brace in ')]', "Ожидалась закрывающая скобка скобка" + str(brace)
            if A_stack.is_empty():
                return False
            left = A_stack.pop()
            assert left in '([', "Ожидалась открывающая скорбка" + str(brace)
            if left=='(':
                right = ')'
            elif left == '[':
                right = ']'
            if right != brace:
                return False
    return A_stack.is_empty()

is_braces_sequence_correct(stroka)





