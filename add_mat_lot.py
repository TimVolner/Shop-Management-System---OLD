import sqlite3
import sys
import os

def set_material_lots():

    mat_lots = []

    try:
        with open('mat_lots_location.txt', 'r') as fp:
            mat_lots_path = fp.read() 
    except:
        pass


    try:
        for file in [f for f in os.listdir(mat_lots_path) if f.endswith('.jpg') or f.endswith('.JPG')]:
            base = os.path.basename(file)
            mat_lots.append(os.path.splitext(base)[0])
    except:
        mat_lots = ['UNCERTIFIED']
        
    return mat_lots

def main():
    
    mt_lots = set_material_lots() 
    
    path = os.getcwd()
    
    conn = sqlite3.connect(path +'\\init_options.db')  
    c = conn.cursor()  
    
    c.execute('''DELETE FROM ADD_ORDER_MTLOTS''')    
    
    for item in mt_lots:
        item = [item]
        c.execute('insert into ADD_ORDER_MTLOTS values (?)', item)
    
    conn.commit()
    conn.close()    

