a = 10
b = 0

try:
    print(a/b)
# except BaseException as ex:
#     print("Some error",ex)
except ZeroDivisionError as ex:
    print(ex)

finally:
    print("Will Always Execute")
