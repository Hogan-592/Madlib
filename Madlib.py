#This project is to build a madlib.
#The definition of a madlib is a word game where one player prompts another for a list of words to substitute for blanks in a story
#string concatenation (aka how to put strings together)
#suppose we want to create a string that says "subscribe to _____"
#youtuber = "" some string variable

#there are three ways to do this
#1. print("subscribe to " + youtuber)
#2. print("subscribe to {}".format(youtuber))
#3. print(f"subscribe to {youtuber}") - let's use this way in this project

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

# \ indicates telling the computer the line has gone to next one
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
