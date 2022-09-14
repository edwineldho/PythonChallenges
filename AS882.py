def reverse(string):
    length = len(string)
    for i in range(length):
        print(string[(length -1) -i ] , end = '' )
        # have to put a -1

string = (input("input"))
reverse(string)

#
