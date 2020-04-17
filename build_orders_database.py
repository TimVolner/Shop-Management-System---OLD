import sqlite3
import os
import datetime
import sys
import pickle

def create_table(c):
    
    try:
        # Create table - ORDERS
        c.execute('''CREATE TABLE ORDERS(
        [Generated_ID] TEXT PRIMARY KEY,
        [PO_Number] integer, 
        [PART_NUMBER] text, 
        [PART_NAME] text, 
        [MATERIAL_TYPE] text, 
        [MATERIAL_LOT] text, 
        [DUE_DATE] date, 
        [MACH_TIME] integer, 
        [DEBURR_TIME] integer, 
        [INSPECTION_TIME] integer, 
        [OSP_TIME] integer, 
        [PRICE] integer,
        [LOCATION] text
        )''')
        
    except:
        pass    
    
def get_id(data, c):    
    
    if data[0] == "":
    
        #Define Variables for Use
        now = datetime.datetime.now()
        now_year = str(now.year)[2:]
        item_int = 0
        new_id = ''
        all_info = []
        all_info = c.execute('SELECT Generated_ID FROM ORDERS').fetchall()
    
        #Determine the current greated ID Number
        if all_info != []:
            for item in all_info:
                if int(str(item[0][7:])) > item_int:
                    item_int = int(str(item[0][7:]))
    
        else:        
            item_int = 0
   
        #Create New ID Number Using the Current Year as the Beginning Digits and 
        #ending with a number which is 1 higher than most recent ID Number
        new_id = "RMS " + now_year + "-" + '{:06d}'.format((item_int + 1))
        
        #Return the created ID to set the "ID" variable
        data[0] = new_id
        
    compile_data(data, c)
    
def ObtainDate():
    
    
    isValid=False
    
    #Determine whether input value for Date is a valid Date
    while not isValid:
        userIn = raw_input("Due Date mm/dd/yy: ")
        try: 
            d = datetime.datetime.strptime(userIn, "%m/%d/%y")
            isValid=True
        except:
            print("Invalid Date, Please Re-type the due date.\n")
    
    #Return the date to set the "DD" variable        
    return d

def compile_data(data, c):
    
    c.execute('insert into ORDERS values (?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
    
def main(data):

    path = os.getcwd()
        
    conn = sqlite3.connect(path +'\\overOrders.db')  
    c = conn.cursor()  
    
    create_table(c)
    get_id(data, c)
    
    #Save SQLITE Data Changes and Close Connection
    conn.commit()
    conn.close()    
    



