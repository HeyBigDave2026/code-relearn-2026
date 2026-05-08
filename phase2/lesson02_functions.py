# lesson02_functions.py
# Phase 2 - lesson 2: Functions
# Dave Pruyn, May 2026


# Functions are reusable blocks of code that perform a specific task. They allow us to break down our code into smaller, more manageable pieces, and they can be called multiple times throughout our program.
# --- Basic function ---
def greet(name):
    """This function takes a name as an argument and prints a greeting. It returns a greeting string for the given name."""
    return f"Hello, {name}"

print(greet("Dave"))  # Output: Hello, Dave


# --- Default parameter values ---
def greet_with_title(name, title="Mr."):
    """Greet with an optional title.  Defaults to Mr."""
    return f"Hello, {title} {name}"


print(greet_with_title("Pruyn"))  # Output: Hello, Mr. Pruyn
print(greet_with_title("Pruyn", "Dr."))  # Output: Hello, Dr. Pruyn

# Multiple return values
def calculate_area_and_perimeter(length, width):
    """Calculate the area and perimeter of a rectangle given its length and width."""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

area, perimeter = calculate_area_and_perimeter(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")  # Output: Area: 15, Perimeter: 16

# MORE Multiple return values - from the lesson
def min_max(numbers):
    """Return the minimum and maximum values from a list of numbers in one shot."""
    return min(numbers), max(numbers)

low, high =min_max([3,1,4,5,9,2,6,17])
print(f"Low: {low}, High: {high}")  # Output: Low: 1, High: 17

#Keyword arguments
def describe_prospect(company, revenue, employees=None):
    """Build a prospect summary string."""
    base = f"{company} = ${revenue}M revenue"
    if employees:
        base += f" with {employees} employees"
    return base

# Can pass args by name, order doesn't matter
print(describe_prospect(revenue=500, company="Acme Corp", employees=1200))
print(describe_prospect("TinyStartup", 2))


# --- *args: variable number of arguments ---
def total (*args):
    """Sum any number of values passed in."""
    return sum(args)

print(total(10, 20, 30))  # Output: 60
print(total(1, 2, 3, 4, 5))  # Output: 15

# ---Docstring access at runtimeß
# print(greet.__doc__)
