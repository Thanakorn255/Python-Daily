days = [31,28,31,30,31,30,31,31,30,31,30,31]
ans = 0

day = int(input())
month = int(input())
year = int(input())
year-=543
if (year%400)==0:
    days[1] += 29
if ((year%4)==0) and ((year%100)!=0):
    days[1] += 29
for i in range(month-1) :
    ans += days[i]
ans += day
print(ans)