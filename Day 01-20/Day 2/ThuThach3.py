"""
check xem có phải đó là năm nhuận hay ko (true or false)
"""
nam = int(input('năm: '))
nhuan = nam % 4 == 0 and nam % 100 != 0 or \
          nam % 400 == 0
print(nhuan)