status = input("Do you have VIP Status? (True/False): ") == "True"
ticket = input("Do you have a Valid Ticket? (True/False): ") == "True"

if status or ticket:
    print("You are Eligible for VIP Access.")
else:
    print("You are Not Eligible for VIP Access, and you need a Valid Ticket.")
print("END")