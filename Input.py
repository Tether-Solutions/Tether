#entry widget = textbox that accepts a single line of user input

from tkinter import *
from API import ethPriceReport

def submit():
  input = entry.get()
  if input == 'Price':
    print(ethPriceReport()['priceETH'])
  elif input == '%change':
    print(ethPriceReport()['percentChangeHRLY'] + '%')
window = Tk()

def delete():
  entry.delete(0,END) #deletes the line of text 

submit = Button(window,text='Submit', command=submit)
submit.pack(side = RIGHT) #puts button on window

delete = Button(window,text='Delete', command=delete)
delete.pack(side = RIGHT) #puts button on window

entry = Entry()
entry.config(font=('Arial', 40))
entry.config(bg='#111111')
entry.config(fg='#00FF00')
entry.config(width=10)
entry.pack()
window.mainloop()


