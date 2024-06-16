# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function calculates modulus
def modulus(x, y):
    return x % y

print("Select operation from the following: \n1. Add (+)\n2. Subtract (-)\n3. Multiply (*)\n4. Divide (/)\n5. Modulus (%)\n")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4/5) or 'q' to quit: ")
    
    if choice == 'q':
        print("Exiting the calculator.....")
        break
    
    # Check if choice is one of the five options
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))
    else:
        print("Invalid input. Please enter a valid choice.")
