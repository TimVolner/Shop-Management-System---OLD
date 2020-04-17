from tkinter import *
from tkinter import ttk
import os
def new_order():
    os.startfile("new_order.exe")

def edit_order():
    os.startfile("edit_order.exe")
    
    
def router():
    #os.startfile("router.exe")
    print("router")

def location_change():
    #os.startfile("location_change.exe")
    print("location_change")
    
def overview_view():
    #os.startfile("overview_view.exe")
    print("overview_view")
    
def development_schedule():
    #os.startfile("development_schedule.exe")
    print("development_schedule")
    
def production_schedule():
    #os.startfile("production_schedule.exe")
    print("production_schedule")
    
def deburr_schedule():
    #os.startfile("deburr_schedule.exe")
    print("deburr_schedule")
    
def inspection_schedule():
    #os.startfile("inspection_schedule.exe)"
    print("inspection_schedule")
    
def ncr():
    #os.startfile("ncr.exe")
    print("ncr")
    
def c_of_c():
    #os.startfile("c_of_c.exe")
    print("c_of_c")

root = Tk()
root.resizable(0, 0)
root.geometry("400x600+300+100")
root.title("RMS System")
root.iconbitmap('RMS_Logo.ico')
root.configure(background='white')


#create buttons
new_order_button = Button(
   root, 
   font=('Geneva', 20),
   text="New Order",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
   command=new_order)

edit_order_button = Button(
   root, 
   font=('Geneva', 20),
   text="Edit Order",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
    command=edit_order)

router_button = Button(
   root, 
   font=('Geneva', 20),
   text="Create Router",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
    command=router)

location_change_button = Button(
   root, 
   font=('Geneva', 20),
   text="Change Order Location",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
    command=location_change)
overview_view_button = Button(
   root, 
   font=('Geneva', 20),
   text="Overview",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
    command=overview_view)
development_schedule_button = Button(
   root, 
   font=('Geneva', 20),
   text="Development Schedule",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
    command=development_schedule)
production_schedule_button = Button(
   root, 
   font=('Geneva', 20),
   text="Production Schedule",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
    command=production_schedule)
deburr_schedule_button = Button(
   root, 
   font=('Geneva', 20),
   text="Deburr/Clean Schedule",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
    command=deburr_schedule)
inspection_schedule_button = Button(
   root, 
   font=('Geneva', 20),
   text="Inspection Schedule",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
    command=inspection_schedule)
ncr_button = Button(
   root, 
   font=('Geneva', 20),
   text="NCR",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
    command=ncr)
c_of_c_button = Button(
   root, 
   font=('Geneva', 20),
   text="Print C of C",
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
    command=c_of_c)

#format buttons
new_order_button.pack(fill=X)
edit_order_button.pack(fill=X)
router_button.pack(fill=X)
location_change_button.pack(fill=X)
overview_view_button.pack(fill=X)
development_schedule_button.pack(fill=X)
production_schedule_button.pack(fill=X)
deburr_schedule_button.pack(fill=X)
inspection_schedule_button.pack(fill=X)
ncr_button.pack(fill=X)
c_of_c_button.pack(fill=X)


root.mainloop()