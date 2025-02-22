# 🐍 Python Basics: If-Else Condition 🤔✅❌
Welcome back! 🎉 Today, we are going to learn about the if-else condition in Python. This helps us make decisions in our code, just like we do in real life! 🌟

# 🤔 What is an If-Else Condition?
Think of it like this:
👉 If it's raining, take an umbrella! ☔
👉 Otherwise, you can go outside freely! 🌞

In Python, we use if and else to make such decisions.

# ===> 📝 1. Basic If Condition ✅
## If Condition
### The if condition checks if something is true. If it's true, Python will run the code inside it.
age = 18

if age >= 18:  # If age is 18 or more
    print("You can vote! 🗳️")  # This will be printed

💡 How it works?
✔️ If the condition age >= 18 is true, it prints "You can vote!".
❌ If the condition is false, Python does nothing (unless we add an else part).

# ===> 📝 2. If-Else Condition ✅❌
## If Else Condition
### The else part runs if the "if" condition is false.
age = 16

if age >= 18:
    print("You can vote! 🗳️")
else:
    print("Sorry, you are too young to vote. 🙁")
💡 How it works?
✔️ If age >= 18 is true, it prints "You can vote!"
❌ Otherwise, it prints "Sorry, you are too young to vote."

# ===> 📝 3. If-Elif-Else Condition 🧐🔄
### Sometimes, we have more than two choices. In that case, we use elif (which means "else if").
## If Elif Else Condition
marks = 85

if marks >= 90:
    print("You got an A! 🎉")
elif marks >= 80:
    print("You got a B! 😊")
elif marks >= 70:
    print("You got a C! 🙂")
else:
    print("You need to study more. 📚")
💡 How it works?
✔️ If marks are 90 or more, print "You got an A!"
✔️ If marks are 80 to 89, print "You got a B!"
✔️ If marks are 70 to 79, print "You got a C!"
❌ Otherwise, print "You need to study more."

# ===> 📝 4. If-Else with Logical Operators (and, or, not) 🔗
### We can combine conditions using and, or, and not.
## If Else with logical operators
#### Example 1 : Basic Comparision Operator:
age = 20
has_ID = True

if age >= 18 and has_ID:
    print("You can enter the club! 🎉")
else:
    print("Sorry, you can't enter. 🚫")
✔️ and means both conditions must be true.

#### Example 2: Using OR Opertor:
weather = "sunny"

if weather == "rainy" or weather == "cloudy":
    print("Take an umbrella! ☂️")
else:
    print("Enjoy the sunshine! ☀️")
✔️ or means at least one condition must be true.

#### Example 3: Using Not Operator:
is_hungry = False

if not is_hungry:
    print("You are not hungry. No need to eat! 🍏")
else:
    print("Go eat something! 🍔")
✔️ not reverses the condition. If is_hungry is False, then not False is True.

# 🎯 Summary
✔️ if → Runs the code if the condition is true.
✔️ else → Runs the code if the condition is false.
✔️ elif → Adds more conditions between if and else.
✔️ and, or, not → Help in combining conditions.

# 🎉 Challenge for You!
Try writing a Python program that checks:
👉 If the temperature is above 30°C, print "It's too hot! Drink water! 🥵"
👉 If the temperature is between 20 and 30°C, print "The weather is nice! 🌤️"
👉 Otherwise, print "It's cold! Wear a jacket! ❄️"
