from tkinter import *

expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""

	except:
		pass

def all_clear():
	global expression
	expression = ""
	equation.set("")
	

def backspace():
	length = len(expression_field.get())
	expression_field.backspace(length-1, 'end')
	if length == 1:
		expression_field.insert(0,"0")	

if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="grey")
	gui.title("Calculator")
	gui.geometry("325x452")
	equation = StringVar()
	expression_field = Entry(gui, textvariable = equation, fg="grey", bg="white")
	expression_field.grid(columnspan = 4, ipadx = 100)

all_clear = Button(gui, text = 'AC', fg = 'white', bg = 'deep pink', command = all_clear, height = 5, width = 10)
all_clear.grid(row = 2, column = 0)

divide = Button(gui, text = ' ÷ ', fg = 'white', bg = 'black', command = lambda: press("/"), height = 5, width = 10)
divide.grid(row = 2, column = 3)

one = Button(gui, text = ' 1 ', fg = 'white', bg = 'black',
					command = lambda: press(1), height = 5, width = 10)
one.grid(row = 5, column = 0)

two = Button(gui, text = ' 2 ', fg = 'white', bg = 'black',
					command  = lambda: press(2), height = 5, width = 10)
two.grid(row = 5, column = 1)

three = Button(gui, text = ' 3 ', fg = 'white', bg = 'black',
					command = lambda: press(3), height = 5, width = 10)
three.grid(row = 5, column = 2)

four = Button(gui, text = ' 4 ', fg = 'white', bg = 'black',
					command = lambda: press(4), height = 5, width = 10)
four.grid(row = 4, column = 0)

five = Button(gui, text = ' 5 ', fg = 'white', bg = 'black',
					command = lambda: press(5), height = 5, width = 10)
five.grid(row = 4, column = 1)

six = Button(gui, text = ' 6 ', fg = 'white', bg = 'black',
					command = lambda: press(6), height = 5, width = 10)
six.grid(row = 4, column = 2)

seven = Button(gui, text = ' 7 ', fg = 'white', bg = 'black',
					command = lambda: press(7), height = 5, width=10)
seven.grid(row = 3, column = 0)

eight = Button(gui, text = ' 8 ', fg = 'white', bg = 'black',
					command = lambda: press(8), height = 5, width = 10)
eight.grid(row = 3, column = 1)

nine = Button(gui, text = ' 9 ', fg = 'white', bg = 'black',
					command = lambda: press(9), height = 5, width = 10)
nine.grid(row = 3, column = 2)

zero = Button(gui, text = ' 0 ', fg = 'white', bg = 'black',
					command = lambda: press(0), height = 5, width = 10)
zero.grid(row = 6, column = 1)

plus = Button(gui, text = ' + ', fg = 'white', bg = 'black',
				command = lambda: press("+"), height = 5, width = 10)
plus.grid(row = 5, column = 3)

minus = Button(gui, text = ' - ', fg = 'white', bg = 'black',
				command = lambda: press("-"), height = 5, width = 10)
minus.grid(row = 4, column = 3)

multiply = Button(gui, text = ' × ', fg = 'white', bg = 'black',
					command = lambda: press("*"), height = 5, width = 10)
multiply.grid(row = 3, column = 3)

equal = Button(gui, text = ' = ', fg = 'white', bg = 'black',
				command = equalpress, height = 5, width = 10)
equal.grid(row = 6, column = 3)

decimal= Button(gui, text = '.', fg = 'white', bg = 'black',
					command = lambda: press('.'), height = 5, width = 10)
decimal.grid(row = 6, column = 2)

doublezero= Button(gui, text = '00', fg = 'white', bg = 'black',
					command = lambda: press('00'), height = 5, width = 10)
doublezero.grid(row = 6, column = 0)

clear= Button(gui, text = 'C', fg = 'white', bg = 'deep pink', command = backspace, height = 5, width = 10)
clear.grid(row = 2, column = 2)

modulus= Button(gui, text = '%', fg = 'white', bg = 'black',
					command = lambda: press('%'), height = 5, width = 10)
modulus.grid(row = 2, column = 1)

gui.mainloop()
