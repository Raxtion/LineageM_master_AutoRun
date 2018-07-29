import numpy as np
import cv2
import os
import timer

T = timer.Timer()

Train_Index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

trains_list = np.array([])
labels_list = np.array([])
T.timestart()
for index in Train_Index:
    os.chdir('C:\\Users\\raxku\\OneDrive\\Documents\\FunctionLib\\python\\pyCode\\MachineLearning_leaning\\LetterRecognition\KNN\\\picture\\' + str(index) + '_magic')
    file_list = os.listdir()
   
    for file in file_list:
        #print(file)
        img = cv2.imread(file)
        #print("img=", img.shape)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     #type = np.array((15x8), 'uint8')
        #print("img=", gray.shape)
        data = gray.reshape(1, 15*8).astype('float32') #type = np.array((150), 'float32')
        label = np.array([index]).reshape(1, 1).astype('int32')
        if trains_list.size == 0:
            trains_list = data
        else:
            trains_list = np.vstack((trains_list, data))
        if labels_list.size == 0:
            labels_list = label
        else:
            labels_list = np.vstack((labels_list, label))
print(T.timepass())

knn = cv2.ml.KNearest_create()
knn.train(trains_list, cv2.ml.ROW_SAMPLE, labels_list)
np.save('trains_list_magic.npy', trains_list)
np.save('labels_list_magic.npy', labels_list)

quit()

trains_list = np.load(os.getcwd() + '\\picture\\trains_list_magic.npy')
labels_list = np.load(os.getcwd() + '\\picture\\labels_list_magic.npy')

knn = cv2.ml.KNearest_create()
knn.train(trains_list, cv2.ml.ROW_SAMPLE, labels_list)

testdata = np.array([])
os.chdir(r'C:\Users\raxku\OneDrive\Documents\FunctionLib\python\pyCode\MachineLearning_leaning\LetterRecognition\KNN\picture')
file_list = [x for x in os.listdir() if 'Result' in x]

for file in file_list:
    testimg = cv2.imread(file)
    testgray = cv2.cvtColor(testimg,cv2.COLOR_BGR2GRAY)
    data = testgray.reshape(1, 15*10).astype('float32')
    if testdata.size == 0:
        testdata = data
    else:
        testdata = np.vstack((testdata, data))

ret, result, neighbours, dist = knn.findNearest(testdata, k=3)


print(ret)
print(result)
print(neighbours)
print(dist)

print(file_list[0], ' = ', result[0])
print(file_list[1], ' = ', result[1])
print(file_list[2], ' = ', result[2])





# result
#    5.0
#    [[5.]
#     [8.]
#     [4.]]
#    [[5. 5. 5.]
#     [8. 8. 8.]
#     [4. 4. 4.]]
#    [[134480. 153950. 180081.]
#     [  4845.  65411.  97760.]
#     [ 17515.  18287. 318004.]]
#    Result_20180326015701_Code1.bmp  =  [5.]
#    Result_20180326015701_Code2.bmp  =  [8.]
#    Result_20180326015701_Code3.bmp  =  [4.]




#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#