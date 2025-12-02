class Romanconverter:
    def __init__(self):
        self.roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
    def to_integer(self, roman):
        total = 0
        prev_value = 0
        for char in reversed (roman):
            value = self.roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value
        return total
converter = Romanconverter()
roman_number = input("Nhập số La Mã: ").upper()  # ví dụ: IX, XIV, MCMXCIV
result = converter.to_integer(roman_number)

print(f"Số nguyên tương ứng với {roman_number} là: {result}")