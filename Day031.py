num = int(input("Enter num 1 or 2 or 3 : "))
if num == 1:
    myFile = open("TextDaily.txt","r")
    print(myFile.read())
elif num == 2:
    myFile = open("TextDaily.txt","w")
    nameList = input("Write to Text : ").split(" ")
    myFile.writelines(nameList)
    myFile.close()
elif num == 3:
    myFile = open("TextDaily.txt","a")
    nameList = input("Update to Text : ").split()
    myFile.writelines(nameList)
    myFile.close()
