lst = []

n= int(input('nhap so lượng phần tử:'))
for i in range(n):
    value = float(input(f"nhập phần tử thứ {i+1}:"))
    lst.append(value)

max_value = max(lst)
min_value = min(lst)

#tìm vị trí (index) của chúng
max_index = lst.index(max_value)
min_index = lst.index(min_value)

print('\ndanh sách:', lst)
print(f"phần tử lớn nhât: {max_value} ở vị trí {max_index}")
print(f"phần tử nhỏ nhất: {min_value} ở vị trí {min_index}")
