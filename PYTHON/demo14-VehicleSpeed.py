speed_log = list(map(int, input("Enter speeds separated by space: ").split()))
print("Speed log:", speed_log)
speed_limit = int(input("Enter the speed limit: "))
violations = 0
while speed_log:
    current_speed = speed_log.pop(0)
    if current_speed > speed_limit:
        violations += 1
        print(f"Speed violation detected: {current_speed} km/h")
print(f"Total number of violations: {violations}")
