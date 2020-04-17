import sqlite3
import sys
import os


def main(mt_types):
    global c
    
    path = os.getcwd()  
    
    conn = sqlite3.connect(path +'\\init_options.db')  
    c = conn.cursor()  

    c.execute('insert into ADD_ORDER_MTTYPES values (?)', mt_types)
    
    conn.commit()
    conn.close() 