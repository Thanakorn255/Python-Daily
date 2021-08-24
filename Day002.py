#Day002
num = int(input())
s = []
for i in range(num):
    s.append(input())
checkS = sorted(s)
shows = "\n".join([str(x) for x in checkS])
print("---------------------------------")
print(shows)
