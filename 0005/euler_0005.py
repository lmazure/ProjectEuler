def gcf(a, b):
    if (b > a):
        a, b = b, a
    r  = a % b
    if r == 0:
        return b
    return gcf(b, r)

def lcm(a, b):
    return a * b / gcf(a, b)

limit = 20
solution = 2
for i in range(2, limit + 1):
    solution = lcm(solution, i)
print(solution)
