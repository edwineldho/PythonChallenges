array = [[]]
n = int(input("Input n:"))
m = int(input("Input m:"))
size = n * m
for i in range (size * size):
    array[i].append(".")
    array[i].append("*")
