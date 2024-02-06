"""
xếp hạng bằng điểm số
"""
score = float(input('điểm số: '))
if score >= 90:
    xephang = 'A'
elif score >= 80:
    xephang = 'B'
elif score >= 70:
    xephang = 'C'
elif score >= 60:
    xephang = 'D'
else:
    grade = 'E'
print('điểm số:', xephang)