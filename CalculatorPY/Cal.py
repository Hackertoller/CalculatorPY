from tkinter import *
import sys
import math
import time
window = Tk()
window.geometry('600x300')
window.title('Calculator')
window.config(bg='gray')
value = StringVar()
XLabel = Label(window,textvariable = value,font="medium").grid(columnspan = 40,row=0,column = 1)
class Start():
    def __init__(self,value,num):
        self.value = value
        self.num = num
    def start(self):
        self.value.set(self.value.get()+self.num)
    def Clear(self):
        self.value.set('')
    def Getting(self):
        self.num = self.value.get()
        try:
            self.value.set(eval(self.num))
        except:
            self.value.set('inifity')
    def Developer(self):
        self.value.set('Developer Is Mr.Rahimi')
btn1 = Button(window,padx=40,text='1',command=Start(value,'1').start,bd=8).grid(row=1,column=0)
btn2 = Button(window,padx=40,text='2',command=Start(value,'2').start,bd=8).grid(row=1,column=1)
btn3 = Button(window,padx=40,text='3',command=Start(value,'3').start,bd=8).grid(row=1,column=2)
btn10 = Button(window,padx=40,text='+',command=Start(value,'+').start,bd=8).grid(row=1,column=3)
btn17 = Button(window,padx=40,text='^',command=Start(value,'**').start,bd=8).grid(row=1,column=4)
btn4 = Button(window,padx=40,text='4',command=Start(value,'4').start,bd=8).grid(row=2,column=0)
btn5 = Button(window,padx=40,text='5',command=Start(value,'5').start,bd=8).grid(row=2,column=1)
btn6 = Button(window,padx=40,text='6',command=Start(value,'6').start,bd=8).grid(row=2,column=2)
btn11 = Button(window,padx=40,text='-',command=Start(value,'-').start,bd=8).grid(row=2,column=3)
btn18 = Button(window,padx=40,text='^2',command=Start(value,'**2').start,bd=8).grid(row=2,column=4)
btn7 = Button(window,padx=40,text='7',command=Start(value,'7').start,bd=8).grid(row=3,column=0)
btn8 = Button(window,padx=40,text='8',command=Start(value,'8').start,bd=8).grid(row=3,column=1)
btn9 = Button(window,padx=40,text='9',command=Start(value,'9').start,bd=8).grid(row=3,column=2)
btn12 = Button(window,padx=40,text='*',command=Start(value,'*').start,bd=8).grid(row=3,column=3)
btn19 = Button(window,padx=40,text='^-1',command=Start(value,'**-1').start,bd=8).grid(row=3,column=4)
btn13 = Button(window,padx=30,text='Clear',command=Start(value,'').Clear,bd=8).grid(row=4,column=0)
btn14 = Button(window,padx=40,text='0',command=Start(value,'0').start,bd=8).grid(row=4,column=1)
btn15 = Button(window,padx=40,text='=',command=Start(value,'').Getting,bd=8).grid(row=4,column=2)
btn16 = Button(window,padx=40,text='/',command=Start(value,'/').start,bd=8).grid(row=4,column=3)
btn20 = Button(window,padx=40,text='sqrt',command=Start(value,'**0.5').start,bd=8).grid(row=4,column=4)
Label(window,text='Please Click Buttons').grid(row=5,column=0,columnspan = 40)
window.mainloop()
