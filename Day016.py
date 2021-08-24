def check_Prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

num = int(input("Input number : "))
list1 = []
while True:
    num += 1
    if check_Prime(num) == True:
        list1.append(num)
    if len(list1) == 2:
        print("Next twin prime:",list1[0],list1[1])
        break


