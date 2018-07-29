import pyautogui as g
import time
import datetime as dt
import os

n = dt.datetime.now()
n.strftime('%Y%m%d%H%M%S')

i = 0
while True:
    #click高級治癒()
    
    im = g.screenshot()
    area = (127,45,223,66)      #血條
    cut_img = im.crop(area)
    cut_img.save(r'C:\Users\raxku\OneDrive\Documents\FunctionLib\python\pyCode\MachineLearning_leaning\LetterRecognition\picture\\' + str(i) + '.bmp')

    img = cut_img.copy()

    bIsBreak = False
    for i in range(0, 96):
        if bIsBreak == True: break
        for j in range(0, 21):
            if bIsBreak == True: break
            R_value = img.getpixel((i,j))[0]
            B_value = img.getpixel((i,j))[1]
            G_value = img.getpixel((i,j))[2]
            if R_value == 0 and B_value == 0 and G_value == 0:
                break
            if R_value > 235 and B_value > 235 and G_value > 235:
                print((i, j))
                print(R_value)
                print(B_value)
                print(G_value)
                os.chdir(r'C:\Users\raxku\OneDrive\Documents\FunctionLib\python\pyCode\MachineLearning_leaning\LetterRecognition\picture')
                #動態切圖會有問題啊 當血量低時 又有光經過血條 會誤判血量 (白色大量擋住切圖功能)
                '''
                area = (i-8,j-3,i-8+10,j-3+15)
                cut_img = img.crop(area)
                cut_img.save('Result_'+n.strftime('%Y%m%d%H%M%S')+'_Code1.bmp')
                area = (i-8+10,j-3,i-8+20,j-3+15)
                cut_img = img.crop(area)
                cut_img.save('Result_'+n.strftime('%Y%m%d%H%M%S')+'_Code2.bmp')
                area = (i-8+20,j-3,i-8+30,j-3+15)
                cut_img = img.crop(area)
                cut_img.save('Result_'+n.strftime('%Y%m%d%H%M%S')+'_Code3.bmp')
                '''
                
                area = (11,5,21,20)
                cut_img = img.crop(area)
                cut_img.save('Result_'+n.strftime('%Y%m%d%H%M%S')+'_Code1.bmp')
                area = (21,5,31,20)
                cut_img = img.crop(area)
                cut_img.save('Result_'+n.strftime('%Y%m%d%H%M%S')+'_Code2.bmp')
                area = (31,5,41,20)
                cut_img = img.crop(area)
                cut_img.save('Result_'+n.strftime('%Y%m%d%H%M%S')+'_Code3.bmp')
                
                bIsBreak = True

    
    i = i + 1
    quit()
    time.sleep(15)
