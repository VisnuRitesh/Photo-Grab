import cv2
import numpy as np
import os
import urllib

def store_raw_images():

    #Example link
    urllink=input("Enter link:")   
    neg_image_urls = urllib.urlopen(urllink).read().decode()
    pic_num = 1
    
    if not os.path.exists('/path'):
        os.makedirs('/path')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i, "/imgpath"+str(pic_num)+".jpg")
            img = cv2.imread("/imgpath"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("/imgpath"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))

def find_uglies():
    match = False
    for file_type in ['/path']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('/path/uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('/path/uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

def store_raw_images1():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'   
    neg_image_urls = urllib.urlopen(neg_images_link).read().decode()
    pic_num = 953
    
    if not os.path.exists('/path'):
        os.makedirs('/path')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i, "/imgpath"+str(pic_num)+".jpg")
            img = cv2.imread("/imgpath"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("/imgpath"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))


store_raw_images()
#find_uglies()
#store_rae_images1()
