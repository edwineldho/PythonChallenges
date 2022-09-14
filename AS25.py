
def histogram(cn, array):
    for i in range(cn):
        print(array[i] * "*")
cn = int(input("How many columns would you like on the histogram "))
array = []
for i in range (cn ):
  f = int(input("what number do you want"))
  array.append(f)
histogram(cn, array)
