main = True
try:
    file = open('demo.txt')
    if main:
        data = file.read()
        print(data)

except BaseException as ex:
    print(ex)

else:
    print("Inside Else Block")
