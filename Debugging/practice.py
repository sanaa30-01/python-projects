def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 == 0 and year % 400 != 0:
            return False
    else:
        return False




# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0 and number % 5 != 0:
            print("Fizz")
        elif number % 5 == 0 and number % 3 != 0:
            print("Buzz")
        else:
            print(number)


fizz_buzz(15)