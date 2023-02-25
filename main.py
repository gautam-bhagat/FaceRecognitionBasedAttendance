import csv
import os
import cv2
import pickle

studentDatabase = "student.dat"

# add student
def addStudent():
    record =[]
    file = open(studentDatabase,'ab+')
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
        os.chdir(os.getcwd()+"\images")
        cv2.imwrite(str(roll)+".jpg",img)

        # Checking if any other data
        choice = input("Do You Want to Add More Students (y/n) : ")
        if choice == 'n' or choice=='N':
            break
    print(record)
    pickle.dump(record,file)
    file.close()


# display student
def readStudent():
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
            deleted = 1
            continue # skipping the record to be deleted
        rec.append(r)
    file = open(studentDatabase,'wb')
    pickle.dump(rec,file) # writing updated data
    file.close()
    if deleted == 1:
        print("Record Deleted")
    else :
        print("Record Not Found")

def main():
    # path for images of students
    path = "images"
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:

    # Create a new directory because it does not exist
        os.makedirs(path)

    isRunning = True
    while isRunning :
        print("\n1. Add Students\n2. List Students\n3. Update\n4. Delete\n5. Train the System\n6. Exit")
        choice = int(input("Enter Your Choice : "))
        if choice == 1 :
            addStudent()
        elif choice ==2 :
            readStudent()
        elif choice == 3 :
            updateStudent()
        elif choice == 4 :
            deleteStudent()
        elif choice == 5 :
            pass
        elif choice == 6 :
            isRunning = False


if __name__ == "__main__":
    main()