import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    file_name = path+"/"+file
    print(file_name)
    images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height,width,channel = frame.shape
size = (width,height)
print(size)
output = cv2.VideoWriter("sunrise.mp4",cv2.VideoWriter_fourcc(*"DIVX"),10,size)
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    output.write(frame)