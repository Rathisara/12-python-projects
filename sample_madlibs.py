"""
Sample Madlibs - Different madlib stories
Each madlib class has a madlib() method that prompts for inputs and prints the story
"""


class hp:
    @staticmethod
    def madlib():
        name = input("Enter a name: ")
        place = input("Enter a place: ")
        adj1 = input("Enter an adjective: ")
        adj2 = input("Enter another adjective: ")
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter another noun: ")
        verb = input("Enter a verb: ")
        
        story = f"Once upon a time, {name} went to {place}. It was a {adj1} and {adj2} place. " \
                f"{name} found a {noun1} and a {noun2}. They decided to {verb} together, " \
                f"and they lived happily ever after!"
        print("\n" + story + "\n")


class code:
    @staticmethod
    def madlib():
        adj = input("Enter an adjective: ")
        verb1 = input("Enter a verb: ")
        verb2 = input("Enter another verb: ")
        noun = input("Enter a noun: ")
        language = input("Enter a programming language: ")
        feeling = input("Enter a feeling: ")
        
        story = f"Computer programming is so {adj}! It makes me so {feeling} all the time because " \
                f"I love to {verb1}. Stay hydrated and {verb2} like you are a {noun}! " \
                f"Learn {language} and become a coding wizard!"
        print("\n" + story + "\n")


class zombie:
    @staticmethod
    def madlib():
        name = input("Enter a name: ")
        weapon = input("Enter a weapon: ")
        place = input("Enter a place: ")
        adj = input("Enter an adjective: ")
        verb = input("Enter a verb: ")
        food = input("Enter a food item: ")
        
        story = f"One dark and stormy night, {name} was walking through {place} with a {weapon}. " \
                f"Suddenly, a {adj} zombie appeared! {name} had to {verb} to survive. " \
                f"In the end, they defeated the zombie and celebrated with {food}!"
        print("\n" + story + "\n")


class hungergames:
    @staticmethod
    def madlib():
        name = input("Enter a name: ")
        district = input("Enter a district number: ")
        weapon = input("Enter a weapon: ")
        skill = input("Enter a skill: ")
        adj = input("Enter an adjective: ")
        verb = input("Enter a verb: ")
        
        story = f"In the Hunger Games, {name} from District {district} must fight for survival. " \
                f"They are skilled with a {weapon} and known for their {skill}. " \
                f"It's a {adj} battle, but {name} must {verb} to become the victor!"
        print("\n" + story + "\n")
