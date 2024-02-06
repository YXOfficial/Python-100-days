def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1
def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(5,6))
print(gcd(50,200))