#Dat 008
num = int(input())
numup = 1000
for i in range(num+1,numup):
    for j in range(2,i):
        if i%j == 0:
            numup+=1
            break
    else:
        print(i)
        break

    
