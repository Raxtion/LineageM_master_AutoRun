from PIL import Image
import numpy as np
import cv2
import os
import timer
import math


T = timer.Timer()

trains_list = np.load(os.getcwd() + '\\picture\\trains_list.npy')
labels_list = np.load(os.getcwd() + '\\picture\\labels_list.npy')

knn = cv2.ml.KNearest_create()
knn.train(trains_list, cv2.ml.ROW_SAMPLE, labels_list)


ntpLetterDetectedSize = (10, 15)            #in (Columns, Rows)
InpFileName = os.getcwd() + '\\picture\\data_19.bmp'

img = Image.open(InpFileName)


dicLabeledDataResult = {}
for group in range(0, int(img.size[0] / ntpLetterDetectedSize[0])):
    for row in range(0, img.size[1]):
        for col in range(0 + group, img.size[0], ntpLetterDetectedSize[0]):
            #area select
            area = (col, row, col + ntpLetterDetectedSize[0], row + ntpLetterDetectedSize[1])
            #print(area)
            if area[2] > img.size[0] or area[3] > img.size[1]:
                break

            cut_img = img.crop(area)
            cvImg = np.array(cut_img)    #the same with cv2.imread('filename')
            testgray = cv2.cvtColor(cvImg,cv2.COLOR_BGR2GRAY)
            data = testgray.reshape(1, ntpLetterDetectedSize[0]*ntpLetterDetectedSize[1]).astype('float32')

            #Knn Test
            ret, result, neighbours, dist = knn.findNearest(data, k=3)

            #print(ret)
            #print(result)
            #print(neighbours)
            #print(dist)

            if len([x for x in dist[0] if x < 200000]) > 2 and len(set(neighbours[0])) == 1:
                dicLabeledDataResult[area] = (result[0], data)
                
#print(dicLabeledDataResult)
print(len(dicLabeledDataResult))

E_ = [x for x in dicLabeledDataResult.keys()]
E_.sort()
EE_ = []
for x in E_:
    if len(EE_) == 0:
        EE_.append(x)
        continue

    if abs(x[0] - EE_[-1][0]) > 2:
        EE_.append(x)
E_ = EE_


print(len(E_))
for key in E_:
    print(key)
    print(dicLabeledDataResult[key][0])

    img2Log = dicLabeledDataResult[key][1]
    img2Log = img2Log.reshape([15, 10])
    im = Image.fromarray(np.uint8(img2Log))
    #im.show()

'''
11
6
(11, 4, 21, 19)
[5.]
(21, 4, 31, 19)
[8.]
(30, 4, 40, 19)
[4.]
(56, 4, 66, 19)
[8.]
(66, 4, 76, 19)
[9.]
(74, 2, 84, 17)
[4.]
'''