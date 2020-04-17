import sqlite3
import sys
import os


def main(loc):
    global c
    
    path = os.getcwd()  
    
    conn = sqlite3.connect(path +'\\init_options.db')  
    c = conn.cursor()  

    c.execute('insert into ADD_ORDER_LOCS values (?)', loc)
    
    conn.commit()
    conn.close() 