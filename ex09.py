#  Write a program that reads any integer and displays its multiplication table.

number = int(input("Enter an interger: "))


print(f"Multiplication table for {number}:")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")