import os
from PIL import Image

#img = Image.open('data_0.bmp')

#print(img.size)
#print(img.getpixel((0,0)))
#print(img.getpixel((95,0)))
#print(img.getpixel((0,20)))
#print(img.getpixel((95,20)))

'''
for i in range(0, 96):
    for j in range(0, 21):
        R_value = img.getpixel((i,j))[0]
        B_value = img.getpixel((i,j))[1]
        G_value = img.getpixel((i,j))[2]
        if R_value == 0 and B_value == 0 and G_value == 0:
            break
        if R_value > 200 and B_value > 200 and G_value > 200:
            print((i, j))
'''


#get (12, 6) -> Crop(11,5) 左上
#第一碼: area = (11,5,21,20)
#第二碼: area = (21,5,31,20)
#第三碼: area = (31,5,41,20)


for x in range(0, 101):
    #os.chdir(r'C:\Users\raxku\OneDrive\Documents\FunctionLib\python\pyCode\MachineLearning_leaning\LetterRecognition\picture\RowData\3Code')
    os.chdir(r'C:\Users\raxku\OneDrive\Documents\FunctionLib\python\pyCode\MachineLearning_leaning\LetterRecognition\picture\RowData\3Code_magic')
    try:
        img = Image.open('data_'+str(x)+'.bmp')
    except:
        continue

    for i in range(0, 96):
        #for j in range(0, 21):
        for j in range(0, 20):
            R_value = img.getpixel((i,j))[0]
            B_value = img.getpixel((i,j))[1]
            G_value = img.getpixel((i,j))[2]
            if R_value == 0 and B_value == 0 and G_value == 0:
                break
            if R_value > 200 and B_value > 200 and G_value > 200:
                #print((i, j))
                os.chdir(r'C:\Users\raxku\OneDrive\Documents\FunctionLib\python\pyCode\MachineLearning_leaning\LetterRecognition\picture\SplitData')
                ''' Blood pixel
                area = (11,5,21,20)
                cut_img = img.crop(area)
                cut_img.save('Result_'+str(x)+'_Code1.bmp')
                area = (21,5,31,20)
                cut_img = img.crop(area)
                cut_img.save('Result_'+str(x)+'_Code2.bmp')
                area = (31,5,41,20)
                cut_img = img.crop(area)
                cut_img.save('Result_'+str(x)+'_Code3.bmp')
                '''

                area = (14,3,22,18)
                cut_img = img.crop(area)
                cut_img.save('Result_'+str(x)+'_Code1.bmp')
                area = (22,3,30,18)
                cut_img = img.crop(area)
                cut_img.save('Result_'+str(x)+'_Code2.bmp')
                area = (30,3,38,18)
                cut_img = img.crop(area)
                cut_img.save('Result_'+str(x)+'_Code3.bmp')

