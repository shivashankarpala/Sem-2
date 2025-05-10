name = input("Enter Your Name: ")
usn = input("Enter Your USN: ")
marks = []

print("Enter Marks of 3 Subjects: ")

for i in range(3):
    temp = int(input(f"Subject {i + 1}: "))
    marks.append(temp)

total = sum(marks)
percentage = (total / 300) * 100

print(f"Name: {name}")
print(f"USN: {usn}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
