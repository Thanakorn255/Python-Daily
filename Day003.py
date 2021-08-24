a = []
num = []
while a!=0:
    a = int(input())
    num.append(a)
    if a == 0:
        ma = str(input())
        if ma == "Max" or ma == "max" or ma == "MaX":
            num.sort(reverse=True)
            integers = [str(num) for num in num]
            _integers = " ".join(integers)
            showint = str(_integers)
            print(showint)
        elif ma == "Min" or ma == "min" or ma == "MiN":
            num.sort()
            integers = [str(num) for num in num]
            _integers = " ".join(integers)
            showint = str(_integers)
            print(showint)
    