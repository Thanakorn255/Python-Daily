def factorial(x):
    if x ==1 or x==0:
        return 1
    else:
        return x*factorial(x-1)

num = [int(x) for x in input().split()]
list1 = list()
for i in num:
    list1.append(factorial(i))
print(list1)