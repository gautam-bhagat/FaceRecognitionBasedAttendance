import csv
import os
import cv2
import pickle

studentDatabase = "student.dat"
# add student
def addStudent():
    record =[]
    file = open(studentDatabase,'ab+')
    mainD = os.getcwd()
    while True:
        # Getting Details
        
        roll = int(input("\nEnter Student Roll : "))
        name = input("Enter Student Name : ")
        mail = input("Enter Student Mail : ")
        data = [roll,name,mail]
        record.append(data)

        # Image Location
        imgPath = input("Enter Image Path : ") 
        imgPath = imgPath.replace('\\','\\\\')

        # Writing Image in specified Location
        img = cv2.imread(imgPath)
        # os.chdir(os.getcwd()+"\images")
        cv2.imwrite(os.path.join(mainD,"images",str(roll)+".jpg"),img)
        # os.chdir(mainD)
        # Checking if any other data
        choice = input("Do You Want to Add More Students (y/n) : ")
        if choice == 'n' or choice=='N':
            break
    pickle.dump(record,file)
    file.close()

# display student
def readStudent():
    os.chdir(os.getcwd())
    file = open(studentDatabase,'rb')
    while True:
        try:
            records = pickle.load(file)
            for r in records:
                print(r)
        except EOFError:
            break
        except:
            print("Error")
    
    file.close()

# update student detials
def updateStudent():
    file = open(studentDatabase,'rb+')
    records = pickle.load(file)
    roll = int(input("Enter Roll Number to be updated : "))
    found = 0
    for r in records:
        # Checking if roll no exists
        if roll == r[0]:
            print("Current Record : ",r)
            found = 1
            name = input("Enter Student Name : ")
            mail = input("Enter Student Mail : ")
            r[1] = name # updating name
            r[2] = mail # updating mail
            print("Updated Record : ",r)
            break

    if found==0:
        print("Record Not Found")
    else:
        file.seek(0) # moving pointer to start of file
        pickle.dump(records,file)

    file.close()

# delte student
def deleteStudent():
    file = open(studentDatabase,'rb')
    # loading all data
    records = pickle.load(file)
    file.close()
    roll = int(input("Enter Roll Number to be deleted : "))
    rec = [] # list to store updated data
    deleted = 0
    for r in records:
        if r[0] == roll:
            mainD = os.getcwd()
            path = os.path.join(mainD,"images",str(roll)+".jpg")
            if os.path.exists(path):
                    os.remove(path)
            print("Record Deleted")
            
            continue # skipping the record to be deleted
        rec.append(r)
    file = open(studentDatabase,'wb')
    pickle.dump(rec,file) # writing updated data
    file.close()

    # if deleted == 1:
    #     mainD = os.getcwd()
    #     path = os.path.join(mainD,"images",str(roll)+".jpg")
    #     if os.path.exists(path):
    #             os.remove(path)
    #     print("Record Deleted")
    # else :
    #     print("Record Not Found")

