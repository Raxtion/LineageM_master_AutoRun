import pyautogui as g
import time


i = 0
while True:
    #click高級治癒()
    
    im = g.screenshot()
    area = (127,45,223,66)      #血條
    cut_img = im.crop(area)
    cut_img.save(r'C:\Users\raxku\OneDrive\Documents\FunctionLib\python\pyCode\MachineLearning_leaning\LetterRecognition\picture\group1\data_' + str(i) + '.bmp')

    im = g.screenshot()
    area = (127,66,223,86)      #魔條
    cut_img = im.crop(area)
    cut_img.save(r'C:\Users\raxku\OneDrive\Documents\FunctionLib\python\pyCode\MachineLearning_leaning\LetterRecognition\picture\group2\data_' + str(i) + '.bmp')

    i = i + 1
    time.sleep(15)
