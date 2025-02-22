#Example 1 : Basic Comparision Operators:
age = int(input ("What is your age: "))
id = input("Do you have your Id: (yes / no )")
if id == 'yes' :
    has_ID = True
else : has_ID = False
if age >= 18 and has_ID:
    print("You can enter the club! 🎉")
else:
    print("Sorry, you can't enter. 🚫")

#Example 2: Using OR Opertor:
weather = input("How's the weather today: (rainy / cloudy)")
if weather == "rainy" or weather == "cloudy":
    print("Take an umbrella! ☂️")
else:
    print("Enjoy the sunshine! ☀️")

#Example 3: Using Not Operator:
is_hungry = input("Are You Hungry: ")

if not is_hungry:
    print("You are not hungry. No need to eat! 🍏")
else:
    print("Go eat something! 🍔")