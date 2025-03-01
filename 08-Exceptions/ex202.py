

flag = True

while flag == True:

    try:
        num = input(("Enter a number:"))
        num+=1
        flag = False

    except :
        print("Error")
        num = ""

