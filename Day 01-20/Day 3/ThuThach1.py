"""
Đổi inch sang cm
"""
value = float(input('Số: '))
unit = input('Đơn vị: ')
if unit == 'in' or unit == 'inch':
    print('%finch = %fcm' % (value, value * 2.54))
elif unit == 'cm' or unit == 'xangtimet=))':
    print('%fcm = %finch' % (value, value / 2.54))
else:
    print('sao lại nhập lung tung v')