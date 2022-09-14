Alphabet = ["A","B","C","D","E","F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Morse = ["._","_..." ,"_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.", "..." , "_", ".._", "..._", ".__", "_.._", "_.__", "__..", ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____.", "_____"]
choose = 0
morse = ""
English = ""
length = 0
x = 0
print("Welcome to the morse code converted")
choose = int(input("Press 1 to convert from morse code to english, Press 2 to convert from english to morse code"))

if choose == 1:
    morse = input("give:")
    length = len(morse)
    for i in range(length):
        x = Morse.index(morse[i])

        print(Alphabet[x])

else:
    English = input("give:")
    length = len(English)
    for i in range(length):
        x = Alphabet.index(English[i])

        print(Morse[x])
