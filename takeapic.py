import cv2 
import time

#key = cv2. waitKey(100)
#webcam = cv2.VideoCapture(0)
#time.sleep(10)
#check, frame = webcam.read()
#cv2.imshow("Capturing", frame)
#key = cv2.waitKey(100)
#cv2.imwrite(filename='D:\\Python_progs\\Finalproject\\custom\\myface.jpg', img=frame)
#webcam.release()
import cv2
camera_port = 0 
ramp_frames = 30 
camera = cv2.VideoCapture(camera_port)
def get_image():
 retval, im = camera.read()
 return im 
for i in range(ramp_frames):
 temp = camera.read()

camera_capture = get_image()
filename = "D:\\Python_progs\\Finalproject\\custom\\myface.jpg"
cv2.imwrite(filename,camera_capture)
del(camera)
