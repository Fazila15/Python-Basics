# here input will return an string which will cause an error with logical operator so convert input into integar first.
marks = int(input("Your Marks Are? ")) 

if marks >= 90:
    print("You got an A! 🎉")
elif marks >= 80:
    print("You got a B! 😊")
elif marks >= 70:
    print("You got a C! 🙂")
else:
    print("You need to study more. 📚")