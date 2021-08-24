def Check_num(num):
    for i in check:
        print(i)
        if num<10:
            return False
        elif i == check[0]:
            if i == check[1]:
                return True
            else:
                return False
        elif i == check[1] or i == check[2] or i == check[3] or i == check[4]:
            return True
            break
num = int(input())
check = str(num)
print(Check_num(num))
