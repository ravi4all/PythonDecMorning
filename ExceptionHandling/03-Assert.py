def calc():
    x = 10
    y = 15
    try:
        assert (x > y), "Assertion Error"
        result = x - y

        print(result)
    except AssertionError as err:
        print(err)

calc()
