"""
Nhập hai số nguyên dương để tính ước chung lớn nhất và bội chung nhỏ nhất của chúng
"""

x = int(input('x = '))
y = int(input('y = '))

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('Ước chung lớn nhất của %d và %d là %d' % (x, y, factor))
        print('Bội số chung nhỏ nhất của %d và %d là %d' % (x, y, x * y // factor))
        break