#!/usr/bin/python
import sys, os
import subprocess as sp

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

# Manage Files #
if not os.path.exists('Files'):
    os.makedirs('Files')



# Advanced Search ####
#########_|_|_|_|#####################
""" Coded By Allistar by Star Sec."""
os.system("clear")
print (" ")
print ("  _|_|_|                  _|                  _|                         	          ")
print ("  _|    _|     _|_|_|   _|_|_|_|     _|_|_|   _|_|_|       _|_|_|     _|_|_|     _|_|      ")
print ("  _|    _|   _|    _|     _|       _|    _|   _|    _|   _|    _|   _|_|       _|_|_|_|     ")
print ("  _|    _|   _|    _|     _|       _|    _|   _|    _|   _|    _|       _|_|   _| 	   ")
print ("  _|_|_|       _|_|_|       _|_|     _|_|_|   _|_|_|       _|_|_|   _|_|_|       _|_|_| ")
print ("------------------------------------------------------------------------------------------ ")
print (" ")
print ("  ===|[ Database Tool ]|===")
print ("  [01] Search By Name       ")
print ("  [02] Search By Number          ")
print ("  [03] Add Information  ")
print ("  [04] Advanced Search")
print ("  [05] Update  ")
print ("  [00] Exit")
print
Data = input(" Choose:  ")

if (Data == '01' or Data == '1'):
       Target = input("Search For\n>")
       Search = sp.getoutput('find -depth -name "*%s*" ' % (Target))
       Search = str(Search)
       search = Search.replace("./", " ")
       print (search)
       os.system("cd( search )")
       os.system("ls")
       sys.exit()

elif (Data == '02' or Data == '2'):
       Target = input("Search For\n>")
       Search = sp.getoutput('find -depth -name "*%s*" ' % (Target))
       Search = str(Search)
       search = Search.replace("./", " ")
       os.system("cd" + search)
       os.system("ls")
       sys.exit()

elif (Data == '03' or Data == '3'):
       Info = input("Path Name\n>")
       os.system("mkdir %s" % (Info))
       os.system("cd Info")
       sys.exit()

elif (Data == '04' or Data == '4'):
       print (" ")
       os.system("clear")
       print ("  ===|[ Select Grade ]|===")
       print ("  [01] Group1 ")
       print ("  [02] Group2 ")
       print ("  [03] Group3 ")
       print ("  [04] Group4 ")
       print ("  [05] Group5 ")
       print ("  [00] Back   ")
       Grade = input(" Select\n>  ")
       Advanced()

elif (Data == '05' or Data == '5'):
       os.system("git clone github.com")
       print ("Updating ...")

elif (Data == '00' or Data == '0'):
       print ("\n[!] Exit the Program...")
       sys.exit()

else:
       print ("\n[!] ERROR : Wrong Input")
       os.system("sleep 1")
       restart_program()
