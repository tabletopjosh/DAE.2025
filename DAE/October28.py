# Constant Usage in Variables
PI = 3.14159  # Defining a constant using a descriptive name

# Decision Structures with if-else
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Repetition with while Loops
def count_down(start):
    while start > 0:
        print(start)
        start -= 1
    print("Countdown finished!")

# Sequence Iteration with for Loops
def iterate_collection(collection):
    for item in collection:
        print(item)

# Function Creation and Utilization
def calculate_area(radius):
    """Calculate the area of a circle given a radius."""
    return PI * (radius ** 2)

def main_calculations():
    radius = 5
    area = calculate_area(radius)  # Function call with argument
    print(f"Area of circle with radius {radius}: {area}")

# List Manipulation and Iteration
def list_operations(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)  # Squaring each element
    return squared_numbers

# File Operations
def file_operations():
    filename = "data.txt"
    # Writing data to a file
    with open(filename, "w") as file:
        file.write("Sample data\nLine 2\nLine 3")
    
    # Reading data from a file
    with open(filename, "r") as file:
        content = file.readlines()
        for line in content:
            print(line.strip())

# Exception Handling
def handle_exceptions():
    try:
        result = 10 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print("Division successful.")
    finally:
        print("Execution completed.")

# Execute functions to meet all requirements
print("Constant Usage:")
print("PI =", PI)

print("\nDecision Structure Example:")
print("Check number:", check_number(-5))

print("\nRepetition with while loop:")
count_down(5)

print("\nSequence Iteration with for loop:")
iterate_collection(["apple", "banana", "cherry"])

print("\nFunction Creation and Utilization:")
main_calculations()

print("\nList Manipulation and Iteration:")
numbers = [1, 2, 3, 4, 5]
print("Squared Numbers:", list_operations(numbers))

print("\nFile Operations:")
file_operations()

print("\nException Handling:")
handle_exceptions()
