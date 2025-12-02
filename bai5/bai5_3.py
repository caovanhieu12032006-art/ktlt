def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    return sum(values) / len(values)

values = [2, 4, 6, 8, 10]

print('squares:')
for v in values:
    print(square(v))

print('cubes:')
for v in values:
    print(cube(v))

print('average:',average(values))
#---datetime example---
import datetime as dt

fmt = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', fmt)

print('\ndatetime example:')
print('day:', t1.day)
print('month:', t1.month)
print('minute:', t1.minute)
print('second:', t1.second)

t2 = dt.datetime.now()
diff = t2 - t1
print('how many days difference?', diff.days)

# ---numpy example---
#lưu ý: cần cài numpy trước: pip install numpy
try:
    import numpy as np
    x = np.arange(12, 38)  #12..37
    print('\nNumpy array from 12 to 37:')
    print(x)
except ImportError:
    print('\nNumpy is not installed. Install with: pip install numpy')
