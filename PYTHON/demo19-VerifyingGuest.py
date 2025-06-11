def verify_guest_lists(guest_list1, guest_list2):
    list1_lower = sorted(name.lower() for name in guest_list1)
    list2_lower = sorted(name.lower() for name in guest_list2)

    if list1_lower == list2_lower:
        print("Lists match")
    else:
        print("Lists do not match")

input1 = input("Enter names for Guest List 1 (comma-separated): ")
input2 = input("Enter names for Guest List 2 (comma-separated): ")

guest_list1 = [name.strip() for name in input1.split(",")]
guest_list2 = [name.strip() for name in input2.split(",")]

verify_guest_lists(guest_list1, guest_list2)
