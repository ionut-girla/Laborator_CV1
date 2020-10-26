#print("Salut")
#import matplotlib.pyplot as plt
#image = plt.imread('path')
#plt.imshow(image)


import cv2
image = cv2.imread('path')
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#import <opencv/cv.h>
#import <string>

int main(){
        std::string s = 'path'
        cv::Mat im = imread ('path')
        imshow('image', image);
        cv:waitKey(0)
        }
