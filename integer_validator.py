"""This program ensures that the user inputs a valid integer instead of 
text or symbols, which would otherwise trigger a ValueError"""
try:
    age = int(input("Please enter your age in years: "))
    print(f"Next year, you will be {age + 1} years old.")

except ValueError:
    print("Error: That is not a valid whole number!")
