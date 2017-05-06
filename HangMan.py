import time
import random

name=raw_input("What is Your name ? ")
print 'Hello '+name+' Lets play Hangman'
time.sleep(1)
word_file='name.txt'
print 'Start guessing... '
time.sleep(0.5)
word_list=open(word_file).read().splitlines()
word=word_list.__getitem__(random.randint(0,3))
gusses=""
trials=word.__len__()+5
print 'No. of trials ',+trials
while trials>0:
    fail=0
    for char in word:
        if char in gusses:
            print char
        else:
            print "_"
            fail+=1

    if fail==0:
        print 'Nice...You Won'
        break
    guess=raw_input("Guess...")
    gusses+=guess
    if guess not in word:
        print 'Wrong Choice'
    trials-=1
    print "You have ",+trials," left"
    if trials==0:
        print 'You Lose'
        print "The word is "+word
