for i in range(1, 101):
    m3 = True if i % 3 == 0 else False
    m5 = True if i % 5 == 0 else False

    if (m3 and m5):
        print("fizzbuzz")
    elif (m3):
        print("fizz")
    elif (m5):
        print("buzz")
    else:
        print(i)
