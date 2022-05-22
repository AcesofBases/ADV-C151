# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:40:15 2022

@author: Ace
"""

from tkinter import *

root = Tk()

root.title("Sales Application")
root.geometry("500x500")

month_label=Label(root)
profits_label=Label(root)
max_prof=Label(root)
min_prof=Label(root)
month=("January","Febuary","March","April","May","June","July","August","September",
       "October","November","December")
profits=(2000,42000,60000,95000,115000,140000,17000,200000,235000,255000,290000,275000)
month_label["text"]="Months " + str(month)
profits_label["text"]="Months " + str(profits)

def function1():
    max_profits=max(profits)
    max_profits_index=profits.index(max_profits)
  

    max_profits_month=month[max_profits_index]
    max_prof["text"]=" The Maximum Profit Of " + str(max_profits) + " Was recorded in the month of " + str(max_profits_month)

def function2():
    min_profits=min(profits)
    min_profits_index=profits.index(min_profits)
    

    min_profits_month=month[min_profits_index]
    min_prof["text"]=" The Minimum Profit Of " + str(min_profits) + " Was recorded in the month of " + str(min_profits_month)

btn=Button(root,text="Show Max Profit Month",command=function1)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
btn1=Button(root,text="Show Min Profit Month",command=function2)
btn1.place(relx=0.5,rely=0.6,anchor=CENTER)

month_label.place(relx=0.5,rely=0.2,anchor=CENTER)
profits_label.place(relx=0.5,rely=0.3,anchor=CENTER)
max_prof.place(relx=0.5,rely=0.5,anchor=CENTER)
min_prof.place(relx=0.5,rely=0.7,anchor=CENTER)


root.mainloop()














#month=("January","Febuary","March")
#print(month.index("Febuary"))
