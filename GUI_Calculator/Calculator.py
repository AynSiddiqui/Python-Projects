from tkinter import *
from tkinter import messagebox
import math as m
class Ayaan_calci:
    "Programme for GUI using OOP"
    def __init__(self,parent):
    #Frameworks
        self.parent=parent
        self.parent.title("Ayaan's Calculator")
        
        #Label info
        self.label = Label(window,
                           text = 'Welcome Ayaan!',
                            font=('Californian FB',45,'bold'),
                            fg='white',
                            bg='black',
                            relief=SUNKEN,
                            bd=10,
                            padx=20,
                            pady=10,)
        self.label.grid()
        self.frame=Frame(parent)
        self.frame.grid()
        
        #Model
        self.exp="" 
        
        #Text Box info
        self.t=Label(self.frame,width="40", text=self.exp,height='2',font=("Arial",16,'bold'))
        self.t.grid(columnspan=6)
        
        #Button info        
        self.button=Button(self.frame,text="1",height='5', width='10', command=lambda: self.addto(1))
        self.button.grid(row=1,column=0)
        self.button=Button(self.frame,text="2",height='5', width='10', command=lambda: self.addto(2))
        self.button.grid(row=1,column=1)
        self.button=Button(self.frame,text="3",height='5', width='10', command=lambda: self.addto(3))
        self.button.grid(row=1,column=2)
        self.button=Button(self.frame,text="4",height='5', width='10', command=lambda: self.addto(4))
        self.button.grid(row=2,column=0)
        self.button=Button(self.frame,text="5",height='5', width='10', command=lambda: self.addto(5))
        self.button.grid(row=2,column=1)
        self.button=Button(self.frame,text="6",height='5', width='10', command=lambda: self.addto(6))
        self.button.grid(row=2,column=2)
        self.button=Button(self.frame,text="7",height='5', width='10', command=lambda: self.addto(7))
        self.button.grid(row=3,column=0)
        self.button=Button(self.frame,text="8",height='5', width='10', command=lambda: self.addto(8))
        self.button.grid(row=3,column=1)
        self.button=Button(self.frame,text="9",height='5', width='10', command=lambda: self.addto(9))
        self.button.grid(row=3,column=2)
        self.button=Button(self.frame,text="0",height='5', width='10', command=lambda: self.addto(0))
        self.button.grid(row=4,column=1)
        self.button=Button(self.frame,text=".",height='5', width='10', command=lambda: self.addto("."))
        self.button.grid(row=4,column=0)
        self.button=Button(self.frame,text="del",height='5', width='10', command=lambda: self.back())
        self.button.grid(row=1,column=3)
        self.button=Button(self.frame,text="-",height='5', width='10', command=lambda: self.addto("-"))
        self.button.grid(row=2,column=3)
        self.button=Button(self.frame,text="/",height='5', width='10', command=lambda: self.addto("/"))
        self.button.grid(row=3,column=3)
        self.button=Button(self.frame,text="*",height='5', width='10', command=lambda: self.addto("*"))
        self.button.grid(row=4,column=3)
        self.button=Button(self.frame,text="C",height='5', width='24', command=lambda: self.clear())
        self.button.grid(row=1,column=4,columnspan=2)
        self.button=Button(self.frame,text="x\u00b2",height='5', width='10', command=lambda: self.addto("\u00b2"))
        self.button.grid(row=2,column=4)
        self.button=Button(self.frame,text="+",height='5', width='10', command=lambda: self.addto("+"))
        self.button.grid(row=3,column=4)
        self.button=Button(self.frame,text="=",height='5', width='24', command=lambda: self.calc())
        self.button.grid(row=4,column=4,columnspan=2)
        self.button=Button(self.frame,text="x^½",height='5', width='10', command=lambda: self.addto("^½"))
        self.button.grid(row=4,column=2)
        self.button=Button(self.frame,text="(",height='5', width='10', command=lambda: self.addto("("))
        self.button.grid(row=2,column=5)
        self.button=Button(self.frame,text=")",height='5', width='10', command=lambda: self.addto(")"))
        self.button.grid(row=3,column=5)
        self.button=Button(self.frame,text="sin(",height='5', width='10', command=lambda: self.addto("sin("))
        self.button.grid(row=5,column=0)
            
    def addto(self, dig): 
        self.counter=0
        if dig=="^½":
            self.counter+=1
        self.exp=self.exp+str(dig)
        self.update_label()
        
    def sinf(self):
    	if self.exp[-1]!=")":
    	     messagebox.showerror("ERROR!","Please ensure correct use of brackets!")
    	     return False
    	self.exp=self.exp[4:-1]
    	print(self.exp)
    	self.exp=str(m.sin(m.radians(eval(self.exp))))
    	return True
    def calc(self):
        if self.sinf()!=True:
            self.exp=""
            self.update_label()
            return
        if self.counter>0 and self.validsqrt()!=True:
            messagebox.showerror("ERROR!","Negative Square Root is invalid!")
            self.exp=""
            self.update_label()
            return
        self.exp=self.exp.replace("\u00b2","**2")
        self.exp=self.exp.replace("^½","**0.5")
        self.exp=self.exp.replace(f")(",f")*(")
        for i in range(0,10):
            self.exp=self.exp.replace(f"{i}(",f"{i}*(") 
            self.exp=self.exp.replace(f"){i}",f")*{i}") 
        if self.exp=="" or self.exp=="\n":
            messagebox.showerror("ERROR!","Please enter an expression!")  
        else:
            try:
                self.exp=str(eval(self.exp))
            except:
                messagebox.showerror("ERROR!","INVALID EXPRESSION! Please Try Again")
                self.exp=""
        self.update_label()

    def validsqrt(self):
        a=0
        b=0
        c=0
        index=0
        x=0
        for i in range(self.counter):
            x=1
            index = self.exp.index('^½')
            for j in range(index,0,-1):
                if self.exp[j]==")":
                    a+=1
                elif self.exp[j]=="(":
                    b+=1
                if a==b and a>0:
                    c=j
                    break
        if x>0 and eval(self.exp[c:index])>=0:
            return True
        index = self.exp.index('^½')
        if self.exp[index-1]!=")":
            return True
        return False
                                
    def clear(self):
        self.exp=""        
        self.update_label()        
        
    def back(self):
        self.exp=self.exp[:-1]
        self.update_label()
        
    def update_label(self):
        self.t["text"]=self.exp
   
if __name__=='__main__':
    window=Tk()
    myapp=Ayaan_calci(window)
    window.mainloop()
