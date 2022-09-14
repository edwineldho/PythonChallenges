def swap(str):
    length = len(str)
    for i in range(length):
        if str[i] in ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            print("haha")

        else:
            print(str[i])

str = str(input("input"))
swap(str)

