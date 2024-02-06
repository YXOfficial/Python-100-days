"""
Xác định xem độ dài cạnh đầu vào có thể tạo thành một hình tam giác hay không và nếu có hãy tính chu vi và diện tích của tam giác
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('chuvi: %f' % (a + b + c))
    p = (a + b + c) / 2
    dientich = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('dientich: %f' % (dientich))
else:
    print('ko thể thành tam giác')