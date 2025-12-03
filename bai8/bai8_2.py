"""2. Viết chương trình đồ họa sử dụng thư viện turtle, kiểm tra kết quả và giải thích
chương trình
"""
import turtle,random
# ngẫu nhiên 7 màu (ramdom)
colors = ["red", "green", "blue", "orange", "purple", "pink","yellow"]
painter = turtle.Turtle()   # bút vẽ
painter.pensize(3)          # sz bút vẽ = 3
# vòng lặp vẽ 9 lần
for i in range(10):
    color = random.choice(colors) # Chọn bút màu ngẫu nhiên
    painter.pencolor(color)       # đặt màu vẽ cho bút
    painter.circle(100)           # vẽ 1 hình tròn bán kính 1oo
    painter.right(30)             # quay phải 30 độ
    painter.left(60)              # rồi quay trái 60 độ
    painter.setposition(0,0)      # trả rùa về vị trí góc tâm 

turtle.done()
