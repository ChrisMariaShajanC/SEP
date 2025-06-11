Amount = int(input("Enter the amount to withdraw: "))

# Initialize counters for each denomination
x = y = z = w = 0

if Amount < 100:
    print("You cannot withdraw less than 100")
else:
    while Amount >= 100:
        if Amount >= 2000:
            Amount -= 2000
            x += 1
        elif Amount >= 500:
            Amount -= 500
            y += 1
        elif Amount >= 200:
            Amount -= 200
            z += 1
        elif Amount >= 100:
            Amount -= 100
            w += 1
        else:
            print("You cannot withdraw this amount")
            break

    print("2000s:", x)
    print("500s:", y)
    print("200s:", z)
    print("100s:", w)
    print("Total amount withdrawn:", (x * 2000) + (y * 500) + (z * 200) + (w * 100))
    print("Remaining amount in ATM:", Amount)