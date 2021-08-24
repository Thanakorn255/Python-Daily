a = 0
b = 1
fibo = 0
num = int(input("Enter number of stair steps : "))
for i in range(num):
    fibo = a+b
    a=b
    b = fibo
print("When rabbit moves 1 or 2 steps in each jump")
print("all possible jumping methods = ",fibo)