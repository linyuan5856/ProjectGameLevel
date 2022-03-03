#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import sys
import xlrd
import csv
import string
import codecs # for write utf8.

#input path.
INPUTPATH= u"..\excel"

#output path for client and server.
CLIENT_OUTPATH = u"..\csv"
SERVER_OUTPATH = u"D:\\svn\\code\\Server\\bin\\config\\room"

EXT = ".xlsx"
CODE = "utf8"

#transfer class.
class Transfer:    
    def __init__(self):
        # all data.
        self.mData = []

        # server data.
        self.mServerData = []
                
        # client data.
        self.mClientData = []

    def getdata(self):
        return self.mData

    def getclientdata(self):
        return self.mClientData

    def getserverdata(self):
        return self.mServerData

    def read(self, filename):
        print("\n=== read: ", filename, " ===")
        xlsfile = xlrd.open_workbook(filename)
        table   = xlsfile.sheet_by_index(0)    
        rownum  = table.nrows     
        colsnum = table.ncols
        
        if rownum <= 1:
            return 

        # flags list.
        flags = []
        for j in range(0, colsnum):
            flag = table.cell_value(1, j)
            flags.append(int(flag))

        types = []
        for j in range(0, colsnum):
            types.append(table.cell_value(2, j))

        for i in range(0, rownum):
            if i == 1:
                continue

            row  = []         
            srow = []
            crow = []  
            for j in range(0, colsnum):
                # read (i,j) data.
                value = table.cell_value(i,j)
                # for string and int value.
                if isinstance(value, int):
                    value = int(value)
                else:
                    if isinstance(value, float): 
                        value = float(value)
                        diff  = value - int(value)
                        if 0 == diff:
                            value = int(value)

                #add to diff list.
                row.append(value)
                if flags[j] == 3 or flags[j] == 1:
                    crow.append(value)
                if flags[j] == 3 or flags[j] == 2:
                    srow.append(value)         
            self.mData.append(tuple(row))
            self.mServerData.append(tuple(srow))
            self.mClientData.append(tuple(crow))  
                                  
    def write(self, path, filename, content):     
        if not os.path.exists(path):         
            os.makedirs(path)
        csvfile = open("tmp", "w", newline="", encoding="utf_8_sig")
        writer = csv.writer(csvfile)       
        writer.writerows(content)      
        csvfile.close()

        if os.path.exists(os.path.join(path,filename+".old")):     
            os.remove(os.path.join(path,filename+".old"))   
        #if os.path.exists(os.path.join(path,filename)):        
        #    os.rename(os.path.join(path,filename),os.path.join(path,filename+".old")) 
        if os.path.exists(os.path.join(path,filename)):     
            os.remove(os.path.join(path,filename))           
        os.rename("tmp", os.path.join(path, filename))     
  
        print("=== write", path, filename, " ok ===")
#end of declaring Transfer class.

def handleExcel():    
    files, dirs, root = readFilename(INPUTPATH)
    for f in files:        
        strstock = os.path.join(INPUTPATH, f)        
        if os.path.exists(strstock):
            st = Transfer()
            st.read(strstock)            
            name = f.replace(EXT, "")
            #st.write(SERVER_OUTPATH, name+".csv", st.getserverdata())
            st.write(CLIENT_OUTPATH, name+".csv", st.getclientdata())   
        else:
            print(strstock+" don't exist")

def readFilename(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files, dirs, root

if __name__ == '__main__':
    print("=== begin to transfer excel(",INPUTPATH,") to csv (",SERVER_OUTPATH,")===")
    handleExcel()
    print("\n=== end to transfer excel to csv! ===")
