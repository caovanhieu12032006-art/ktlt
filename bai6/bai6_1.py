class Circle:
    def __init__(self, radius):
        self.radius = radius  # Lưu bán kính vào thuộc tính của đối tượng

    def area(self):
        return 3.14 * self.radius ** 2  # Tính diện tích hình tròn
hinh_tron = Circle(5)  # Tạo đối tượng hình tròn với bán kính 5
print("Diện tích:", hinh_tron.area())  # In ra diện tích
