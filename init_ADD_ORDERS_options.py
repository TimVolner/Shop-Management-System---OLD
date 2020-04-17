import sqlite3
import sys
import os
import add_mat_lot

def create_table(c):
    try:
        # Create table - ADD_ORDER_OPTIONS
        c.execute('''CREATE TABLE ADD_ORDER_MTTYPES(
        [MAT_TYPES] text
        )''')   
        c.execute('''CREATE TABLE ADD_ORDER_MTLOTS(
        [MAT_LOTS] text
        )''')
        c.execute('''CREATE TABLE ADD_ORDER_LOCS(
        [LOCS] text
        )''')    
        
    except:
        pass

    a = add_mat_lot.main()
    
def main():
    
    path = os.getcwd()
    
    conn = sqlite3.connect(path +'\\init_options.db')  
    c = conn.cursor()  
    
    create_table(c)
    
    #Save SQLITE Data Changes and Close Connection
    conn.commit()
    conn.close()
    
    
    
    
main()

