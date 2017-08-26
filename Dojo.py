from tkinter import*

root = Tk()
root.geometry("1000x500+0+0")
root.title("Dojo Python")

text_input = StringVar()
operator=""

Tops = Frame(root, width = 1600, height = 80, bg = "powder blue", relief = SUNKEN)
Tops.pack(side = TOP)

frame = Frame(root, width = 300, height = 700, bg = "powder blue", relief = SUNKEN)
frame.pack(side = TOP)

lblinfo = Label(Tops, font=("SHOWCRAD GOTHIC", 50, 'bold'), text = "Dojo Python")
lblinfo.grid(row = 0, column = 0)

def btnClick(numero):
	global operator
	operator = operator + str(numero)
	text_input.set(operator)

def btnEval(numero):
	global operator
	result = str(eval(operator))
	text_input.set(operator)
	operator=""

txtDisplay = Entry(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), textvariable = text_input, bg = "gray")
txtDisplay.grid(columnspan = 4)

#123 row
btn1 = Button(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), command = lambda:btnClick(1)).grid(row = 2, column= 0)
btn2 = Button(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), command = lambda:btnClick(2)).grid(row = 2, column= 1)
btn3 = Button(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), command = lambda:btnClick(3)).grid(row = 2, column= 2)

#456 row
btn4 = Button(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), command = lambda:btnClick(4)).grid(row = 3, column= 0)
btn5 = Button(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), command = lambda:btnClick(5)).grid(row = 3, column= 1)
btn6 = Button(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), command = lambda:btnClick(6)).grid(row = 3, column= 2)

#789 row
btn7 = Button(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), command = lambda:btnClick(7)).grid(row = 4, column= 0)
btn8 = Button(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), command = lambda:btnClick(8)).grid(row = 4, column= 1)
btn9 = Button(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), command = lambda:btnClick(9)).grid(row = 4, column= 2)

#Actions row
btnPlus = Button(frame, font=("SHOWCRAD GOTHIC", 50, 'bold'), command = lambda:btnClick("+")).grid(row = 5, column= 1)

root.mainloop()