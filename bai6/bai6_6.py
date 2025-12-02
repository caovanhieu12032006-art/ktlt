class MyString:
    def __init__(self):
        self.text = ""

    def get_String(self):
        self.text = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.text.upper())
s = MyString()
s.get_String()       # Nhập: hello world
s.print_String()     # Kết quả: HELLO WORLD
