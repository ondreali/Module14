"""
program: Final_anagram
Author: Ondrea Li
Last date modfied: 08/02/20

The purpose of this program is to write an anagram game that test the user's ability
to rewrite a jumbled word in 60 seconds and gain as many points as possible.
"""

import tkinter
from tkinter import *
import random
from random import shuffle
from Final import Starting_gui


#Imports the random function

JUMBLED, PLAINTEXT = 0, 1

timeleft = 60

#The wordlist with the unscrambled words
wordlist = ["red", "yellow", "green", "orange", "purple", "math", "cat", "dog", "horses"
            "chicken", "llama", "hello world", "cow", "tiger", "lycee", "durian", "banana",
            "highligter"]
chosenword = random.choice(wordlist) #Makes a variable called chosenword that stores a random word from the wordlist



#this jumbles the letters up
def word_jumble(word):
    letters = list(word)
    random.shuffle(letters)

    return "".join(letters)

#this jumbles the sentence up
def sentence_jumble(w):
    words = w.split()

    random.shuffle(words)

    return " ".join(word_jumble(word) for word in words)



def startGame(event):
    global jumble
    #timer to countdown
    if timeleft == 60:
        countdown()
    guess.focus_set()
    jumble = jumble_list.pop()

    label.config(text="Scrambled Word:" + jumble[JUMBLED],bg="Black", fg="White")

#check the input
def score_game(event):
    global score

    if guess.get().lower() == jumble[PLAINTEXT].lower():
        #correct answer, gains 1 point
        score += 1
        score_display.config(text="score : " +str(score))

        if jumble_list:
            score_display.after(500, startGame)
        else:
            m.unbind('<Return>')



shuffle(wordlist)

jumble_list = [(sentence_jumble(title), title) for title in wordlist]
score= 0
jumble = None

#timer function
def countdown():
    global timeleft

    # if a game is in play
    if timeleft > 0:

        # decrement the timer.
        timeleft -= 1

        # update the time left label
        timeLabel.config(text = "Time left: " + str(timeleft))

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)






m = tkinter.Tk()
#clear button to delete text
def clearTextInput():
    anagram_entry.delete(0, END)





m.geometry("600x400")
m.configure(bg= "Black")
anagram_var = tkinter.StringVar()
#constructors
m.title('Anagram Game')
please_enter = tkinter.Label(m, text="Enter an Anagram you see fit", bg="Black", fg="White", font = ('Helvetica', 15))
anagram_entry= tkinter.Entry(m, textvariable=anagram_var, font=('calibre', 15, 'normal'), width=20)
timeLabel = tkinter.Label(m, text="Time left: " +str(timeleft), bg="Black", fg="White")
enter_to_start = tkinter.Label(m, text="Press enter to start", font = ('Helvetica', 15), bg="Black", fg="White")
score_display = tkinter.Label(m, text="score: " + str(score))
label = tkinter.Label(m, bg="Black", fg="White", font=("Helvetica", 30))
clear_button = tkinter.Button(m, height=1, width=10, text="Clear", command=clearTextInput)


#location
please_enter.grid(row=1)
anagram_entry.grid(row=7)
timeLabel.grid(row=6)
label.grid(row=5)
score_display.grid(row=4)
enter_to_start.grid(row=3)
clear_button.grid(row=8)


#type in anagram


# run the 'startGame' function
# when the enter key is pressed


# set focus on the entry box
guess = tkinter.Entry(m)
guess.focus_set()

m.bind('<Return>', score_game)
m.bind('<Return>', startGame)

m.mainloop()

if __name__ == '__main__':
