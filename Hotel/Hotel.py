from tkinter import *
from tkinter import messagebox
import sqlite3
from time import strftime
import random as r

con = sqlite3.connect('HOTEL.db')
cur = con.cursor()

class Hotel:
	def __init__(self,parent):
	#Frameworks
		cur.execute('SELECT * FROM HOTEL')
		self.parent=parent
		self.parent.title('INTERNATIONAL DA DHABA')
		self.mymenu={'Samosa':10,'Vade Pav':5,'Black Cod':20,'Fried Rice':14,'Sushi':30,'Lassi':7}
		self.show_menu=[]
		for i in self.mymenu:
			self.show_menu.append(str(f"{i}--${self.mymenu[i]}"))
		self.frame=Frame(parent)
		self.frame.grid()
		self.frame1=Frame(self.frame,height=250,width=250,borderwidth=3,
		relief=SUNKEN,padx=0,pady=0)
		self.frame1.grid()
		self.total=0
		self.table_total=[]
		for i in range(1,11):
			self.table_total.append(i)
		self.order_placed=False		
		self.order_items=[]  
		self.parent.resizable(False, False)
		self.frame2=Frame(self.frame,height=250,width=250,borderwidth=3,relief=SUNKEN)
		self.frame2.grid(row=1,column=0)
		self.frame2=Frame(self.frame,height=500,width=350,borderwidth=3,relief=SUNKEN)
		self.frame2.grid(row=0,column=1,rowspan=2)
		self.frame3=Frame(self.frame,height=250,width=250,borderwidth=3,
		relief=SUNKEN,padx=0,pady=0)
		self.frame3.grid(row=1,column=0)
		self.tableid=r.randint(1,10)
  
		#TOP LEFT FRAME
		#Menu
		self.choice_menu=StringVar(self.frame1)
		self.choice_menu.set('Choose an option')		
		self.label=Label(self.frame1,text='MENU',font=('Arial',30),relief=RIDGE,bd=6)
		self.label.place(relx=0.1,rely=0.05,width=200)
		self.options=OptionMenu(self.frame1,self.choice_menu,*self.show_menu)
		self.options.config(font=('Arial',14))
		self.options.place(relx=0.5,rely=0.4,anchor='center')
		menu = self.frame1.nametowidget(self.options.menuname)
		menu.config(font=('Arial',13))
		self.buttonadd=Button(self.frame1,text="Add to Order",font=('Arial',14),height='2', width='15',command=lambda:self.add_to_order())
		self.buttonadd.place(relx=0.15,rely=0.6)
  
		#RIGHT SIDE
		#DISPLAY
		int1=IntVar()
		int1.set(10)
		self.label=Label(self.frame2,text='Customer_ID :',font=('Arial',13),padx=6,pady=8)
		self.label.place(relx=0.1,rely=0.02)
		self.labelcustom=Entry(self.frame2,borderwidth=2,width=17,relief='solid',font=('Arial',13),justify=CENTER)
		self.labelcustom.place(relx=0.5,rely=0.02,height=40)
		self.label=Label(self.frame2,text='Table_ID :',font=('Arial',13),padx=6,pady=8)
		self.label.place(relx=0.1,rely=0.12)
		self.labelallot=Label(self.frame2,text=self.tableid,borderwidth=2,height=2,width=16,relief='solid',font=('Arial',13),padx=6,pady=0)
		self.labelallot.place(relx=0.5,rely=0.12,height=40,width=160)
		self.label=Label(self.frame2,text='Date :',font=('Arial',13),padx=6,pady=8)
		self.label.place(relx=0.1,rely=0.22)

		self.labelt=Label(self.frame2,borderwidth=2,width=16,font=('Arial',13),relief='solid',padx=6,pady=8)
		self.labelt.place(relx=0.5,rely=0.22,height=40)
		self.timeupd()
		self.label=Label(self.frame2,text='Order :',font=('Arial',12),padx=6,pady=8)
		self.label.place(relx=0.1,rely=0.30)
		self.labelf=Listbox(self.frame2,borderwidth=2,relief='solid',font=('Arial',13),selectmode=MULTIPLE,justify=RIGHT)
		self.labelf.place(relx=0.3,rely=0.32,width=230,height=156)
		self.label=Label(self.frame2,text='Your Total :',font=('Arial',13),padx=6,pady=8)
		self.label.place(relx=0.49,rely=0.64)
		self.labeltotal=Label(self.frame2,text="$0",borderwidth=2,height=2,width=6,relief='solid',font=('Arial',13),padx=6,pady=0)
		self.labeltotal.place(relx=0.762,rely=0.63)
		self.button=Button(self.frame2,text='DELETE',command=lambda:self.delete_selected())
		self.button.place(relx=0.18,rely=0.74,width=100)
		self.button=Button(self.frame2,text='CLOSE',command=lambda:self.closew())
		self.button.place(relx=0.6,rely=0.74,width=100)
		self.payment=StringVar()
		self.payment.set("Select Payment Option")
		self.options1=OptionMenu(self.frame2,self.payment,'BY CASH','BY CARD', 'BY DIGITAL WALLET')
		self.options1.config(font=('Arial',12))
		self.options1.place(relx=0.5,rely=0.86,anchor='center')
		menu = self.frame2.nametowidget(self.options1.menuname)
		menu.config(font=('Arial',13))
		self.buttonconf=Button(self.frame2,text='CONFIRM',font=('Arial',12),state=DISABLED,command=lambda:self.order_whole())
		self.buttonconf.place(relx=0.15,rely=0.9,width=100)
		self.buttonnew_order=Button(self.frame2,text='NEW ORDER',font=('Arial',12),state=DISABLED,command=lambda:self.new_order())
		self.buttonnew_order.place(relx=0.5,rely=0.9,width=120)
		self.choice_list=StringVar(self.frame2)
		self.choice_list.set(self.labelf.curselection())
        
        #BOTTOM LEFT
		self.table_search=StringVar()
		self.table_search.set('Select Table')
        #DATA DISPLAY
		self.label=Label(self.frame3,text='Table_ID :',font=('Arial',13),padx=6,pady=8)
		self.label.place(relx=0.0,rely=0.12)
		self.options2=OptionMenu(self.frame3,self.table_search,*self.table_total)
		self.options2.config(font=('Arial',11))
		self.options2.place(relx=0.35,rely=0.12,height=40,width=160)
		self.date=Label(self.frame3,text='Date : ',font=('Arial',13),padx=6,pady=8)
		self.date.place(relx=0.0,rely=0.4)
		self.date=Label(self.frame3,text='(DD/MM/YY)',font=('Arial',8))
		self.date.place(relx=0.01,rely=0.52)
		self.datesel1=Entry(self.frame3,justify=CENTER,borderwidth=2,font=('Arial',13),relief='solid')
		self.datesel1.place(relx=0.35,rely=0.4,height=40,width=50)
		self.datesel2=Entry(self.frame3,justify=CENTER,borderwidth=2,font=('Arial',13),relief='solid')
		self.datesel2.place(relx=0.575,rely=0.4,height=40,width=50)
		self.datesel3=Entry(self.frame3,justify=CENTER,borderwidth=2,font=('Arial',13),relief='solid')
		self.datesel3.place(relx=0.795,rely=0.4,height=40,width=50)
		
		self.button=Button(self.frame3,text='SHOW RESULTS SINCE DATE',font=('Arial',11),command=lambda:self.show_results())
		self.button.place(relx=0.05,rely=0.7)

	def timeupd(self):
		self.date=strftime('%d/%m/%y')
		self.time=strftime('%H:%M')
		#self.datet=self.date+" "+self.time
		if self.order_placed!=True:
			self.labelt.config(text=self.date+" "+self.time)
			self.fin_time=str(strftime('%y%m%d')+self.time)
			self.labelt.after(1000*60,self.timeupd)
  
	#GET CHOICE IN THE MENU
	# def rtit(self):
	# 	print(self.choice_menu.get())
 
	# #GET CHOICE IN LIST BOX
	# def rtit(self):
	# 	print(self.labelf.curselection())
	
	def delete_selected(self):
		selected_item= self.labelf.curselection()
		for item in selected_item[::-1]:
			self.labelf.delete(item)
		self.display_total()
		
	def add_to_order(self):
		# if self.payment.get()=='Select Payment Option':
		# 	messagebox.showerror("ERROR",'SELECT PAYMENT OPTION FIRST')
		# 	return
		try:
			if(int(self.choice_menu.get()[self.choice_menu.get().index('$')+1:])>0):
				#self.labelf.insert(END,(str(self.choice_menu.get())+"--$"+str(self.mymenu[str(self.choice_menu.get())])))
				self.labelf.insert(END,str(self.choice_menu.get()))
				#self.total+=self.mymenu[str(self.choice_menu.get())]
				self.display_total()
		except:
			messagebox.showerror('ERROR',"Please select an option before clicking!")  
	def closew(self):
		self.parent.destroy()
	def display_total(self):
		self.items=self.labelf.get(0,END)
		self.total=0
		for i in self.items:
			a=int(i[i.index('$')+1:])
			self.total+=a
		if self.total>0 and self.order_placed==False:
			self.buttonconf.config(state=NORMAL)
		else:
			self.buttonconf.config(state=DISABLED)
		self.labeltotal.config(text='$'+str(self.total))
	def order_whole(self):
		self.customer_id=self.labelcustom.get()		
		if self.customer_id.isnumeric()==False and len(self.customer_id)!=4:
			messagebox.showerror("ID ERROR",'Customer ID must be all numbers and 4 digits')
			return
		if self.payment.get()=='Select Payment Option':
			messagebox.showerror("ERROR",'SELECT PAYMENT OPTION')
			return
		self.final_date=str(self.date)
		for i in self.items:
			a=i[:i.index('--')]
			self.order_items.append(a)
		self.payment_opt=self.payment.get()[3:]
		a=messagebox.askyesno(title='CONFIRMATION',
                    message='Do you want to confirm your order?')
		if a==False:
			return
		cur.execute('''INSERT INTO HOTEL VALUES (?,?,?,?,?,?);''',(int(self.customer_id), int(self.tableid),str(self.order_items), int(self.total), str(self.payment_opt),str(self.fin_time)))
		con.commit()
		self.buttonconf.config(state=DISABLED)
		self.labelcustom.config(state=DISABLED)
		self.buttonadd.config(state=DISABLED)
		self.labelf.config(state=DISABLED)
		self.options.config(state=DISABLED)
		self.choice_menu.set('Choose an option')
		self.order_placed=True
		self.options1.config(state=DISABLED)
		self.payment.set("Select Payment Option")
		self.labeltotal.config(state=DISABLED)
		self.labelallot.config(state=DISABLED)
		self.timestop=str(self.labelt['text'])
		self.labelt.config(text=self.timestop)
		self.labelt.config(state=DISABLED)
		self.buttonnew_order.config(state=NORMAL)
		messagebox.showinfo('ORDER STATUS', 'YOUR ORDER HAS BEEN SUCCESSFULLY PLACED')

		
	def show_results(self):
		if len(self.datesel1.get())!=2 or len(self.datesel1.get())!=2 or len(self.datesel3.get())!=2:
			messagebox.showerror("DATE ERROR",'PLEASE ENTER VALID DATE ACCORDING TO FORMAT')
			return
		try:
			if 0<int(self.datesel1.get())<=31 and 0<int(self.datesel2.get())<=12 and 0<int(self.datesel1.get())<=99:
				self.date_search=self.datesel3.get()+self.datesel2.get()+self.datesel1.get()
			else :
				messagebox.showerror("DATE ERROR",'PLEASE ENTER VALID DATE')
				return
		except:
			messagebox.showerror("ERROR",'PLEASE MAKE SURE FIELDS ARE ENTERED CORRECTLY')
			return
		if self.table_search.get()!='Select Table':
			cur.execute("SELECT * FROM HOTEL WHERE (Table_ID = ? AND Date >= ?) ",(int(self.table_search.get()),str(self.date_search),))
			q=cur.fetchall()
			new= Toplevel(self.parent)
			new.geometry("750x250")
			new.title("Results")
			text1=str()
			label=Label(new,text=text1,justify=LEFT)
			label.pack(anchor='nw')
			total_earn=0
			for i in q:
				total_earn+=i[3]
				date1=i[-1]
				date1=f"{date1[6:]} {date1[4:6]}/{date1[2:4]}/{date1[:2]}"
				text1+=f"Customer ID : {i[0]}; Table : {i[1]}; Order : {i[2]}; Total : ${i[3]}; Date : {date1}\n"
				#text1.set(text2)
				label.config(text=text1)
			label2=Label(new,text="Total Earned : $" + str(total_earn),font=('Arial',18))
			label2.pack(side=BOTTOM)
			
		else:
			messagebox.showerror("ERROR",'PLEASE SELECT A TABLE')
			return
		new.title(f'All Orders since {self.datesel1.get()}/{self.datesel2.get()}/{self.datesel3.get()}')
		self.datesel1.delete(0,END)
		self.datesel2.delete(0,END)
		self.datesel3.delete(0,END)
		self.table_search.set('Select Table')
	def new_order(self):
		b=messagebox.askyesno(title='NEW ORDER PLACEMENT',
                    message='Are you sure you want to place a new order? \nAll your previous data will be lost!')
		if b==False:
			return
		self.buttonconf.config(state=NORMAL)
		self.labelcustom.config(state=NORMAL)
		self.buttonadd.config(state=NORMAL)
		self.labelf.config(state=NORMAL)
		self.options.config(state=NORMAL)
		self.order_placed=False
		self.options1.config(state=NORMAL)
		self.labeltotal.config(state=NORMAL)
		self.labelallot.config(state=NORMAL)
		self.labelt.config(state=NORMAL)
		self.total=0
		a=r.randint(1,10)
		while(a==self.tableid):
			a=r.randint(1,10)
		self.tableid=a
		self.labelf.delete(0,END)
		self.buttonnew_order.config(state=DISABLED)
		self.labelcustom.delete(0,END)
		self.labeltotal.config(text='$0')
		self.labelallot.config(text=self.tableid)
		
		
if __name__=='__main__':
	window=Tk()
	myapp=Hotel(window)
	window.mainloop()
