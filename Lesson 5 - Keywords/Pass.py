for x in range(10):
    if x % 10 == 0:
        print("hello")
    elif x % 15 == 0:
        pass
    elif x % 60 == 0:
        print("bye")
    else:
        print(x)