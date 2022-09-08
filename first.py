# Проверка полиномов f и g на биективность/транзитивность.
# N = 1
# f(x) = 11 - 3x + 2x^2
# g(x) = 13x - 1

def check(z, fun):
    print(f"Полином {z}:\n")

    # биективность
    z_ring = list(range(2**2))
    # print(z_ring)
    [print(f"x = {item}; f(x) = {fun(item) % 4}") for item in z_ring]
    flag = all(fun(item) % 4 in z_ring for item in z_ring)
    print(f'==> биективен: {bool(flag)}\n')

    # транзитивность
    z_ring = list(range(2**3))
    # print(z_ring)
    [print(f"x = {item}; f(x) = {fun(item) % 8}") for item in z_ring]
    flag = all(fun(item) % 8 in z_ring for item in z_ring)
    print(f'==> транзитивен: {bool(flag)}')

# z_f = (2, 3, 7)
# f = lambda x : 2*x**2 + 3*x + 7

z_f = (2, -3, 11)
f = lambda x : 11 - 3*x + 2*x**2

z_j = (13, -1)
j = lambda x : 13*x - 1

check(z_f, f)
print('_'*50)
check(z_j, j)


