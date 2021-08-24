p = 2
gcd = 1
x = int(input("Enter num1 : "))
y = int(input("Enter num2 : "))
while p<x and p<y:
    if x%p==0 and y%p==0:
        x=x/p
        y=y/p
        gcd = gcd*p
        p = 2
    else:
        p=p+1
print("Greatest common divisor =",gcd)
