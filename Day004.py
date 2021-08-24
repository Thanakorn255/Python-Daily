#Day 004
num = sorted(input())
check_num = ['0','1','2','3','4','5','6','7','8','9']
for i in check_num:
      if num == check_num:
          print("None")
          break
      else:
          check_show = [x for x in check_num if x not in num]
          if len(check_show) != 0:
            Shownum = " ".join(str(x) for x in check_show)
            print(Shownum)
            break


        
