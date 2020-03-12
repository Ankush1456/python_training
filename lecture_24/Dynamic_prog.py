def fibo(n):
    if n<2:
        return n
    res = fibo(n-1)+fibo(n-2)
    return res

print(fibo(10))


def fiboDp(n):
    if n<2:
        return n

    if memory.get(n):
        return memory.get(n)

    res = fiboDp(n-1, memory)+fiboDp(n-2, memory)
    memory[n] = res
    return res

print(fiboDp(50, {}))