import os
from os import path
from pathlib import Path



def main():
    #f = open("textfile.py","r")
    #completeContent = f.read()
    #print(completeContent)
    #if f.mode == 'r':

    #    arrayLine = f.readlines()
    #    for x in arrayLine:
    #        print(x)

    #f.close()

    print("The OS name is :" +os.name)
    if path.exists("textfile.py"):
        print("File exists :"+ str(path.realpath("textfile.py")))
        print("Dir exists: "+ str(path.getmtime("textfile.py"))) 

    file = open("textfile.py","r")

    with open ("textfile.py","r") as reader:
       # print(str(reader.readlines()))
        reader.close()
    
    data= file.readlines()
    for x in data:

        print(data)

    file.close()

if __name__ =="__main__":
    main()