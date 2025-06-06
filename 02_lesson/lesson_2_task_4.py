def fizz_buzz(n):
    for num in range(1, n + 1):
        if num % 3 == 0:
            print("Fizz")
        if num % 5 == 0:
            print("Buzz")
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        else:
            print(num)


print(fizz_buzz(17))
