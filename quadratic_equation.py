a = int(input())
b = int(input())
c = int(input())
d = b*b + 4*a*c

if d > 0:
    x1 = (-b + d**0.5)/2*a
    x2 = (-b - d**0.5)/2*a
    print(x1, x2)
elif d == 0:
    x1 = -b/2*a
    print(x1)

else:
    print("Нет рациональных решений")

