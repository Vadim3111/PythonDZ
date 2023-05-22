n = int(input())
m = int(input())
k = int(input())
x = n * m
y = x - k 
if y % 2 == 0 or k % 2 == 0:
    print("yes")
else:
    print("no")
