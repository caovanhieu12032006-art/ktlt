chuoi = input("nhập câu: ")
chu_hoa = 0
chu_thuong = 0
for ch in chuoi:
    if ch.isupper():
        chu_hoa += 1
    elif ch.islower():
        chu_thuong += 1
print("chữ hoa:", chu_hoa)
print("chữ thường:", chu_thuong)