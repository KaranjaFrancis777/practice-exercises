
def fizz_buzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        elif n % 7 == 0:
            print("Francis")
        else:
            print(n)


# Call the function
fizz_buzz()