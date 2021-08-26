num = input()
char_num = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ans = []
for i in num:
    for j in char_num:
        if i==j:
            ans.append(char_num)
print(len(ans))