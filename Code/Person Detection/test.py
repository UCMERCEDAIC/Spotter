import cv2

img=cv2.imread(r"Images\Corrcet_0041.jpg")

print(img.shape)

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

classIds,confs,bbox=net.detect(img,confThreshold=.70)
print(classIds)
print(bbox)
counter=0

for x in classIds:
    
    for y in x:
        print(y)
        if y==1:
            print('found person')
            print(x)
            print(counter)
            temparray=bbox[counter]
            
            
            print(temparray)
            x1=temparray[0]
            y1=temparray[1]
            x2=temparray[2]
            y2=temparray[3]

            crop_img = img[y1:y2+200, x1:x2+200]
            cv2.imshow("cropped", crop_img)
            cv2.waitKey(2000)

    
    counter=counter+1
    num = 0