import sqlite3
import os
import sys
import pickle

def load_mattypes():
    global mat_types
    
    mat_types = c.execute('SELECT MAT_TYPES FROM ADD_ORDER_MTTYPES').fetchall()

def load_matlots():
    global mat_lots
    
    mat_lots = c.execute('SELECT MAT_LOTS FROM ADD_ORDER_MTLOTS').fetchall()

def load_locs():
    global locations
    
    locations = c.execute('SELECT LOCS FROM ADD_ORDER_LOCS').fetchall()

def compile_to_tmp():
    global data
    
    with open('temp.tmp', 'wb') as fp:
        pickle.dump(data, fp)     
    
def main():
    global mat_types, mat_lots, locations, data, c
    
    path = os.getcwd()
    
    conn = sqlite3.connect(path +'\\init_options.db')  
    c = conn.cursor()        
    
    load_mattypes()
    load_matlots()
    load_locs()
    
    data.append(mat_types)
    data.append(mat_lots)
    data.append(locations)

    compile_to_tmp()    
    
    conn.commit()
    conn.close()

mat_types = []
mat_lots = []
locations = []
data = []

main()
