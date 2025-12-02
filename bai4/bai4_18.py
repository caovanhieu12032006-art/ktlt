n = int(input("nhập n: "))
a, b=0, 1
fib = []
while a < n:
    fib.append(a)
    a, b =b, a + b
print("dãy fibonacci nhỏ hơn", n, "là:")
print(fib)