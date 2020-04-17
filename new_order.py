from tkinter import *
import os
import pickle
import sys
import datetime
from tkcalendar import DateEntry
import sqlite3
import init_ADD_ORDERS_options
import load_options
import add_mat_lot, add_mat_type, build_orders_database
import add_loc

def manual_entry():
   if manual_entry_isChecked.get() == True:
      get_id_textbox.grid(column=1, row=4, sticky='ew')
      manual_id_label.grid(column=0, row=4, sticky=E)
      default_value_checkbutton.deselect()    
      
   else:
      default_value_checkbutton.select()
      default_value()
    
    
def default_value():
   if default_value_isChecked.get() == True:
      get_id_textbox.grid_remove()
      manual_id_label.grid_remove()
      manual_entry_checkbutton.deselect()
      
   else:
      manual_entry_checkbutton.select()
      manual_entry()
    
def add_order(event=None):
   global new_order_data, path
   
   valid = True
   
   if manual_entry_isChecked.get() == True:
      new_order_data = get_id_textbox.get()
      
      conn = sqlite3.connect(path +'\\overOrders.db')  
      c = conn.cursor()  
      try:
         current_ids = c.execute('SELECT Generated_ID FROM ORDERS').fetchall()
         if any(new_order_data in i for i in current_ids):
            valid = False         
         
         
      except:
         pass
      
      c.close()
      
      
   else:
      new_order_data = ""
   
   if valid:
      new_order_data = [new_order_data]
      new_order_data.extend((
         PO_textbox.get(),
         PN_textbox.get(), 
         PName_textbox.get(),
         mat_var.get(),
         ml_var.get(),
         DD_cal.get_date(),
         mach_T_textbox.get(),
         DT_textbox.get(),
         IT_textbox.get(),
         OSPT_textbox.get(),
         Pr_textbox.get(),
         loc_var.get()
      ))
      
   
   
      creat_order = build_orders_database.main(new_order_data)
      sys.exit()
      
   else:
      bad_order = Toplevel()
      bad_order.resizable(0, 0)
      bad_order.title("ERROR")
      bad_order.iconbitmap('RMS_Logo.ico')
      bad_order.geometry("300x100")
      bad_order.configure(background='white')
      Label(bad_order, wraplength=300, justify='center', text="The ID number entered is already in use. If you would like to edit the information for this ID, please use the 'Edit Order' function. Otherwise, re-type the desired ID number or select 'DEF'.", font=('Times New Roman', 12), bg='white').grid(row=0, sticky=E)
      
   

def set_material_type(event=None):
   global mat_var
   if mat_var.get() == 'Add Type':
      get_new_mt()
      
def get_new_mt():
   global nmt, get_mt_textbox
   nmt = Toplevel()
   nmt.resizable(0, 0)
   nmt.title("New Material Type")
   nmt.iconbitmap('RMS_Logo.ico')
   nmt.configure(background='white')
   get_mt_textbox = Entry(
       nmt,
      font=('Geneva', 15),
      width=20, 
      borderwidth=0, 
      highlightbackground='black', 
      highlightthickness=0.5)     
   
   add_mt_button = Button(
       nmt, 
      font=('Geneva', 15),
      text="Add Material Type",
      width=17, 
      bg='white',
      activebackground='white', 
      borderwidth=0.5,
      takefocus=1,
      command=add_mt)
   
   Label(nmt, text="New Material Type:", font=('Geneva', 15), bg='white').grid(row=0, sticky=E)

   
   get_mt_textbox.grid(column=1, row=0, sticky='ew')
   add_mt_button.grid(column=1, row=1, sticky=W)    

   get_mt_textbox.bind("<Return>", add_mt)    
   
def add_mt(event=None): 
   global nmt, get_mt_textbox
   new_mat = get_mt_textbox.get()
   
   if new_mat != "":
      new_mat_ar = [new_mat]
      add_mat_type.main(new_mat_ar) 
   
      MT_OptionMenu['menu'].add_command(label=new_mat, command=lambda value=new_mat: mat_var.set(value))
      mat_var.set(new_mat) 
      nmt.destroy()
   
def set_loc(event=None):
   global loc_var
   
   if loc_var.get() == 'Add Location':
      get_new_location()
      
def get_new_location():
   global nlc, get_loc_textbox
   nlc = Toplevel()
   nlc.resizable(0, 0)
   nlc.title("New Location")
   nlc.iconbitmap('RMS_Logo.ico')
   nlc.configure(background='white')
   get_loc_textbox = Entry(
       nlc,
      font=('Geneva', 15),
      width=20, 
      borderwidth=0, 
      highlightbackground='black', 
      highlightthickness=0.5)     
   
   add_loc_button = Button(
       nlc, 
      font=('Geneva', 15),
      text="Add Location",
      width=17, 
      bg='white',
      activebackground='white', 
      borderwidth=0.5,
      takefocus=1,
      command=add_location)
   
   Label(nlc, text="New Location:", font=('Geneva', 15), bg='white').grid(row=0, sticky=E)

   
   get_loc_textbox.grid(column=1, row=0, sticky='ew')
   add_loc_button.grid(column=1, row=1, sticky=W)    

   get_loc_textbox.bind("<Return>", add_location)  
   

def add_location(event=None):
   global nlc, get_loc_textbox
   new_loc = get_loc_textbox.get()
   if new_loc != "":
      new_loc_ar = [new_loc]
      add_loc.main(new_loc_ar)    
      loc_OptionMenu['menu'].add_command(label=new_loc, command=lambda value=new_loc: loc_var.set(value))
      loc_var.set(new_loc) 
   
      nlc.destroy() 
   
def get_material_types():
   
   global options_data
   
   mt_types = ['Select', 'Add Type']
   
   for o in options_data[0]:
      for mt in o:
         mt_types.append(mt)
   
   return mt_types  
   
   
def set_material_lot():
   global options_data
   
   mat_lots = []
   
   for o in options_data[1]:
      for ml in o:
         mat_lots.append(ml)
   
   return mat_lots
  
def get_locs():
   global options_data

   locs = ["Add Location"]

   for o in options_data[2]:
      for l in o:
         locs.append(l)
   return locs  
   
   
   
def focus_next_widget(event):
   event.widget.tk_focusNext().focus()
   return("break")

def load_options():
   global options_data

   try:
      with open('temp.tmp', 'rb') as fp:
         options_data = pickle.load(fp)  

      os.remove('temp.tmp')

   except:
      options_data = ['', '', '']  

path = os.getcwd()

root=Tk()
root.resizable(0, 0)
root.title("Add Order")
root.iconbitmap('RMS_Logo.ico')
root.configure(background='white')

manual_entry_isChecked = IntVar()
default_value_isChecked = IntVar()

options_data = []
load_options()

material_types = get_material_types()
material_lot = set_material_lot()
locs = get_locs()

mat_var = StringVar(root)
ml_var = StringVar(root)
loc_var = StringVar(root)

ml_var.set(material_lot[0])
mat_var.set(material_types[0])
loc_var.set(locs[0])

manual_entry_checkbutton = Checkbutton(
    root, 
    text="Manual Entry", 
    variable=manual_entry_isChecked, 
    command=manual_entry, 
    state=NORMAL, 
    bg='white',
   font=('Geneva', 15))
default_value_checkbutton = Checkbutton(
    root, 
    text="DEF", 
    variable=default_value_isChecked, 
    command=default_value, 
    state=NORMAL,
    bg='white',
   font=('Geneva', 15))

get_id_textbox = Entry(
   root,
   font=('Geneva', 15),
   width=20, 
   borderwidth=0, 
   highlightbackground='black', 
   highlightthickness=0.5) 
PO_textbox = Entry(
   root,
   font=('Geneva', 15),
   width=20,
   borderwidth=0, 
   highlightbackground='black', 
   highlightthickness=0.5)

PN_textbox = Entry(
   root,
   font=('Geneva', 15),
   width=20,
   borderwidth=0, 
   highlightbackground='black', 
   highlightthickness=0.5)

PName_textbox = Entry(
   root,
   font=('Geneva', 15),
   width=20,
   borderwidth=0, 
   highlightbackground='black', 
   highlightthickness=0.5)

MT_OptionMenu = OptionMenu(
   * (root, mat_var) + tuple(material_types),
   command=set_material_type)

MT_OptionMenu.config(
   bg='white', 
   font=('Geneva', 15), 
   borderwidth=0.5, 
   activebackground='white', 
   highlightbackground='black',
   highlightthickness=0.5, 
   takefocus=1)

MT_OptionMenu["menu"].config(
   bg="white")

ML_OptionMenu = OptionMenu(
   *(root, ml_var) + tuple(material_lot))

ML_OptionMenu.config(
   bg='white', 
   font=('Geneva', 15), 
   borderwidth=0.5,
   activebackground='white', 
   highlightbackground='black', 
   highlightthickness=0.5, takefocus=1)

ML_OptionMenu["menu"].config(
   bg="white")

DD_cal = DateEntry(
   root, 
   font=('Geneva', 15),
   width=19, 
   background='black',
   foreground='white', 
   borderwidth=0,
   highlightbackground='black', 
   highlightthickness=0.5,
   firstweekday='sunday',
   selectbackground='black')

mach_T_textbox = Entry(
   root,
   font=('Geneva', 15),
   width=20,
   borderwidth=0, 
   highlightbackground='black', 
   highlightthickness=0.5)

DT_textbox = Entry(
   root,
   font=('Geneva', 15),
   width=20,
   borderwidth=0, 
   highlightbackground='black', 
   highlightthickness=0.5)

IT_textbox = Entry(
   root,
   font=('Geneva', 15),
   width=20,
   borderwidth=0, 
   highlightbackground='black', 
   highlightthickness=0.5)

OSPT_textbox = Entry(
   root,
   font=('Geneva', 15),
   width=20,
   borderwidth=0, 
   highlightbackground='black', 
   highlightthickness=0.5)

Pr_textbox = Entry(
   root,
   font=('Geneva', 15),
   width=20,
   borderwidth=0, 
   highlightbackground='black', 
   highlightthickness=0.5)

loc_OptionMenu = OptionMenu(
   *(root, loc_var) + tuple(locs),
   command=set_loc)

loc_OptionMenu.config(
   bg='white', 
   font=('Geneva', 15),
   borderwidth=0.5, 
   activebackground='white', 
   highlightbackground='black', 
   highlightthickness=0.5,
   takefocus=1, 
)

loc_OptionMenu["menu"].config(
   bg="white")

add_order_button = Button(
   root, 
   font=('Geneva', 15),
   text="Add Order",
   width=17,
   command=add_order, 
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1)

manual_entry_checkbutton.grid(
    column=1, 
    row=0, 
    sticky=E)

default_value_checkbutton.grid(
    column=1, 
    row=0, 
    sticky=W)

                  

PO_textbox.grid(column=1, row=6, sticky='ew')
PN_textbox.grid(column=1, row=7, sticky='ew')
PName_textbox.grid(column=1, row=8, sticky='ew')
mach_T_textbox.grid(column=1, row=12, sticky='ew')
DT_textbox.grid(column=1, row=13, sticky='ew')
IT_textbox.grid(column=1, row=14, sticky='ew')
OSPT_textbox.grid(column=1, row=15, sticky='ew')
Pr_textbox.grid(column=1, row=16, sticky='ew')

DD_cal.grid(column=1, row=11)

MT_OptionMenu.grid(column=1, row=9, sticky='ew')
ML_OptionMenu.grid(column=1, row=10, sticky='ew')
loc_OptionMenu.grid(column=1, row=17, sticky='ew')

add_order_button.grid(column=1, row=20, sticky=W)

manual_id_label = Label(root, text="Manual ID:  ", font=('Geneva', 15), bg='white')

Label(root, text="Create ID:", font=('Geneva', 15), bg='white').grid(row=0, sticky=E)
Label(root, text="PO Number:  ", font=('Geneva', 15), bg='white').grid(column=0, row=6, sticky=E)
Label(root, text="Part Number:  ", font=('Geneva', 15), bg='white').grid(column=0, row=7, sticky=E)
Label(root, text="Part Name:  ", font=('Geneva', 15), bg='white').grid(column=0, row=8, sticky=E)
Label(root, text="Material Type:  ", font=('Geneva', 15), bg='white').grid(column=0, row=9, sticky=E)
Label(root, text="Material Lot:  ", font=('Geneva', 15), bg='white').grid(column=0, row=10, sticky=E)
Label(root, text="Due Date:  ", font=('Geneva', 15), bg='white').grid(column=0, row=11, sticky=E)
Label(root, text="Machining Time:  ", font=('Geneva', 15), bg='white').grid(column=0, row=12, sticky=E)
Label(root, text="Deburr Time:  ", font=('Geneva', 15), bg='white').grid(column=0, row=13, sticky=E)
Label(root, text="Inspection Time:  ", font=('Geneva', 15), bg='white').grid(column=0, row=14, sticky=E)
Label(root, text="OSP Time:  ", font=('Geneva', 15), bg='white').grid(column=0, row=15, sticky=E)
Label(root, text="Price:  $", font=('Geneva', 15), bg='white').grid(column=0, row=16, sticky=E)
Label(root, text="Location:  ", font=('Geneva', 15), bg='white').grid(column=0, row=17, sticky=E)

get_id_textbox.bind("<Tab>", focus_next_widget)
PO_textbox.bind("<Tab>", focus_next_widget)
PN_textbox.bind("<Tab>", focus_next_widget)
PName_textbox.bind("<Tab>", focus_next_widget)
mach_T_textbox.bind("<Tab>", focus_next_widget)
DT_textbox.bind("<Tab>", focus_next_widget)
IT_textbox.bind("<Tab>", focus_next_widget)
OSPT_textbox.bind("<Tab>", focus_next_widget)
Pr_textbox.bind("<Tab>", focus_next_widget)
add_order_button.bind("<Return>", add_order)
MT_OptionMenu.bind("<Tab>", focus_next_widget)
ML_OptionMenu.bind("<Tab>", focus_next_widget)
loc_OptionMenu.bind("<Tab>", focus_next_widget)

default_value_checkbutton.select()

mainloop()

