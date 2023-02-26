import os

from attend import takeAttendance
from crud import *
from encode_images import trainSystem


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
        print("\n1. Add Students\n2. List Students\n3. Update\n4. Delete\n5. Train the System\n6. Take Attendance\n7. Exit")
        choice = int(input("Enter Your Choice : "))
        if choice == 1 :
            addStudent()
        elif choice ==2 :
            readStudent()
            # pass
        elif choice == 3 :
            updateStudent()
        elif choice == 4 :
            deleteStudent()
        elif choice == 5 :
            trainSystem()
        elif choice == 6 :
            takeAttendance()
        elif choice == 7 :
            isRunning = False


if __name__ == "__main__":
    main()