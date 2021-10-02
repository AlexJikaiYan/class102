import cv2
import time
import random
starttime=time.time()
def Takesnapshot():
    number=random.randint(1,9)
    Videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=Videocaptureobject.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        starttime=time.time
        result=False
    return  imagename
    print("snapshot taken")
    Videocaptureobject.release()
    cv2.destroyAllWindows()
Takesnapshot()
