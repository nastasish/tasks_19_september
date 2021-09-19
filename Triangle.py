
sides = [1, 4, 7, 88, 9,  5, 11, 222, 3, 2, 144]
sorted_sides = sorted(sides)
max1 = abs(sorted_sides[len(sides)-3])
max2 = abs(sorted_sides[len(sides)-2])
max3 = abs(sorted_sides[len(sides)-1])
print(max3, max2, max1)

if max1 + max2 > max3 and max1 + max3 > max2 and max3 + max2 > max1:
    p = int((max1 + max2 + max3)/2)
    s = int((p*(p - max1)*(p - max2)*(p - max3))**(1/2))
    print(s)

