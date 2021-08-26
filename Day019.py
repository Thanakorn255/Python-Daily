high = float(input("Enter high (Metre) : "))
count = 0
while high>0.1:
    high = high*0.9
    count += 1
    print("[#%d]" %count,"High : %.2f" %high)
print("Hit count : ",count)