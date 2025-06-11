total = float(input("Enter the subtotal: "))
tax = total * 0.1
discount = 0.05

if total < 100:
    print("total:", total + tax)
else:
    print("total:", total + tax - discount * total)

print("END")
