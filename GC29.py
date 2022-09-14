# Write your code here :-)
import random
N_of_student = int(input("How many students"))
Comments = ["Very good", "Good, some improvements needed", "Not bad, many areas require development", "This standard is unacceptable"]
for i in range(N_of_student):
    Teach_comment = random.choice(Comments)
    print (Teach_comment)
