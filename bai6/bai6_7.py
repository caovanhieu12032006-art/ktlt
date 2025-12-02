class Circle:
    def __init__(self, radius):
        self.radius = radius
    def dientich(self):
        return self.radius * 3.14 ** 2
    def chuvi(self):
        return self.radius * 3.14 * 2
hinh_tron = Circle(5)
print("Diện tích: ", hinh_tron.dientich())
print("Chu vi:", hinh_tron.chuvi())