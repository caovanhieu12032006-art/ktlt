import numpy as np

#định nghĩa kiểu dư liệu cho từng cột
data_type = [('name', 'S15'),('class', int),('height', float)]

#danh sách sinh viên: (tên, lớp, chiều cao)
students_details = [
    ('james', 5,48.5),
    ('nail', 6, 52.5),
    ('Paul',5, 42.10),
    ('Pit',5, 40.11)
]

#tạo mảng
students = np.array(students_details, dtype=data_type)
#in mảng gốc
print('original array:')
print(students)
# sắp xếp theo chiều cao
sorted_students = np.sort(students, order='height')

print('\nSort by height:')
print(sorted_students)                             
