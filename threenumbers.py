x=input("Enter the first number: ")
y=input("Enter the second number: ")
z=input("Enter the third number: ")
# Determine the largest number
if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = y

# Display the result
print("The largest number is:", largest)