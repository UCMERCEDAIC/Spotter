import cv2
import numpy as np

img =cv2.imread(r"0001.jpg",1)
print (img.shape)
cv2.imshow("Legend",img)
cv2.waitKey(2000)
cv2.destroyAllWindows
img=cv2.resize(img,int(img))
classNames=[]
classFile=r"Code\Person Detection\coco.names"