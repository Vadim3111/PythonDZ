import random
from random import randint
num = int(input())
my_list = []
for i in range(num):
    my_list.append(random.randint(0,10))

print(my_list)
num_1 = int(input())
sum = 0
for i in my_list:
    if i == num_1:
        sum += 1
print(sum)
