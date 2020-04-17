import sqlite3
import os
import datetime
import sys
import pickle


def compile_data(data):
    
    c.execute('''UPDATE ORDERS
    SET PO_Number=?,
    PART_NUMBER=?,  
    PART_NAME=?,
    MATERIAL_TYPE=?, 
    MATERIAL_LOT=?, 
    DUE_DATE=?, 
    MACH_TIME=?, 
    DEBURR_TIME=?, 
    INSPECTION_TIME=?, 
    OSP_TIME=?, 
    PRICE=?,
    LOCATION=?
    WHERE Generated_ID=?
    ''', data)
    
def main(data):
    global c
    
    path = os.getcwd()
        
    conn = sqlite3.connect(path +'\\overOrders.db')  
    c = conn.cursor()  
         
    compile_data(data)
    #Save SQLITE Data Changes and Close Connection
    conn.commit()
    conn.close()    
    




