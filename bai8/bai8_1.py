"""1. Viết chương trình đồ họa sử dụng thư viện turtle, kiểm tra kết quả và giải thích
chương trình"""

# nạp thư viện turtle để có thể vẽ đồ họa
import turtle
# 1. Cài đặt màn hình
window = turtle.Screen() #tạo cửa sổ để hiển thị
window.bgcolor('blue') # màu nền là xANH nhạt
window.title('Vẽ bài 1')

# 2. tạo bút vẽ tên là painter
painter = turtle.Turtle()
painter.fillcolor('blue') #màu tô là xanh dương
painter.pencolor('white')  #màu nét là xanh dương
painter.pensize(3)        # độ dày nét là 3

# 3. Định nghĩa hàm vẽ nét cơ bản
def drawsp(t,s):
    for i in range(4):  # lặp lại 4 lần
        t.forward(s)    # đi thẳng 1 đọn dài s 
        t.left(18)      # rẽ trái 1 góc 18 độ
# 4. Vòng lặp chính     
for i in range (1,180):  # lặp lại 179 lần
    painter.left(18)     # xoay bút sang trái 18 độ so với vị trí cũ
    drawsp(painter, 200) #Gọi hàm trên để vẽ đường cong dài 200 pixel
