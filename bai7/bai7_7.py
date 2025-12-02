def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print("Số dòng trong file là:", len(lines))

# Gọi hàm với đường dẫn file
count_lines('D:/a.txt')
