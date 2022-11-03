#The Random Insult Generator. You have horrible comebacks, and just keep on getting roasted by everyone.
# This code will help you take your revenge.
# It must ask for the student’s name, and include that when roasting.
# There must be a random generator based upon a list.
import random
name = input("What is your name")
def RandomInsultGenerator(name):
    list = ["abomination", "absolute zero",  "accident" , "acrotomophile" , "addle-brain" , "addle head" , "addle pate" , "airhead",  "alcatote"]
    index = random.randint(0,8)
    sentance = (name + " is" + " an " + list[index])
    print(sentance)

RandomInsultGenerator(name)