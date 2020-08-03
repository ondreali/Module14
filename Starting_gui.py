
"""
program: Starting_gui
Author: Ondrea Li
Last date modfied: 08/02/20

The purpose of this program is to write an database,
collecting the user's name and age into a database.
"""

import tkinter
import sqlite3
from sqlite3 import Error

class InvalidWordException(Exception):
    ''' invalid word exception '''
    pass

class Info_input(object):
    def __init__(self, letter=''):
        word_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
        if not (word_characters.issuperset(letter)):
            raise InvalidWordException

        self.letter = letter

    def add_letters(self, letters):
        """
        :param letters: represents letters in word
        :return: returns letters in dictionary with index
        """
        a = self
        for index, letter in enumerate(letters):
            #assign index to each iterable item
            if letter not in a.dict:
                a.dict[letter] = Info_input(letter)
            a = a.dict[letter]



m = tkinter.Tk()



Fullname= tkinter.StringVar()
Age= tkinter.StringVar()

def create_connection(db):
    """Connect to SQLite database
    :param db: filename of database
    :return: connection if no error, otherwise None
    """
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None

def database(db):
   name1= Fullname.get()
   age= Age.get()
   conn = sqlite3.connect(db)
   with conn:
       cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT, Email TEXT)')
   cursor.execute('INSERT INTO Student (FullName, Email) VALUES(?,?)',(name1,age,))
   conn.commit()


#driver
#size of the layout
m.geometry("500x400")
    #color of background and text
m.configure(bg= "Black")
m.title('Anagram Game')
welcome = tkinter.Label(m, text="Welcome to the Anagram Game!", bg="Black", fg="White", font=5, width=43)
enter_name = tkinter.Label(m, text="Enter your name:", bg="Black", fg="White", font=5)
submit = tkinter.Button(m, text="submit", width=33, bg="Yellow", command=database)
enter_age = tkinter.Label(m, text="Enter your age:", bg="Black", fg="White", font=5)
name = tkinter.Entry(m, textvariable=Fullname, font=('calibre', 11, 'normal'), width=30)
age = tkinter.Entry(m, textvariable=Age)
done = tkinter.Button(m, text="DONE", command= m.destroy)

#layout
welcome.grid(row=0)
enter_name.grid(row=1)
enter_age.grid(row=3)
name.grid(row=2)
age.grid(row=4)
submit.grid(row=5)
done.grid(row=6)




m.mainloop()
if __name__ == '__main__':
   while True:
      word_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
      if not (word_characters.issuperset(letters)):
         raise InvalidWordException
