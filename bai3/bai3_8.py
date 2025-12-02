import math

x = 0
y = 0

while True:
    s = input("Nhập hướng và số bước (ENTER để dừng): ")
    if not s:
        break
    direction, steps = s.split()
    steps = int(steps)
    if direction.upper() == "UP":
        y += steps
    elif direction.upper() == "DOWN":
        y -= steps
    elif direction.upper() == "LEFT":
        x -= steps
    elif direction.upper() == "RIGHT":
        x += steps

distance = math.sqrt(x**2 + y**2)
print(round(distance))
