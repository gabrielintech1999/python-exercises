# Write a program that reads a value in meters and displays it converted to centimeters and millimeters.


meters = float(input("Enter a value in meters: "))


centimeters = meters * 100
milimeters = meters * 1000


print(f"{meters} meters is equivalent to  {centimeters} centimeters.")
print(f"{meters} meters is equivalent to  {milimeters} milimeters.")