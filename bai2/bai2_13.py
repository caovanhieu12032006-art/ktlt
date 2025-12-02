a=float(input("nhap he so a:"))
b=float(input("nhap he so b:"))
c=float(input("nhap he so c:"))
import math
if a==0:
    if b==0:
        if c==0:
           print("pt co vo so nghiem.")
        else:
           print("pt vo nghiem.")
    else:
        x=-c/b
        print("pt bac nhat co nghiem: x=",x)
else:

    delta= b**2 - 4*a*c
    if delta<0:
        print("pt vo nghiem.")
    elif delta==0:
        x= -b/(2*a)
        print("pt co nghiem kep: x1=x2=",x)
    else:
        x1= (-b + math.sqrt(delta))/(2*a)
        x2= (-b - math.sqrt(delta))/(2*a)
        print("pt co 2 nghiem phan biet.")
        print("x1=",x1)
        print("x2=",x2)
