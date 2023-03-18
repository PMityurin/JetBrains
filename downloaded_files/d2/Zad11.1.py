def push(n, stack):
    n = int(n)
    print('ok')
    stack.append(n)
    return stack

def pop(stack):
    if len(stack) > 0:
        print(stack[-1])
        stack.pop()
        return stack
    print('error')
    return stack

def back(stack):
    if len(stack) > 0:
        print(stack[-1])
        return stack
    print('error')
    return stack

def size(stack):
    print(len(stack))
    return stack

def clear(stack):
    print('ok')
    stack.clear()
    return stack

dic = {'push':push, 'pop':pop, 'back':back, 'size':size, 'clear':clear}
stack = []
s = [i for i in input().split()]
while s[0] != 'exit':
    if len(s) > 1:
        stack = dic[s[0]](s[1], stack)
    else:
        stack = dic[s[0]](stack)
    s = [i for i in input().split()]
print('bye')