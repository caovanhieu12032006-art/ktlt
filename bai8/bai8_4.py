# Dương Phúc Hợp msv: 245752021610047
"""4. Viết chương sử dụng thư viện đồ họa tkinter thực hiện:
a) Xây dựng cửa sổ đồ họa window form
b) Thêm một widget (button) vào window form
c) Xây dựng phương thức xử lý sự kiện phím bấm
d) Thay đổi màu nền và màu chữ của button sử dụng thuộc tính “bg” và “fg”
"""
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Window')   #tiêu đề
window.geometry('500x300')  # kích cỡ
window['bg'] = 'aqua'

# tạo nút
def click():
    print("Bạn đã nhấn vào nút")
    # Hiển thị hộp thoại
    messagebox.showinfo("Bạn vừa click vào nút")
    # thay đổi màu nút sau khi ấn
    btn_action.config(bg='yellow', fg='red', text="đã bấm")

    # tạo nút
btn_action = tk.Button(window , text="Bấm vào đây", font=('time new roman',13),bg="darkblue", fg= "white", command = click)
btn_action.pack(padx=50,pady=50)


window.mainloop()