🐍 Day 1: Python Basics — Beginner-Friendly Guide
🎯 Learning Goals

Understand variables & data types
Use operators, lists, tuples, dictionaries
Apply conditional statements & loops
Write functions
Complete Simple Calculator mini-project

## 1️⃣ Variables & Data Types

| Type | Example |
|------|---------|
| String | `"Hello World"` |
| Integer | `10` |
| Float | `10.5` |
| Boolean | `True / False` |
| List | `["apple", "banana"]` |
| Tuple | `("red", "green")` |
| Dictionary | `{"name": "Ali", "age": 24}` |

```python
name = "Ali Omar Abdi"
age = 24
is_student = True
```

## 2️⃣ Strings & Methods

```python
name = "Ali Omar Abdi"
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("Ali","Omar"))
print(name.split())
```

## 3️⃣ Numbers & Operators 

```python
a, b = 10, 5

# Math
print(a+b, a-b, a*b, a/b, a**b)

# Comparison
print(a>b, a==b)

# Logical
print(a>5 and b<10, not a<5)
```

## 4️⃣ Collections

### List — Mutable
```python
fruits = ["apple","banana","cherry"]
fruits.append("orange")
print(fruits)
```

### Tuple — Immutable
```python
colors = ("red","green","blue")
print(colors[1])
```

### Dictionary — Key-Value
```python
person = {"name":"Ali","age":24}
person["job"]="IT Support"
print(person)
```

## 5️⃣ Conditional Statements

```python
age = 18
if age >= 18:
    print("Adult")
else:
    print("Underage")
```

## 6️⃣ Loops

### For Loop
```python
for fruit in fruits:
    print(fruit)
```

### While Loop
```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

## 7️⃣ Functions

```python
def greet(name):
    print(f"Hello, {name}!")

def add_numbers(a,b):
    return a+b

greet("AliKey")
print(add_numbers(10,5))
```

## 8️⃣ Mini Project: Simple Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose +, -, *, /: ")

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    if num2 != 0:
        print(num1/num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
```

✅ End of Day 1

Learned variables, data types, operators, collections, loops, functions

Completed Simple Calculator

Ready for Day 2: NumPy for Numerical Computation
```
<<<<<<< HEAD

In this updated version, the code is formatted using Markdown syntax, which is commonly used for readme files. The code is displayed using triple backticks and the appropriate language syntax (`python` in this case). The table is displayed using a pipe-separated format, which is also commonly used in Markdown tables.
=======
>>>>>>> origin/main
