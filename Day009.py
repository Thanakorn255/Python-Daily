#Day 009
a = int(input())
b = int(input())

for i in range(0,4):
    if b>a:
        print("Higher")
        b = int(input())
    elif b<a:
        print("Lower")
        b = int(input())
if b == a:
    print("You Win")
else:
    if b>a:
        print("Higher")
        print("You Lose")
    elif b<a:
        print("Lower")
        print("You Lose")
