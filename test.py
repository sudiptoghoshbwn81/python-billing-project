from My_Module_Feb import add,subtract,multiply,divide
# Main Program
print("===== Simple Calculator =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))

elif choice == 2:
    print("Result:", subtract(num1, num2))

elif choice == 3:
    print("Result:", multiply(num1, num2))

elif choice == 4:
    print("Result:",divide(num1, num2))

else:
    print("Invalid choice!")