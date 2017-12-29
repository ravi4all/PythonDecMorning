def calc():
    x = 10
    y = 15
    try:
        if x > y:
            result = x-y
            print(result)
        else:
            # raise ValueError("Some Error")
            print("Some Error")
    except ValueError as err:
        print(err)


calc()
