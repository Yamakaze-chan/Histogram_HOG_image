import numpy as np
import cv2
from matplotlib import pyplot as plt
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

def HOG(mode, path):
    img = cv2.imread(path,0)
    #img = cv2.resize(img, (32,32), interpolation = cv2.INTER_AREA)
    if(mode == 1):
        arr = img.ravel()
        arr.sort()
        hog_arr = []
        hog_arr.append([arr[0],1])
        i = 1
        y = 0
        while 1:
            if(arr[i] == arr[y]):
                hog_arr[y][1] = hog_arr[y][1] + 1
            else:
                hog_arr.append([arr[i],1])
                y = y + 1
            i = i + 1
            if(i == len((arr))):
                break
        #PLOT
        plt.plot(np.array(hog_arr)[:, 1]) #([0]: color ; [1]: counting)
        plt.show()
        #print(np.array(hog_arr)[:, 1])
        print(max(np.array(hog_arr)[:, 1]))
        #return
        return np.array(hog_arr)
    if(mode == 2):
        #cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
        plt.hist(img.ravel(),256,[0,256])
        plt.show()
        #return histr
#print(HOG(1, 'img\F3Ur0MUa8AAs9mZ.jfif'))
suppress_qt_warnings()
HOG(1, 'img\FmL6iHsaEAAysAd.jfif')
