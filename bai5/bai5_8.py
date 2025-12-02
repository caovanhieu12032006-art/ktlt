def sequential_search(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos += 1
    return found, pos + 1 if found else -1

if __name__== "__main__":
    n= int(input('nhập số phần tử của danh sách:'))
    dlist = []
    for i in range(n):
        x = int(input(f"nhập phần tử thứ {i+1}:"))
        dlist.append(x)

    item = int(input('nhập phần tử cần tìm:'))
    found, position = sequential_search(dlist, item)

    if found:
        print(f"phần tử(item) được tìm thấy tại vị trí {position}.")
    else:
        print(f"phần tử(item) không có trong danh sách.")
