from datetime import datetime
import numpy as np
import cv2 
import re

img = 'C:/Users/User/Desktop/0602.jpg'
image = cv2.imread(img)
image2 = cv2.resize(image, dsize=(900,1200))
drawing = False
ix , iy , i , j = 0, 0, 0, 0
today = datetime.today().strftime("%Y%m%d")

a = re.split(r"[/,.]",img)
save_name = ((a[len(a)-2]))

def draw(event,x,y,flags,params):
    global ix,iy,i,j,save_name

    if event == cv2.EVENT_LBUTTONDOWN:
        ix = x
        iy = y
        cv2.rectangle(image2, (ix-32,iy-32), (x+32,y+32), (0,0,255), 5)
        crop_img = image[(10*iy)-640:(10*y)+640, (10*ix)-640:(10*x)+640]
        cv2.imwrite('test/0610roi/'+today+'_'+str(i+1)+'.jpg', crop_img)
        cv2.putText(image2, str(i+1), (x,y), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 5)
        i += 1

    if event == cv2.EVENT_RBUTTONDOWN:
        ix = x
        iy = y
        cv2.rectangle(image2, (ix-32,iy-32), (x+32,y+32), (255,0,0), 5)
        crop_img = image[(10*iy)-640:(10*y)+640, (10*ix)-640:(10*x)+640]
        cv2.imwrite('test/0610roi/'+today+'_new_'+str(j+1)+'.jpg', crop_img)
        cv2.putText(image2, str(j+1), (x,y), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 5)
        j += 1

cv2.namedWindow("Window")
cv2.setMouseCallback("Window",draw)

while(True):
    cv2.imshow("Window",image2)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()