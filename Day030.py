def check(t):
    show = t
    while show>0:
        show-=1
        for i in range(2,show//2):
            p=(show**2-i**2)**(1/2)
            if p+show+i==t:
                print(show)
                show=0
                break

inp=int(input("Enter Input : "))
check(inp)