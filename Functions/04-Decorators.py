def parent(x):
    print("This is parent function...")
    def child_1():
        print("This is child function...")

    print(type(x))
    return x

@parent
def func_1():
    print("This is another function...")

#parent(func_1)
func_1()
