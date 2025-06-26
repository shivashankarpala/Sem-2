n = int(input("Enter Number: "))

print("Digit\tFrequency")

for i in range(16):
    count = 0
    num = n
    while num > 0:
        temp = num % 10
        if temp == i:
            count += 1
        num //= 10
    if count > 0:
        print(f"{i}\t{count}")