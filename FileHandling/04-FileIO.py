file = open('file_1.txt', 'r')

# data = file.readline()
# data = file.readlines()
# print(data[0][7:])

file.seek(15)

data_1 = file.read()
print(data_1)

file.close()
