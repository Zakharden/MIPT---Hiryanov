_stack = []


def push(x):
    _stack.append(x)
    return print(_stack)


def pop():
    return _stack.pop()



def is_empty():
    if len(_stack) == 0:
        return True
    return False

if __name__ == "__stack_create__":
    import doctest
    doctest.testmod() #будет работать в main(в случае расхождения метода и написанной фуункции)

print(is_empty())
push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())
print(is_empty())
