def check_list(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
            else:
                return False

setlist1 = []
setlist2 = []
setlist1,setlist2 = input().split("], [")
print(check_list(setlist1, setlist2))