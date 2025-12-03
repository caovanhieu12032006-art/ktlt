"""5. Sử dụng thư viện tkinter thực hiện:
a) Xây dựng các radio button cho phép thực hiện các lựa chọn khác nhau
b) Thay thế các radio button thành các indicator như hình"""

import tkinter as tk
# tạo cửa sổ
root = tk.Tk()
root.title("Bài tập 5a")
root.geometry('300x250')
# biến lưu trữ giá trị được chọn
v = tk.IntVar()
v.set(1) # mặc định chọn giá trị đầu tiên
# danh sách dữ liệu (tên hiển thị, gtri)
danh_sach = [
    ('python',1),
    ('perl', 2),
    ('java', 3),
    ('C++', 4),
    ('c#', 5)
]

# Hàm xử lý khi đc chọn
def click():
    print(f"Bạn đang chọn ngôn ngữ có ID: {v.get()}")

# tạo nhãn tiêu đề
tk.Label(root, text= " hãy chọn phần mềm bạn cần", justify=tk.LEFT,
         padx=20).pack()
# 3. Vòng lặp tạo Radio Button
# Lưu ý: Đã sửa logic vòng lặp để lấy đúng Tên và Giá trị
for name, val in danh_sach:
    tk.Radiobutton(root, 
                   text=name,       # Hiển thị tên (Python, Java...)
                   padx=20, 
                   variable=v,      # Liên kết với biến v
                   command=click,
                   value=val).pack(anchor=tk.W) # Căn lề trái

root.mainloop()
