class ATM:
    def __init__(self, so_du=0):
        self.so_du = so_du

    def kiem_tra_so_du(self):
        print(f"Số dư hiện tại: {self.so_du} VND")

    def gui_tien(self):
        so_tien = int(input("Nhập số tiền muốn gửi: "))
        self.so_du += so_tien
        print(f"Đã gửi {so_tien} VND")

    def rut_tien(self):
        so_tien = int(input("Nhập số tiền muốn rút: "))
        if so_tien > self.so_du:
            print("Không đủ số dư!")
        else:
            self.so_du -= so_tien
            print(f"Đã rút {so_tien} VND")

    def menu(self):
        while True:
            print("\n--- MENU ATM ---")
            print("1. Kiểm tra số dư")
            print("2. Gửi tiền")
            print("3. Rút tiền")
            print("4. Thoát")
            lua_chon = input("Chọn chức năng (1-4): ")

            if lua_chon == '1':
                self.kiem_tra_so_du()
            elif lua_chon == '2':
                self.gui_tien()
            elif lua_chon == '3':
                self.rut_tien()
            elif lua_chon == '4':
                print("Cảm ơn bạn đã sử dụng ATM!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
atm = ATM(100000)  # Khởi tạo với số dư ban đầu là 100.000 VND
atm.menu()
