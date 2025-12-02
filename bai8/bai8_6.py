# Dương Phúc Hợp msv: 245752021610047
"""6. Viết chương trình thực hiện tạo menu theo các bước sau:
Bước 1: Thực hiện tạo mới window form và các menu theo code mẫu
Bước 2: Tiến hành các thay đổi cần thiết để nhận được kết quả các cửa sổ window
có các menu như hình
Bước 3: Thêm các phương thức OpenFile(), Exit(), InsText(), InsPic() thực hiển
hiển thị các thông báo hiển thị ra màn hình các thông báo lựa chọn tương ứng 
"""
from tkinter import *
from tkinter import messagebox

def NewFile():
    messagebox.showinfo("Thông báo", "New File!")

def OpenFile():
    messagebox.showinfo("Thông báo", "Bạn đã chọn: Open File")

def Exit():
    messagebox.showinfo("Thông báo", "Bạn đã chọn: Exit")
    root.quit()

def InsText():
    messagebox.showinfo("Thông báo", "Bạn đã chọn: Insert Text")

def InsPic():
    messagebox.showinfo("Thông báo", "Bạn đã chọn: Insert Picture")

def About():
    messagebox.showinfo("About", "This is a simple example of a menu")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.mainloop()