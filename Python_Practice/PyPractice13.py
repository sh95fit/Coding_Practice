# tkinter 라이브러리를 활용해 계산기 만들기

import tkinter

def calculate(op):
    if op == '=' :
        result = eval(screen.get())
        screen.set(result)
    elif op == 'c' :
        screen.set('')
    else :
        screen.set(screen.get()+op)

window = tkinter.Tk()

window.title("Calculator")
window.geometry('210x250')

screen = tkinter.StringVar()

display = tkinter.Entry(window, textvariable = screen).place(x=35, y=20)

buttons = [['1','2','3','4'],
          ['5','6','7','8'],
          ['9','0','c','='],
          ['+','-','*','/']]

x1 = 27
y2 = 50
for button in buttons :
    for button_text in button :
        btn = tkinter.Button(window, text = button_text, width=4, height=2,
        command=lambda text=button_text:calculate(text)).place(x=x1,y=y2)
        x1 = x1 + 40
    y2 = y2 + 40
    x1 = 27

window.mainloop()