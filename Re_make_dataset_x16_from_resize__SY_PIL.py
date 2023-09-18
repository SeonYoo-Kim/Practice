from configparser import Interpolation
import cv2
from PIL import Image, ImageOps
import os
from glob import glob
#from flags import *
import os
from scipy import misc
import numpy as np
import datetime
import imageio
from multiprocessing.dummy import Pool as ThreadPool

Read_HR_dir='C:/Users/tjdn9/Documents/SuperResolution/data/DIV2K/valid/DIV2K_valid_HR'
save_dir='C:/Users/tjdn9/Documents/SuperResolution/data/DIV2K/valid/PIL_LR/x4'
starttime = datetime.datetime.now()
def mkdir2(path, i):
    if not os.path.exists(path):
        save_HR_path = os.path.join(save_dir, 'HR_x{}'.format(i))
        save_LR_path = os.path.join(save_dir, 'LR_x{}'.format(i))
        save_HR_path = save_HR_path.replace('\\', '/')
        save_LR_path = save_LR_path.replace('\\', '/')
        os.mkdir(save_HR_path)
        os.mkdir(save_LR_path)


# 업스케일링 C:\Users\tjdn9\Documents\srdata\T-91\HR
# LR_path = "C:/Users/tjdn9/Documents/srdata/Set5/LR_bicubic_PIL/X2"
# filenames = [filename for filename in os.listdir(LR_path) if filename.endswith(".png")]
# HR_path = "C:/Users/tjdn9/Documents/srdata/Set5/HR"
# 다운스케일링 C:\Users\tjdn9\Documents\srdata\BSD100\HR

filenames = [filename for filename in os.listdir(Read_HR_dir) if filename.endswith(".png")]

#save_path = "C:/Users/tjdn9/Documents/srdata/DIV8k/LR_bicubic_PIL/X8"
scale = 4

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
def PIL_DOWN(HR, scale, ratio):

    LR = HR.resize((int(HR.size[0] / scale), int(HR.size[1] / scale)), Image.BICUBIC)
    HR = LR.resize((int(LR.size[0] * 4), int(LR.size[1] * 4)), Image.BICUBIC)
    save_name_HR = os.path.join(save_dir, 'HR_x{}'.format(ratio), "{}_{}".format(scale, filename))
    HR.save(save_name_HR)
    save_name_LR = os.path.join(save_dir, 'LR_x{}'.format(ratio), "{}_{}".format(scale, filename))
    LR.save(save_name_LR)

def PIL_Rotation (HR, scale, ratio):
    LR = HR.resize((int(HR.size[0] / scale), int(HR.size[1] / scale)), Image.BICUBIC)

    rot180_img= rotation(LR, 180)
    HR = rot180_img.resize((int(rot180_img.size[0] * 4), int(LR.size[1] * 4)), Image.BICUBIC)
    save_name_HR = os.path.join(save_dir, 'HR_x{}'.format(ratio), "rotated_{}_{}".format(scale, filename))
    HR.save(save_name_HR)
    save_name_LR = os.path.join(save_dir, 'LR_x{}'.format(ratio), "rotated_{}_{}".format(scale, filename))
    rot180_img.save(save_name_LR)

def rotation(x, a) :
    rows, cols = x.size
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), a, 1)
    rotated_img = x.rotate(a, resample=Image.BICUBIC)
    return rotated_img

def PIL_size(img, scale) :
    LR = img.resize((int(HR.size[0] / scale), int(HR.size[1] / scale)), Image.BICUBIC)
    return LR
def PIL_UP(filename, LR_path, save_path):
    LR = Image.open(os.path.join(LR_path, filename)).convert('RGB')
    HR = LR.resize((int(LR.size[0] * scale), int(LR.size[1] * scale)), Image.BICUBIC)
    save_name = os.path.join(save_path, filename)
    HR.save(save_name)
def CV2_DOWN(filename, HR_path, save_path):
    HR = cv2.imread(os.path.join(HR_path, filename), flags=cv2.IMREAD_COLOR)
    resized_img = cv2.resize(HR, (int(HR.shape[0] / scale), int(HR.shape[1] / scale)), cv2.INTER_CUBIC)
    save_name = os.path.join(save_path, filename)
    cv2.imwrite(save_name, resized_img)
def CV2_UP(filename, LR_path, save_path):
    LR = cv2.imread(os.path.join(LR_path, filename), flags=cv2.IMREAD_COLOR)
    resized_img = cv2.resize(LR, ((LR.shape[0] * scale), (LR.shape[1] * scale)), cv2.INTER_CUBIC)
    save_name = os.path.join(save_path, filename)
    cv2.imwrite(save_name, resized_img)
def PIL_HRsize(filename, LR_path, HR_path, save_path):
    LR = Image.open(os.path.join(LR_path, filename)).convert('RGB')
    HR = Image.open(os.path.join(HR_path, filename)).convert('RGB')
    resized = LR.resize((HR.size[0], HR.size[1]), Image.BICUBIC)
    save_name = os.path.join(save_path, filename)
    resized.save(save_name)
def modcrop(image, scale) -> object:
	if len(image.shape) == 3:
		h, w, _ = image.shape
		h = h - np.mod(h, scale)
		w = w - np.mod(w, scale)
		image = image[0:h, 0:w, :]
	else:
		h, w = image.shape
		h = h - np.mod(h, scale)
		w = w - np.mod(w, scale)
		image = image[0:h, 0:w]
	return image
def save_HR_LR(img, size, path, idx):
    #HR_img = misc.imresize(img, size, interp='bicubic')
    HR_img = modcrop(img, i)
    rot180_img = misc.imrotate(HR_img, 180)
    #x4_img = misc.imresize(HR_img, 1 / 4, interp='bicubic')
    x4_img = PIL_size(img, size)
    #x4_rot180_img = misc.imresize(rot180_img, 1 / 4, interp='bicubic')
    x4_rot180_img = PIL_size(rot180_img, size)
    img_path = path.split('/')[-1].split('.')[0] + '_rot0_' + 'ds' + str(idx) + '.png'
    rot180img_path = path.split('/')[-1].split('.')[0] + '_rot180_' + 'ds' + str(idx) + '.png'
    x4_img_path = path.split('/')[-1].split('.')[0] + '_rot0_' + 'ds' + str(idx) + '.png'
    x4_rot180img_path = path.split('/')[-1].split('.')[0] + '_rot180_' + 'ds' + str(idx) + '.png'

    misc.imsave(save_dir + '/' + img_path, HR_img)
    misc.imsave(save_dir + '/' + rot180img_path, rot180_img)
    misc.imsave(save_dir + '/' + x4_img_path, x4_img)
    misc.imsave(save_dir + '/' + x4_rot180img_path, x4_rot180_img)
if __name__ == "__main__":
    ratio = [4,16]
    HR_size = [1.0, 0.8, 0.7, 0.6, 0.5]
    # for i in ratio :
    #     mkdir2(save_path, i)

    for i in ratio :

        for filename in filenames:

            HR = Image.open(os.path.join(Read_HR_dir, filename)).convert('RGB')

            for size in HR_size:
                PIL_DOWN(HR,i/size, i)
                PIL_Rotation(HR, i/size, i)


        #PIL_UP(filename, LR_path, save_path)
        #CV2_DOWN(filename, HR_path, save_path)
        #CV2_UP(filename, LR_path, save_path)
        #PIL_HRsize(filename, LR_path, HR_path, save_path)