# ==========================================
# 🧠 Mini Project: Simple Calculator
# ==========================================

# Welcome message
print("🧮 Welcome to the Simple Calculator!")

# Step 1: Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Show available operations
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Step 3: Ask for the user’s choice
choice = input("\nEnter your choice (1/2/3/4): ")

# Step 4: Perform the calculation based on choice
if choice == '1':
    result = num1 + num2
    print(f"\n✅ Result: {num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"\n✅ Result: {num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"\n✅ Result: {num1} × {num2} = {result}")

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"\n✅ Result: {num1} ÷ {num2} = {result}")
    else:
        print("\n❌ Error: Cannot divide by zero!")

else:
    print("\n❌ Invalid choice! Please select 1, 2, 3, or 4.")

# Step 5: End message
print("\n🎯 Thank you for using the Simple Calculator!")
print("Have a nice day!")