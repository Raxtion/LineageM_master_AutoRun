from PIL import Image
from PIL import ImageGrab
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

def clickSELF():
    g.click(1060, 438)

def clickBuff():
    g.click(790, 670)


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

    filter_times = 3
    Blood_filter_L = []
    Magic_filter_L = []
    Blood_filter_R = []
    Magic_filter_R = []

    T_L = timer.Timer()
    T2_L = timer.Timer()
    T_R = timer.Timer()
    T2_R = timer.Timer()
    T_Buff = timer.Timer()

    trains_list = np.load(os.getcwd() + '\\picture\\trains_list.npy')
    labels_list = np.load(os.getcwd() + '\\picture\\labels_list.npy')
    knn_blood = cv2.ml.KNearest_create()
    knn_blood.train(trains_list, cv2.ml.ROW_SAMPLE, labels_list)
    trains_list = np.load(os.getcwd() + '\\picture\\trains_list_magic.npy')
    labels_list = np.load(os.getcwd() + '\\picture\\labels_list_magic.npy')
    knn_magic = cv2.ml.KNearest_create()
    knn_magic.train(trains_list, cv2.ml.ROW_SAMPLE, labels_list)


    while True:
        #Get Full Screenshot
        g.press('printscreen')
        full_screenshot_img = ImageGrab.grabclipboard()
        #full_screenshot_img.show()
        #quit()

        if full_screenshot_img == None:
            continue

        #Get Left Blood Bar img (L)
        area = (120,45,223,66)
        cut_screenimg = full_screenshot_img.crop(area)
        #cut_screenimg.show()   #Check Cut Screen
        #cut_screenimg.save('testblood_2.bmp')
        #quit()
        
        #Get Left Blood Value (L)
        Result_blood_L = CVKNNgetLetter(knn_blood, cut_screenimg, (10, 15), nThreshold = 300000)


        #Get Left Magic Bar img (L)
        area = (120,66,223,86)
        cut_screenimg = full_screenshot_img.crop(area)
        #cut_screenimg.show()   #Check Cut Screen
        #cut_screenimg.save('testmagic_2.bmp')
        #quit()

        #Get Left Magic Value (L)
        Result_magic_L = CVKNNgetLetter(knn_magic, cut_screenimg, (8, 15), nThreshold = 150000)


        #Get Right Blood Bar img (R)
        area = (2040,45,2143,66)
        cut_screenimg = full_screenshot_img.crop(area)
        #cut_screenimg.show()   #Check Cut Screen
        #cut_screenimg.save('testblood_2.bmp')
        #quit()
        
        #Get Right Blood Value (R)
        Result_blood_R = CVKNNgetLetter(knn_blood, cut_screenimg, (10, 15), nThreshold = 300000)

        #Get Right Magic Bar img (R)
        area = (2040,66,2143,86)
        cut_screenimg = full_screenshot_img.crop(area)
        #cut_screenimg.show()   #Check Cut Screen
        #cut_screenimg.save('testmagic_2.bmp')
        #quit()

        #Get Right Magic Value (R)
        Result_magic_R = CVKNNgetLetter(knn_magic, cut_screenimg, (8, 15), nThreshold = 150000)

        
        if len(Result_blood_L) < 2 or len(Result_magic_L) < 2 or len(Result_blood_R) < 2 or len(Result_magic_R) < 2:
            #print('Blood ', Result_blood)
            #print('Magic ', Result_magic)
            continue
        
        try:
            BloodValue_L = int(Result_blood_L[:-2])
            MagicValue_L = int(Result_magic_L[:-2])
            BloodValue_R = int(Result_blood_R[:-2])
            MagicValue_R = int(Result_magic_R[:-2])

            Blood_filter_L.append(BloodValue_L)
            if len(Blood_filter_L) > filter_times:
                Blood_filter_L = Blood_filter_L[1:]

            Magic_filter_L.append(MagicValue_L)
            if len(Magic_filter_L) > filter_times:
                Magic_filter_L = Magic_filter_L[1:]

            Blood_filter_R.append(BloodValue_R)
            if len(Blood_filter_R) > filter_times:
                Blood_filter_R = Blood_filter_R[1:]

            Magic_filter_R.append(MagicValue_R)
            if len(Magic_filter_R) > filter_times:
                Magic_filter_R = Magic_filter_R[1:]

            if len(Blood_filter_L) < filter_times or len(Magic_filter_L) < filter_times or len(Blood_filter_R) < filter_times or len(Magic_filter_R) < filter_times:
                continue

            listTemp = Blood_filter_L.copy()
            listTemp.sort()
            BloodValue_L = listTemp[int(filter_times/2)]
            listTemp = Magic_filter_L.copy()
            listTemp.sort()
            MagicValue_L = listTemp[int(filter_times/2)]
            listTemp = Blood_filter_R.copy()
            listTemp.sort()
            BloodValue_R = listTemp[int(filter_times/2)]
            listTemp = Magic_filter_R.copy()
            listTemp.sort()
            MagicValue_R = listTemp[int(filter_times/2)]

            print('Blood_L ' + '{:>5}'.format(BloodValue_L) 
                  + ' : Magic_L ' + '{:>5}'.format(MagicValue_L)
                  + '    Blood_R ' + '{:>5}'.format(BloodValue_R) 
                  + ' : Magic_R ' + '{:>5}'.format(MagicValue_R), end='\r')
        except:
            continue

        #Control for Left 
        if T_L.timeup() and BloodValue_L < 600:
            clickSELF()
            click高級治癒()
            time.sleep(1)
            click高級治癒()
            T_L.timestart(3000)
            bIsUseMagicLock = True
            clickSELF()
        elif T_L.timeup() and BloodValue_L > 600 and bIsUseMagicLock == True:
            bIsUseMagicLock = False

        if bIsUseMagic == True and MagicValue_L < 500:
            bIsUseMagic = False
        elif bIsUseMagic == False and MagicValue_L > 900:
            #bIsUseMagic = True
            bIsUseMagic = False
        else:
            pass

        if bIsUseMagic == True and bIsUseMagicLock == False:
            if T2_L.timeup():
                click地裂()
                T2_L.timestart(3000)


        #Control for Right 
        if T_R.timeup() and BloodValue_R < 600:
            click高級治癒()
            time.sleep(1)
            click高級治癒()
            T_R.timestart(3000)
            bIsUseMagicLock = True
        elif T_R.timeup() and BloodValue_R > 600 and bIsUseMagicLock == True:
            bIsUseMagicLock = False

        #Add Buff
        if (T_Buff.timeup()):
            clickBuff()
            T_Buff.timestart(360000)

        time.sleep(1)

