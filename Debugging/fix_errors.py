try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid age.")
    print("Please try again with a numerical value like 25.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")

