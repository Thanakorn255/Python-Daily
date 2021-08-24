num = []
asnum = []
x = 1
while num!= -1:
    num = int(input())
    asnum.append(num)
  
for i in range(len(asnum)):
    for j in range(len(asnum)):
        if i == j:
            x=x+1
    if x >= (len(asnum)/2):
        print(asnum[i])
        break
    else:
        print("Not found")
        break
       




