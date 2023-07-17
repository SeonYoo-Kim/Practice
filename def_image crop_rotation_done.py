import os
from PIL import Image
import numpy as np
import cv2
import PIL.Image
from PIL import Image
import math
# Get all image filenames in the folder
import cv2
import random
#h, w = img1.shape[:2]
#print(h, w)
# Open and resize all images
HR_folder = ["C:/Users/user/Desktop/Mypaper/DataSet/DIV2K_SW/train/HR/HR",
             "C:/Users/user/Desktop/Mypaper/DataSet/DIV2K_SW/train/LR/x2",
             "C:/Users/user/Desktop/Mypaper/DataSet/DIV2K_SW/train/LR/x4",
             "C:/Users/user/Desktop/Mypaper/DataSet/DIV2K_SW/train/LR/x8",
             "C:/Users/user/Desktop/Mypaper/DataSet/DIV2K_SW/train/LR/x16",
             "C:/Users/user/Desktop/Mypaper/DataSet/DIV2K_SW/train/LR/x32"]

def main():

    HR_filenames = [filename for filename in os.listdir(HR_folder[0]) if filename.endswith(".png")] # UHD

    for filename in HR_filenames:
        x, y = 0, 0
        rotation_angle = random.choice([0, 90, 180, 270])
        for i in range(5):
            img = cv2.imread(os.path.join(HR_folder[i], filename), flags=cv2.IMREAD_COLOR)

            if(i == 0):
                x, y = get_xy(img)
                crop_HR = crop_img_HR(x, y, img)
                rot = rotation(crop_HR, rotation_angle)
            else :
                crop_LR = crop_img_LR(x, y, img)
                rot = rotation(crop_LR, rotation_angle)
            save_img(rot, filename, HR_folder[i])

def image_read(x,y) :
    img = cv2.imread(os.path.join(x, y), flags=cv2.IMREAD_COLOR)
    return img

def get_xy(x) :
    h, w, c = x.shape
    start_x = random.randint(0, w - 60)
    start_y = random.randint(0, h - 60)
    return start_x, start_y

def crop_img_LR(x,y ,img) :
    crop_img = img[y/2:y/2 + 60, x/2:x/2 + 60]
    return crop_img

def crop_img_HR(x,y ,img) :
    crop_img = img[y:y + 120, x:x + 120]
    return crop_img

def rotation(x, a) :
    rows, cols = x.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), a, 1)
    rotated_crop = cv2.warpAffine(x,M, (cols, rows))
    return rotated_crop

def save_img(x ,y, z) :
    save_name_HR = "{}/rotation_{}".format(z,y)
    cv2.imwrite(save_name_HR, x)
    return