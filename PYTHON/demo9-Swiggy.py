location = bool(input("Enter your location (True/False): ") == "True")
amount = int(input("Enter the amount of food you want to order: "))

if location or amount > 500:
    print("You can order food from Swiggy.")
else:
    print("You cannot order food from Swiggy.")

print("Thank you for using Swiggy!")
