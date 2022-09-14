agreement = False
total = 0
num = 0
Input = ""

while agreement == False:
    Input = input("Input bit:")
    for i in range(len(Input)):
        num = int(Input[i])
        total = total + num

    if total%2 == 0:
        agreement = True
        print("vaiid")
    else:
        print("invalid input")
        agreement = False



