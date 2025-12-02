hoten = input("Nhập họ và tên: ").strip()
parts = hoten.split()
if len(parts) == 2:
    ho = parts[0]
    ten = parts[1]
    print("Họ:", ho)
    print("Tên riêng:", ten)
else:
    print("Vui lòng nhập đúng định dạng: 'Họ Tên' (mỗi phần chỉ một âm).")
