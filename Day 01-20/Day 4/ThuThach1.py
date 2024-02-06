"""
scan xem số nguyên dương có phải là số nguyên tố hay ko
"""
from math import sqrt

num = int(input('số nguyên: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%là số nguyên tố' % num)
else:
    print('%d ko phải là số nguyên tố' % num)