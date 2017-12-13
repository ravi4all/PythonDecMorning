def outer(x):
    print("This is outer...")
    def inner():
        print("This is inner...")
        return x + 1
    def inner2():
        print("This is inner2...")
        return x - 1

    # print(inner())
    return inner2

# print(outer(12)())

x = outer(12)
print(x())
