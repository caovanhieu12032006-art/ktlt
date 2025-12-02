chuoi = input("Nhập một chuỗi: ")
chuoi_moi = ''.join([ch for ch in chuoi if not ch.isdigit()])
print("Chuỗi sau khi loại bỏ chữ số là:", chuoi_moi)
