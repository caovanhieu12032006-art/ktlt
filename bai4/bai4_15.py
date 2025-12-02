chuoi = input("nhập chuỗi số các từ tiếng anh:")
ds = chuoi.split()
ds.sort()
print("Các từ theo thứ tự từ điển:")
for w in ds:
    print(w)
