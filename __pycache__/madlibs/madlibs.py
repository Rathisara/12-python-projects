# madlibs will have a bunch of blank spaces that the user will fill in
# madlibs is solved by using the string concatenation
# suppose we have a story like this:
# "Once upon a time in a land far, far away, there was a king who had a beautiful queen who was the most beautiful woman in the world. The king and the queen had a son who was the most handsome boy in the world. The king and the queen lived happily ever after."
# we want to create a madlibs game that will ask the user for a list of words to fill in the blanks in the story.
# the user will be able to input the words and the program will output the story with the words filled in.
"""
youtuber ="Rathi" #some string variable

#few ways to do this:
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib=f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)"""

from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()