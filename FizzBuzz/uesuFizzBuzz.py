for i in range(1,101):
    FB = i % 15
    F  = i % 3
    B  = i % 5
    if FB == 0:
        print("FIZZBUZZ")
    elif F == 0:
        print("FIZZ")
    elif B == 0:
        print("BUZZ")
    else:
        print(i)
