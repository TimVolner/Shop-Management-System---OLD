from tkinter import *
import os
import pickle
import sys
import datetime
from tkcalendar import DateEntry
import sqlite3
import init_ADD_ORDERS_options
import load_options
import add_mat_lot, add_mat_type, update_orders_database
import add_loc

def set_order_data(event=None):
   
   global data, rms_ids_var, root
   
   selected_id = rms_ids_var.get()
   use_id = []
   use_id.append(selected_id)
   
   try:
      conn = sqlite3.connect(path +'\\overOrders.db')  
      c = conn.cursor()    

      data = c.execute('SELECT * FROM ORDERS where Generated_ID=?', use_id).fetchone()
   
   
      conn.commit()
      conn.close()  
      
      print("1")
      
      date = datetime.datetime.strptime(data[6], '%Y-%m-%d')
      
      print("2")
   
      PO_textbox.delete(0,END)
      PN_textbox.delete(0,END)
      PName_textbox.delete(0,END)    
      mach_T_textbox.delete(0,END) 
      DT_textbox.delete(0,END) 
      IT_textbox.delete(0,END) 
      OSPT_textbox.delete(0,END) 
      Pr_textbox.delete(0,END) 
      
      PO_textbox.insert(0, data[1])
      PN_textbox.insert(0, data[2])
      PName_textbox.insert(0, data[3])
      mat_var.set(data[4])
      ml_var.set(data[5])
      DD_cal.set_date(date)
      mach_T_textbox.insert(0, data[7])
      DT_textbox.insert(0, data[8])
      IT_textbox.insert(0, data[9])
      OSPT_textbox.insert(0, data[10])
      Pr_textbox.insert(0, data[11])
      loc_var.set(data[12])
      
      
      submit_button.config(state=NORMAL)
     
      
   except:
      pass
   
   print(data)

    
def submit_change(event=None):
   global new_order_data, path
   

   new_order_data = [
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
      loc_var.get(),
      rms_ids_var.get()
   ]
      
   
   
   creat_order = update_orders_database.main(new_order_data)
   sys.exit()
              

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
      
      
def get_rms_ids():
   global path
   rms_id_nums = ['Select']
    
   try:
      conn = sqlite3.connect(path +'\\overOrders.db')  
      c = conn.cursor()    
   
      ids = c.execute('SELECT Generated_ID FROM ORDERS').fetchall()
     
      conn.close() 
      
      for i in ids:
         for num in i:
            rms_id_nums.append(num)
   except:
      pass
   
   return(rms_id_nums)   




path = os.getcwd()

root=Tk()
root.resizable(0, 0)
root.title("Edit Order")
root.iconbitmap('RMS_Logo.ico')
root.configure(background='white')


options_data = []
load_options()

rms_ids = get_rms_ids()
material_types = get_material_types()
material_lot = set_material_lot()
locs = get_locs()
data_index = 0
data = []

rms_ids_var = StringVar(root)
mat_var = StringVar(root)
ml_var = StringVar(root)
loc_var = StringVar(root)

rms_ids_var.set(rms_ids[0])
ml_var.set(material_lot[0])
mat_var.set(material_types[0])
loc_var.set(locs[0])

rms_ids_OptionMenu = OptionMenu(
   * (root, rms_ids_var) + tuple(rms_ids),
   command=set_order_data)

rms_ids_OptionMenu.config(
   bg='white', 
   font=('Geneva', 10), 
   borderwidth=0.5, 
   activebackground='white', 
   highlightbackground='black',
   highlightthickness=0.5, 
   takefocus=1)

rms_ids_OptionMenu["menu"].config(
   bg="white")

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

submit_button = Button(
   root, 
   font=('Geneva', 15),
   text="Submit",
   width=17,
   command=submit_change, 
   bg='white',
   activebackground='white', 
   borderwidth=0.5,
   takefocus=1,
   state=DISABLED)


                  

PO_textbox.grid(column=1, row=6, sticky='ew')
PN_textbox.grid(column=1, row=7, sticky='ew')
PName_textbox.grid(column=1, row=8, sticky='ew')
mach_T_textbox.grid(column=1, row=12, sticky='ew')
DT_textbox.grid(column=1, row=13, sticky='ew')
IT_textbox.grid(column=1, row=14, sticky='ew')
OSPT_textbox.grid(column=1, row=15, sticky='ew')
Pr_textbox.grid(column=1, row=16, sticky='ew')

DD_cal.grid(column=1, row=11)

rms_ids_OptionMenu.grid(column=1, row=0, sticky='ew')
MT_OptionMenu.grid(column=1, row=9, sticky='ew')
ML_OptionMenu.grid(column=1, row=10, sticky='ew')
loc_OptionMenu.grid(column=1, row=17, sticky='ew')

submit_button.grid(column=1, row=20, sticky=W)


Label(root, text="Select ID:", font=('Geneva', 15), bg='white').grid(row=0, sticky=E)
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

rms_ids_OptionMenu.bind("<Tab>", focus_next_widget)
PO_textbox.bind("<Tab>", focus_next_widget)
PN_textbox.bind("<Tab>", focus_next_widget)
PName_textbox.bind("<Tab>", focus_next_widget)
mach_T_textbox.bind("<Tab>", focus_next_widget)
DT_textbox.bind("<Tab>", focus_next_widget)
IT_textbox.bind("<Tab>", focus_next_widget)
OSPT_textbox.bind("<Tab>", focus_next_widget)
Pr_textbox.bind("<Tab>", focus_next_widget)
submit_button.bind("<Return>", submit_change)
MT_OptionMenu.bind("<Tab>", focus_next_widget)
ML_OptionMenu.bind("<Tab>", focus_next_widget)
loc_OptionMenu.bind("<Tab>", focus_next_widget)


mainloop()

