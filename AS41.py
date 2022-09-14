q1 = 0
q2 = 0
q3 = 0
q4 = 0
print("welcome to the quiz")
q1 = int(input("Is there an error in the binary transmission 11101001 using odd parity. Press 1 for yes, 2 for no"))

if q1 == 2:
    print("Correct!")
else:
    print("Wrong, the correct answer is No, because there are an odd number of 1s in this digit, meaning it follows the odd parity method")

q2 = int(input("What is the bit added at the end of 1010101 in order for it to be an even parity bit"))
if q2 == 0:
    print("Correct!")
else:
    print("Wrong, the correct answer is 1, because there are already8 an even number of 1s in th8is digit, and so to keep the 1s and 0s even, a zero should be added at the end")


q3 = int(input("What is the bit added at the end of 1111000 in order for it to be an Odd parity bit"))
if q3 == 1:
    print("Correct!")
else:
    print("Wrong, the correct answer is 1, because there are an even number of 1s in th8is digit, and so to make is odd, a 1 should be added at the end")

q4 = int(input("Is there an error in the binary transmission 10110010 using even parity. Press 1 for yes, 2 for no"))

if q4 == 2:
    print("Correct!")
else:
    print("Wrong, the correct answer is No, because there are an even number of 1s in this digit, meaning it follows the even parity method")


