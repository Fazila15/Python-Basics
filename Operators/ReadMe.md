Python Basics:Basic Operators
Welcome back! 👋 In this section, we’ll learn about basic operators in Python. Operators are symbols that perform operations on variables and values. Let’s see how they work! 🔧

 # ===> Arithmetic Operators ➕➖✖️➗

These operators help us do basic math, like addition, subtraction, multiplication.
# Addition
print(x + y)  # Output: 15

# Subtraction
print(x - y)  # Output: 5

# Multiplication
print(x * y)  # Output: 50

# Division
print(x / y)  # Output: 2.0 (Remember, the result is a decimal!)

# Modulus (remainder)
print(x % y)  # Output: 0 (The remainder when dividing x by y)

# Exponentiation (x raised to the power of y)
print(x ** y)  # Output: 100000

 # ===> Comparison Operators 🤔
These operators compare values and return either True or False. They help us make decisions in programs.
# Equal to
print(x == y)  # Output: False (x is not equal to y)

# Not equal to
print(x != y)  # Output: True (x is not equal to y)

# Greater than
print(x > y)   # Output: True (x is greater than y)

# Less than
print(x < y)   # Output: False (x is not less than y)

# Greater than or equal to
print(x >= y)  # Output: True (x is greater than or equal to y)

# Less than or equal to
print(x <= y)  # Output: False (x is not less than or equal to y)


 # ===> Logical Operators 🔎
These operators help us combine conditions and make more complex decisions.
# AND (both conditions need to be true)
print(x > y and z > y)  # Output: True (both are true)

# OR (at least one condition needs to be true)
print(x > y or z < y)   # Output: True (one condition is true)

# NOT (reverses the result)
print(not(x > y))  # Output: False (because x > y is True, NOT makes it False)


 # ===> Assignment Operators ➡️
These operators are used to assign values to variables.
# Plus value in variable.
x += 5  # Add 5 to x (x = x + 5)
print(x)  # Output: 15

# Subtracts value from variable.
x -= 3  # Subtract 3 from x (x = x - 3)
print(x)  # Output: 12

# Variable multiplied by value. 
x *= 2  # Multiply x by 2 (x = x * 2)
print(x)  # Output: 24

# Variable divided by value.
x /= 4  # Divide x by 4 (x = x / 4)
print(x)  # Output: 6.0


 # ===> Identity Operators 🔗
These operators compare the memory locations of two objects.
# 'is' checks if both variables point to the same object in memory
print(x is y)  # Output: False (they are two different objects, even if they look the same)

# 'is not' checks if they point to different objects
print(x is not y)  # Output: True



# Summary 📚
Arithmetic Operators: Do math (addition, subtraction, etc.).
Comparison Operators: Compare values (e.g., is one number greater than another?).
Logical Operators: Combine conditions (AND, OR, NOT).
Assignment Operators: Assign or update values (e.g., +=, -=).
Identity Operators: Compare if two objects are the same (using is or is not).


Great job! 🎉 Now that you know the basics of operators, you can start using them in your programs. Keep practicing, and you'll be a Python pro in no time! 💻🚀
