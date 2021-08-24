#Day007

v1 = [float(e) for e in input().split()]
v2 = [float(e) for e in input().split()]
if len(v1) != len(v2) :
 print( 'Error' )
else :
 ans = 0
 for i in range(len(v1)) :
    ans += v1[i]*v2[i]
 print(ans)
