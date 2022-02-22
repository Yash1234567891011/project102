from os import access
from tkinter import Frame
import cv2
import dropbox
import random
import time
start_time=time.time()
def take_photo():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
        return img_name
    print("Photo taken") 
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_photo(file):
    access_token="sl.BAIbjDQKDt4uVBEUKTqa_BDC2KTdNnSualqKRK3SXKwtTdmUeGP-yf_wlCoHlqjGFhmii8F93FEFTqDrSHrGUwDsj61dyMsbqdMnZp4LKwLXxnS5qsfLfz5Ymw18t1MyReKOsbCI7bk"
    img=file
    file_from=img
    file_to="/securityphotos/"+(file)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_photo()
            upload_photo(name)
main()                    