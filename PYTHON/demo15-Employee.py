n = int(input("Enter number of employees: "))
attendance = []
x = 0  
y = 0  

for i in range(n):
    att = int(input(f"Enter attendance for employee {i+1} (1 for present, 0 for absent): "))
    attendance.append(att)

for att in attendance:
    if att == 1:
        x += 1
    else:
        y += 1

print("Present:", x)
print("Absent:", y)
attendance_percentage = (x / n) * 100 if n > 0 else 0
print(f"Attendance Percentage: {attendance_percentage:.2f}%")

print("Attendance List:")
for i, att in enumerate(attendance, start=1):
    status = "Present" if att == 1 else "Absent"
    print(f"Employee {i}: {status}")    
    