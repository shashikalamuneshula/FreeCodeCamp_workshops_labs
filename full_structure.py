"""This comprehensive example uses the complete exception block architecture:
try: Code that might fail.
except: Runs only if a specific error happens.
else: Runs only if no errors happen in the try block.
finally: Always runs at the end, regardless of errors."""
try:
    number = int(input("Enter a number to double: "))
    result = number * 2

except ValueError:
    print("Error: Invalid numeric input provided.")

else:
    # This executes only if the try block succeeds
    print(f"Success! Double your number is: {result}")

finally:
    # This always executes, useful for cleanups
    print("Thank you for using the doubling program.")
