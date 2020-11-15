import cv2

img=cv2.imread(r"Images\Corrcet_0010.jpg")
cv2.imshow("Output",img)
cv2.waitKey(2000)
classNames=[]
classFile=r"Code\Person Detection\coco.names"
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
print(classNames)
weightpath=r"Code\Person Detection\frozen_inference_graph.pb"
configpath=r"Code\Person Detection\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"

net=cv2.dnn_DetectionModel(weightpath,configpath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

classIds,confs,bbox=net.detect(img,confThreshold=.7)
print(classIds)
print(bbox)