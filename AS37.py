string = input("input")
array = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

for i in range (len(string)):
    if string[i] in array:
        print(string[i] + "o" + string[i], end = '')
    else:
        print(string[i], end = '')
