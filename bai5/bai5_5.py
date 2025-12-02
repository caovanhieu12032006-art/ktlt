def sort_list(lst):
    'Hàm sắp xếp danh sách tăng dần'
    return sorted(lst)

def find_max(lst):
    'hàm tìm phần tử lớn nhất'
    return max(lst)

def find_min(lst):
    'hàm tìm phần tử nhỏ nhất'
    return min(lst)

n= int(input('nhập số lượng phần tử:'))

lst=[]
for i in range(n):
    value = float(input(f"nhập phần tử thứ {i+1}:"))
    lst.append(value)

sorted_lst = sort_list(lst)
max_value = find_max(lst)
min_value = find_min(lst)

print('\nDanh sách ban đầu:', lst)
print('danh sách sau sắp xếp:', sorted_lst)
print('phần tử lớn nhất:', max_value)
print('phần tử nhỏ nhất:', min_value)
       
