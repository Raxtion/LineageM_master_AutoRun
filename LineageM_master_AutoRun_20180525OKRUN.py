from PIL import Image
import numpy as np
import cv2
import os
import timer
import math
import pyautogui as g
import time

def click高級治癒():
    g.click(536, 662)

def click指定傳送():
    g.click(1200, 670)

def click紅水():
    g.click(970, 678)

def click地裂():
    g.click(704, 664)


def CVKNNgetLetter(knn, img, ntpLetterDetectedSize = (0, 0), nThreshold = 200000):
    dicLabeledDataResult = {}
    for group in range(0, int(img.size[0] / ntpLetterDetectedSize[0])):
        for row in range(0, img.size[1]):
            for col in range(0 + group, img.size[0], ntpLetterDetectedSize[0]):
                #area select
                area = (col, row, col + ntpLetterDetectedSize[0], row + ntpLetterDetectedSize[1])
                if area[2] > img.size[0] or area[3] > img.size[1]:
                    break

                cut_img = img.crop(area)
                cvImg = np.array(cut_img)    
                testgray = cv2.cvtColor(cvImg,cv2.COLOR_BGR2GRAY)
                data = testgray.reshape(1, ntpLetterDetectedSize[0]*ntpLetterDetectedSize[1]).astype('float32')

                #Knn Test
                ret, result, neighbours, dist = knn.findNearest(data, k=3)

                #Result collection
                if len([x for x in dist[0] if x < nThreshold]) > 2 and len(set(neighbours[0])) == 1:
                    dicLabeledDataResult[area] = (result[0], data)
                
    E_ = [x for x in dicLabeledDataResult.keys()]
    E_.sort()
    intervalMarkerIndes = [E_.index(x) for x in E_ if dicLabeledDataResult[x][0] == 10.0]
    if len(intervalMarkerIndes) < 1:
        return ""
    EE_ = []
    for x in E_[:intervalMarkerIndes[0]+1]:
        if len(EE_) == 0:
            EE_.append(x)
            continue

        if abs(x[0] - EE_[-1][0]) > (ntpLetterDetectedSize[0]-2):
            EE_.append(x)

    S_ = ''.join([str(int(dicLabeledDataResult[x][0][0])) for x in EE_])
    return S_


if __name__ == '__main__':
    bIsUseMagic = False
    bIsUseMagicLock = False

    T = timer.Timer()
    T2 = timer.Timer()

    trains_list = np.load(os.getcwd() + '\\picture\\trains_list.npy')
    labels_list = np.load(os.getcwd() + '\\picture\\labels_list.npy')
    knn_blood = cv2.ml.KNearest_create()
    knn_blood.train(trains_list, cv2.ml.ROW_SAMPLE, labels_list)
    trains_list = np.load(os.getcwd() + '\\picture\\trains_list_magic.npy')
    labels_list = np.load(os.getcwd() + '\\picture\\labels_list_magic.npy')
    knn_magic = cv2.ml.KNearest_create()
    knn_magic.train(trains_list, cv2.ml.ROW_SAMPLE, labels_list)


    while True:
        #Get Blood Bar img
        screenimg = g.screenshot()
        area = (127,45,223,66)
        cut_screenimg = screenimg.crop(area)        
        #cut_screenimg.show()   #Check Cut Screen
        #quit()
        
        #Get Blood Value
        Result_blood = CVKNNgetLetter(knn_blood, cut_screenimg, (10, 15), nThreshold = 250000)

        #Get Magic Bar img
        screenimg = g.screenshot()
        area = (127,66,223,86)
        cut_screenimg = screenimg.crop(area)

        #Get Magic Value
        Result_magic = CVKNNgetLetter(knn_magic, cut_screenimg, (8, 15), nThreshold = 150000)

        
        if len(Result_blood) < 2 or len(Result_magic) < 2:
            #print('Blood ', Result_blood)
            #print('Magic ', Result_magic)
            continue
        
        print('Blood ' + '{:>5}'.format(Result_blood[:-2]) + ' : Magic ' + '{:>5}'.format(Result_magic[:-2]), end='\r')

        try:
            BloodValue = int(Result_blood[:-2])
            MagicValue = int(Result_magic[:-2])
        except:
            continue

        if T.timeup() and BloodValue < 600:
            click高級治癒()
            time.sleep(1)
            click高級治癒()
            T.timestart(3000)
            bIsUseMagicLock = True
        elif T.timeup() and BloodValue > 600 and bIsUseMagicLock == True:
            bIsUseMagicLock = False

        if bIsUseMagic == True and MagicValue < 500:
            bIsUseMagic = False
        elif bIsUseMagic == False and MagicValue > 900:
            bIsUseMagic = True
        else:
            pass

        if bIsUseMagic == True and bIsUseMagicLock == False:
            if T2.timeup():
                click地裂()
                T2.timestart(3000)


        time.sleep(1)

