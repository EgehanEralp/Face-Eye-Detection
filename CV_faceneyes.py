#%%

import cv2
import numpy as np 

face_cascade = cv2.CascadeClassifier(      
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )


eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_eye.xml'
        )

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()#img == GERÇEK KAMERA GÖRÜNTÜSÜ
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #grey == GRİ KAMERA GÖRÜNTÜSÜ
    
    faces = face_cascade.detectMultiScale(gray,1.1,6)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(
                img,(x,y),(x+w,y+h), (255,0,0), 2
                )
        roi_gray=gray[y:y+h, x:x+h]
        roi_color=img[y:y+h, x:x+h]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(
                    roi_color,(ex,ey),(ex+ew,ey+eh), (0,255,0),3
                    )
    cv2.imshow('img',img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()