import cv2
import os
from csv import writer
import face_recognition
import pickle
import numpy as np
from datetime import datetime

presentId =[]

def markAttendance(id,name,mail):
    print(id)
    if id not in presentId:
        presentId.append(id)
        print("Attendance Marked")
        rec = [str(datetime.now()),id,name.get(id),mail.get(id)]
        with open("Attendance.csv",'a') as f:
             writer_obj = writer(f)
             writer_obj.writerow(rec)
             f.close()

def takeAttendance():
    cap =  cv2.VideoCapture(0)

    encodedFile = open("EncodedFile.p",'rb+')
    encodedFilewithId = pickle.load(encodedFile)
    encodedFile.close()

    encodings , ids = encodedFilewithId


    os.chdir(os.getcwd())
    file = open("student.dat",'rb')
    name = {}
    mail = {}

    while True:
            try:
                records = pickle.load(file)
                for r in records:
                    name[r[0]] = r[1]
                    mail[r[0]] = r[2]
            except EOFError:
                break
            except:
                print("Error")
    file.close()

    while True:
        
            success , liveImage = cap.read()
    

            liveImageS = cv2.resize(liveImage,(0,0), None,  0.25,0.25)
            liveImageS = cv2.cvtColor(liveImage,cv2.COLOR_BGR2RGB)

            faceCurLive = face_recognition.face_locations(liveImageS)
            encodeCurLive = face_recognition.face_encodings(liveImageS,faceCurLive)

            for encodeFace,faceLoc in zip(encodeCurLive,faceCurLive):
                matches = face_recognition.compare_faces(encodings,encodeFace)
                distance = face_recognition.face_distance(encodings,encodeFace)
            #     print(matches)
            #     print(distance)
                matchIndex = np.argmin(distance)
                if matches[matchIndex]:
                    id = ids[matchIndex]
                    y1, x2, y2, x1 = faceLoc
                    print("Name : ",name.get(int(id)))
                    print("Mail : ",mail.get(int(id)),end="\n")
                    markAttendance(int(id),name,mail)
                    cv2.rectangle(liveImage, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(liveImage, (x1, y2 ), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(liveImage, id, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    cv2.putText(liveImage, name.get(int(id)), ( 20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                
            cv2.imshow("Attendance", liveImage)
            if not success:
                break
            
            k = cv2.waitKey(1)

            if cv2.getWindowProperty("Attendance", cv2.WND_PROP_VISIBLE) <1:
                break

            if k%256 == 27:
                 break
            elif k%256 == 32:
                pass
        
# if __name__ == "__main__":
#     takeAttendance()