import cv2
import pyttsx3
import numpy as np

# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier('C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

# Load functions

def speak(audio):
    
    #Function for speak output
    
    engine.say(audio)
    engine.runAndWait()
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",140)
engine.setProperty("volume",1000)



def face_extractor(img):
    
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h,x:x+w]
    return cropped_face

# Initialize Webcam
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
count = 0
speak("please look into the camera..")

# Collect 10 samples of your face from webcam input
while True:
    ret,frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame),(200,200))
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

        file_name_path = 'C:\\Users\\hp\\FACE\\'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,face)

        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow("face cropper",face)
    else:
        print('face not found')
        speak("face not found..")
        pass
    if cv2.waitKey(1)==13 or count==10:  #13 is the Enter Key
        break
cap.release()
cv2.destroyAllWindows()
print("collecting samples complete")