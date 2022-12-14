print("\n******************* Python Calculator *******************")


# Function the sum
def add(x, y):
    return x + y


# Function the subtract
def subtract(x, y):
    return x - y


# Function the multiply
def multiply(x, y):
    return x * y


# Function the divide
def divide(x, y):
    return x / y


# Output of Key User
print("\nChoose a number over the desired operation: \n")
print("1 - Sum")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

# Variable of choice
choice = input("\nChoice one option (1/2/3/4): ")

# Variable of numbers
num1 = int(input("\nEnter an fist number: "))
num2 = int(input("\nEnter an second number: "))

# Condition

if choice == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))


elif choice == '2':
    print("\n")
    print(num1, "+", num2, "=", subtract(num1, num2))

elif choice == '3':
    print("\n")
    print(num1, "+", num2, "=", multiply(num1, num2))

elif choice == '4':
    print("\n")
    print(num1, "+", num2, "=", divide(num1, num2))


else:
    print("\nOpção Inválida")

