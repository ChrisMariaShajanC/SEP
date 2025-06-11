password=str(input("Set your password: "))
userinput=str(input("Enter your password: "))
for i in range(2):
    if userinput == password:
        print("Password is correct")
        break
    else:
        print("Password is incorrect, try again")
        userinput = str(input("Enter your password: "))
