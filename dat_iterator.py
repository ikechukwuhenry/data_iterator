# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 22:36:25 2017

@author: User
"""
import os
import cv2
import random as rd
import tensorflow as tf
import numpy as np
from PIL import Image as img



"""This function is gives the necessary condition requirement in creating 512X512 dimension before creating a 512x512 picture patch"""
def sizeCheck(sizeGen,width_height):
    val = sizeGen
    ans = width_height - val
    if ans >= 512:
         return 0
    else:
         return 1


 
"""Save a 1920x1080 dimension picture size created by the program.Initial image must have a dimenssion of 512 x 512 
or higher for this 512 x 512 dimension to be created"""    
def save(fileName,count):
    fileName1 = "C:/Users/User/Desktop/Python/pic/convert1920_1080" + str(count) + ".jpg"
    print("Saving File Temporaryly ","convert1920_1080_" + str(count))
    cv2.imwrite(str(fileName1),fileName)    


    
"""Function to resize the picture file"""
def fileResize1920_1080(save,count):
     for f in os.listdir('.'):
        
        if f.endswith('.jpg') or f.endswith('.png'):# or f.endswith('.png')
            img1 = cv2.imread(f,cv2.IMREAD_COLOR)
            
            """ Creating Image with dimension 1921 x 1080 and saving it in \pic\ directory"""
            #new_img = img1[1:1081 , 1:1921]
            new_img = cv2.resize(img1,(1920,1080))
            save(new_img,count)
            count += 1
            
            
def fileProcessing(sizeCheck,count):    
    for f in os.listdir('.'):
        
        if f.endswith('.jpg') or f.endswith('.png'):# or f.endswith('.png')
              
            fileName1 = "C:/Users/User/Desktop/Python/pic/convert1920_1080"+ str(count) +".jpg"
                       
            """ Opening the created image for processing inorder to get the size and the image itself"""
            image1 = img.open(fileName1)
            height,width = image1.size
            new_img = cv2.imread(fileName1,cv2.IMREAD_COLOR)
            
            
            """Random width and height size generated here"""
            sizeWidth = rd.randint(1,width)
            sizeHeight = rd.randint(1,height)
            
            if sizeCheck(sizeWidth,width) == 0 and sizeCheck(sizeHeight,height) == 0:
                new_img = new_img[sizeWidth:sizeWidth+512,sizeHeight:sizeHeight+512]
            elif sizeCheck(sizeWidth,width) == 0 and sizeCheck(sizeHeight,height) == 1:
                new_img = new_img[sizeWidth:sizeWidth+512,sizeHeight-512:sizeHeight]
            elif sizeCheck(sizeWidth,width) == 1 and sizeCheck(sizeHeight,height) == 0:
                new_img = new_img[sizeWidth-512:sizeWidth,sizeHeight:sizeHeight+512]
            else:
                new_img = new_img[sizeWidth-512:sizeWidth,sizeHeight-512:sizeHeight]
            
            
            cv2.imshow("File_processing"+str(count),new_img)
            #cv2.waitKey(0)
            cv2.destroyAllWindows()
            fileName11 = "C:/Users/User/Desktop/Python/final/done"+ str(count) +".jpg"
           
            message = "Saving File finally......................"+fileName11
            print(message)
            cv2.imwrite(fileName11,new_img)
            count += 1


def main():
    count = 1     
    """This is used to resize file to 1920 x 1080 but your picture must have higher dmension
    Not required to run fileResize1920_1080(save,count) if your file is 1920 x 1080"""
     
    fileResize1920_1080(save,count)
    
    fileProcessing(sizeCheck,count)      
    
    image1= False
    image2 = False
    directory = "C:/Users/User/Desktop/Python/final/"
    sess = tf.InteractiveSession()
    for f in os.listdir(directory):
            
            if f.endswith('.jpg') or f.endswith('.png'):
                image1 = tf.image.decode_jpeg(tf.read_file(directory+f),channels=1)
                image2 += np.asarray(sess.run(image1))
                """Optional to run this"""
                #print(sess.run(image1)) 
                print(image2)

  
if __name__ == "__main__":
    main()



           