import os 
a = os.listdir("C:\\Users\\DINESH\\Documents\\Custom Office Templates\\LIA\\DataBase\\NotePad")
for aa in a :
    if ".txt" in aa:
        if "lol" in aa:
            b = open("DataBase\\NotePad\\"+aa,"r")
            print(b.read())
    else:
        print(False)