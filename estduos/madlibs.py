#string concatenation (aka how to put string together)
#suppose we want to creat a string that says 'subscribe to __'


#youtuber = "bullet for my valentine" #some string variable

# a few ways to do this
#print("subscribe to " + youtuber)
#print('subscribe to {}'.format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("adjective: ")
verb1 = input('verb: ')
verb2 = input('verb: ')
famous_person = ('famous person: ')


madlib = f"computer programing is so {adj}! It makes me so excited all the time because \n i love to {verb1}. Stay hydrated end {verb2} like you are {famous_person}! "

print(madlib)
