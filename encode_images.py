import cv2
import face_recognition
import pickle
import os

def trainSystem():
    
    imagesFolder ="images"
    images = os.listdir(imagesFolder)

    imgList = []
    studentIds = []
    for i in images : 
        studentIds.append(os.path.splitext(i)[0])
        imgList.append(cv2.imread(os.path.join(imagesFolder,i)))


    def findEncodings(imgList):
        encodeList = []
        for img in imgList:
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    print("Training Faces to System")
    encodeListKnown = findEncodings(imgList)
    encodeListKnown = [encodeListKnown,studentIds]

    file = open("EncodedFile.p",'wb')
    pickle.dump(encodeListKnown,file)
    file.close()
    print("Training Complete")