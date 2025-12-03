"""3. Dựa trên các kết quả đạt được từ các chương trình trên hãy viết chương trình hiển
thị hình ảnh đồ họa sau"""

import turtle

# tạo cửa sổ chính
window = turtle.Screen()
window.title("Ve bai 3 sgk")
window.setup(800,700)
window.bgcolor('white')

# các màu sẽ chạy trong bài
colors = ["red","blue","green"]
# tạo bút vẽ
painter = turtle.Turtle()
painter.pensize(3)

# Khởi chạy số lần vẽ
for i in range(12):
    # Sử dụng phép chia lấy dư (%) để chọn màu theo tuần tự 0, 1, 2
    # Khi i=0, lấy màu thứ 0 (blue).
    # Khi i=1, lấy màu thứ 1 (red).
    # Khi i=2, lấy màu thứ 2 (green).
    # Khi i=3, nó quay lại màu thứ 0
    painter.pencolor(colors[i % 3])
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0,0)

turtle.done()
