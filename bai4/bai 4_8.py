day_tu = input("Nhập dãy các từ (cách nhau bởi dấu cách): ").split()
max_len = max(len(tu) for tu in day_tu)
tu_dai_nhat = [tu for tu in day_tu if len(tu) == max_len]
print("Các từ dài nhất là:", ', '.join(tu_dai_nhat))
print("Độ dài của các từ này là:", max_len)
