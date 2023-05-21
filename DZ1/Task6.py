n = int(input())
a = n % 10
b = n % 100 // 10
c = n % 1000 // 100
d = n % 10000 // 1000
e = n % 100000 // 10000
f = n % 1000000 // 100000
if a + b + c == d + e + f:
    print("yes")
else:
    print("no")