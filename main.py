from tkinter import *
from datetime import datetime

temp = 0
after_id = ''

def tick():
	global temp, after_id
	after_id = root.after(1000, tick)
	f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
	label1.configure(text=str(f_temp))
	temp += 1


def start_t():
	btn.grid_forget()
	btn2.grid(row=1, columnspan=2, sticky="ew")
	tick()

def stop_t():
	btn2.grid_forget()
	btn3.grid(row=1, column=0, sticky="ew")
	btn4.grid(row=1, column=1, sticky="ew")
	root.after_cancel(after_id)

def continue_t():
	btn3.grid_forget()
	btn4.grid_forget()
	btn2.grid(row=1, columnspan=2, sticky="ew")
	tick()

def reset_t():
	global temp
	temp = 0
	label1.configure(text='00:00')
	btn3.grid_forget()
	btn4.grid_forget()
	btn.grid(row=1, columnspan=2, sticky="ew")


root = Tk()
root.resizable(width=False, height=False)
root.title('StopWatch')
root["bg"] = "#666363"
root.iconbitmap('E:/Projects/QRCODE/second.ico')

label1 = Label(root, width=5, height=1, font=('Ubuntu', 100), text='00:00')
label1.grid(row=0, columnspan=2)

btn = Button(root, text='Start', background="#241f1f", activebackground='#423c3c', foreground='#a69797', relief='flat', font=('Ubuntu', 30), command=start_t)
btn2 = Button(root, text='Stop', background="#241f1f", activebackground='#423c3c', foreground='#a69797', relief='flat', font=('Ubuntu', 30), command=stop_t)
btn3 = Button(root, text='Continue', background="#241f1f", activebackground='#423c3c', foreground='#a69797', relief='flat', font=('Ubuntu', 30), command=continue_t)
btn4 = Button(root, text='Reset', background="#241f1f", activebackground='#423c3c', foreground='#a69797', relief='flat', font=('Ubuntu', 30), command=reset_t)

btn.grid(row=1, columnspan=2, sticky="ew")

root.mainloop()