from fuzzywuzzy import fuzz
from tkinter import *
from functools import partial
import json, requests,urllib.request
from tkinter import messagebox, ttk
win = Tk()
def search(a):
	url="https://raw.githubusercontent.com/jarvis5797/data_/master/data.json"
	data = json.loads(requests.get("https://raw.githubusercontent.com/jarvis5797/data_/master/data.json").text)
	str=(a.get())
	for widget in results.winfo_children():
		widget.destroy()
	if str.lower() in data:
		arr=list(data[str.lower()])
		yax=1
		for i in range (len(arr)):
			label=Label(results,text=arr[i],wraplength=1200,fg='red')
			label.place(x=0,y=yax)
			win.update()
			yax+=100
	elif str.title() in data:
		arr=list(data[str.title()])
		yax=1
		for i in range (len(arr)):
			label=Label(results,text=arr[i],wraplength=1200,fg='red')
			label.place(x=0,y=yax)
			win.update()
			yax+=100
	elif str.upper() in data:
		arr=list(data[str.upper()])
		yax=1
		for i in range (len(arr)):
			label=Label(results,text=arr[i],wraplength=1200,fg='red')
			label.place(x=0,y=yax)
			win.update()
			yax+=100
	else:
		lst=[]
		for i in data:
			if fuzz.ratio(str,i)>80:
				lst.append(i)
		if len(lst)>=1:
			def search_again(b):
				for widget in results.winfo_children():
					widget.destroy()
				str=(b.get())
				arr=list(data[str])
				yaxis=1
				for i in range (len(arr)):
					label1=Label(results,text=arr[i],wraplength=1200,fg='red')
					label1.place(x=0,y=yaxis)
					win.update()
					yaxis+=100
			dym=Label(win,text='Did You Mean...',fg='firebrick')
			dym.place(x=0,y=200)
			b=StringVar()
			search_result=ttk.Combobox(win,width=12,textvariable=b,value=(lst))
			search_result.place(x=150,y=200)
			search_again=partial(search_again,b)
			go=Button(win,text='GO',command=search_again)
			go.place(x=300,y=200)
			win.update()
		else:
			messagebox.showinfo("From jarvis","Not found")
win.title("Dictinary")
win.geometry("1366x768")
results=Frame(win,width=1366,height=400,bd=10,bg="black")
results.place(x=0,y=400)
l1=Label(win,text="Dictionary",font="system 40 bold",fg='red')

l1.place(x=370,y=0)

l2=Label(win,text="Enter the word you want to search : ",font="arial 18",fg='blue')

l2.place(x=2,y=150)

a=StringVar()
e1=Entry(win,textvariable=a)
e1.place(x=500,y=150)
search=partial(search,a)
b1=Button(win,text="Search",command=search,fg='green',activebackground='blue')
b1.place(x=650,y=150)

win.mainloop()
