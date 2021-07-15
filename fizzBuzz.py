for i in range(101):
    a = "Fizz" if i%3 == 0 else ""
    b = "Buzz" if i%5 == 0 else ""
    print(f"{i}: {a+b}")