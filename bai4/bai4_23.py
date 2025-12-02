chuoi = input("nhập câu: ")
chu_cai = 0
chu_so = 0
for ch in chuoi:
    if ch.isalpha():
        chu_cai += 1
    elif ch.isdigit():
        chu_so +=1

print("số chữ cái là:", chu_cai)
print("số chữ số là:", chu_so)