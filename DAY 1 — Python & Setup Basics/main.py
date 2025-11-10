# ==========================================
# 🧠 Day 1: Python Basics — Variables, Loops, Lists, Functions
# ==========================================

# -------------------------------
# 🔹 VARIABLES — store values
# -------------------------------
# Python variables are like containers that hold data.
# Common types: string, integer, float, boolean, list, tuple, dictionary etc.

# -------------------------------
# 🔸 STRING — text data
# -------------------------------
Name = "Ali Omar Abdi - AliKey"
print("Your name is:", Name)
print("Type:", type(Name))

# String Methods — modify text
print("Capitalize:", Name.capitalize())
print("Uppercase:", Name.upper())
print("Lowercase:", Name.lower())
print("Title Case:", Name.title())
print("Replace:", Name.replace("Ali", "Omar"))
print("Split into words:", Name.split())
print("Joined back:", " ".join(Name.split()))


# -------------------------------
# 🔸 INTEGER — whole numbers
# -------------------------------
number = 10
print("\nInteger:", number)
print("Type:", type(number))

# 🔸 FLOAT — decimal numbers
decimal_number = 10.5
print("\nFloat:", decimal_number)
print("Type:", type(decimal_number))

# 🔸 BOOLEAN — True or False
isTrue = True
print("\nBoolean value:", isTrue)
print("Type:", type(isTrue))


# -------------------------------
# ➕ MATH OPERATORS — basic math
# -------------------------------
a = 10
b = 5
print("\n--- Math Operators ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (remainder):", a % b)
print("Exponent (power):", a ** b)


# -------------------------------
# ⚖️ COMPARISON OPERATORS
# -------------------------------
print("\n--- Comparison Operators ---")
print("Equal (==):", a == b)
print("Not Equal (!=):", a != b)
print("Greater Than (>):", a > b)
print("Less Than (<):", a < b)
print("Greater or Equal (>=):", a >= b)
print("Less or Equal (<=):", a <= b)


# -------------------------------
# 🔗 LOGICAL OPERATORS
# -------------------------------
print("\n--- Logical Operators ---")
print("AND:", (a > 5 and b < 10))
print("OR:", (a < 5 or b < 10))
print("NOT:", not a < 5)


# -------------------------------
# 🧮 ASSIGNMENT OPERATORS
# -------------------------------
print("\n--- Assignment Operators ---")
x = 10
x += 5
x -= 3
x *= 2
x /= 4
print("Final value of x:", x)


# -------------------------------
# 🧺 LIST — collection of items (can change)
# -------------------------------
fruits = ["apple", "banana", "cherry"]
print("\nFruits list:", fruits)
fruits.append("orange")
print("After adding orange:", fruits)
fruits.remove("banana")
print("After removing banana:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# -------------------------------
# 🎨 TUPLE — collection (cannot change)
# -------------------------------
colors = ("red", "green", "blue")
print("\nColors tuple:", colors)
print("Second color:", colors[1])


# -------------------------------
# 👤 DICTIONARY — key-value pairs
# -------------------------------
person = {
    "name": "Ali",
    "age": 24,
    "country": "Somalia"
}
print("\nPerson:", person)
person["job"] = "IT Support"
print("After adding job:", person)
del person["country"]
print("After removing country:", person)
print("Keys:", person.keys())
print("Values:", person.values())


# -------------------------------
# 🔍 CONDITIONALS — decision making
# -------------------------------
print("\n--- If Statements ---")

age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are underage.")

# If-Elif-Else example
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# Match (switch) statement
print("\n--- Match (Switch) Example ---")
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")


# -------------------------------
# 🔁 LOOPS — repeat actions
# -------------------------------
print("\n--- For Loop ---")
for fruit in fruits:
    print("I like", fruit)

print("\n--- While Loop ---")
count = 1
while count <= 3:
    print("Counting:", count)
    count += 1


# -------------------------------
# ⚙️ FUNCTIONS — reusable blocks of code
# -------------------------------
def greet(name):
    """Say hello"""
    print(f"Hello, {name}! Welcome to Python.")


def add_numbers(a, b):
    """Return the sum of two numbers"""
    return a + b


print("\n--- Functions ---")
greet("AliKey")
result = add_numbers(10, 5)
print("Sum of 10 and 5 is:", result)


# -------------------------------
# ✅ END OF DAY 1
# -------------------------------
print("\n✅ End of Day 1: Python Basics Complete!")
print("You learned variables, data types, operators, lists, tuples, dictionary, conditionals, loops & functions.")
print("Now it's time to start coding! Good luck!")
