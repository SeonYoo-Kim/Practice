from configparser import Interpolation
import cv2
from PIL import Image, ImageOps
import os
# 업스케일링 CC:\Users\tjdn9\Documents\srdata\Set5\LR_bicubic_PIL\X16
LR_path = "C:/Users/tjdn9/Documents/srdata/Set14/LR_bicubic_PIL/X16"
filenames = [filename for filename in os.listdir(LR_path) if filename.endswith(".png")]
# HR_path = "C:/Users/tjdn9/Documents/srdata/Set5/HR"
# 다운스케일링 C:\Users\tjdn9\Documents\srdata\BSD100\HR
#HR_path = "C:/Users/tjdn9/Documents/srdata/DIV8k/HR"
#filenames = [filename for filename in os.listdir(HR_path) if filename.endswith(".png")]
# C:\Users\tjdn9\Documents\SuperResolution\TEST\0_Bicubic\x8\MANGA109
save_path = "C:/Users/tjdn9/Documents/SuperResolution/TEST/0_Bicubic/PILx16/Set14"
scale = 16

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
def PIL_DOWN(filename, HR_path, save_path):
    HR = Image.open(os.path.join(HR_path, filename)).convert('RGB')
    LR = HR.resize((int(HR.size[0] / scale), int(HR.size[1] / scale)), Image.BICUBIC)
    save_name = os.path.join(save_path, filename)
    LR.save(save_name)
def PIL_UP(filename, LR_path, save_path):
    LR = Image.open(os.path.join(LR_path, filename)).convert('RGB')
    HR = LR.resize((int(LR.size[0] * scale), int(LR.size[1] * scale)), Image.BICUBIC)
    save_name = os.path.join(save_path, filename)
    HR.save(save_name)
def CV2_DOWN(filename, HR_path, save_path):
    HR = cv2.imread(os.path.join(HR_path, filename), flags=cv2.IMREAD_COLOR)
    resized_img = cv2.resize(HR, (int(HR.shape[1] / scale), int(HR.shape[0] / scale)), cv2.INTER_CUBIC)
    save_name = os.path.join(save_path, filename)
    cv2.imwrite(save_name, resized_img)
def CV2_UP(filename, LR_path, save_path):
    LR = cv2.imread(os.path.join(LR_path, filename), flags=cv2.IMREAD_COLOR)
    resized_img = cv2.resize(LR, ((LR.shape[1] * scale), (LR.shape[0] * scale)), cv2.INTER_CUBIC)
    save_name = os.path.join(save_path, filename)
    cv2.imwrite(save_name, resized_img)
def PIL_HRsize(filename, LR_path, HR_path, save_path):
    LR = Image.open(os.path.join(LR_path, filename)).convert('RGB')
    HR = Image.open(os.path.join(HR_path, filename)).convert('RGB')
    resized = LR.resize((HR.size[0], HR.size[1]), Image.BICUBIC)
    save_name = os.path.join(save_path, filename)
    resized.save(save_name)
if __name__ == "__main__":

    if not os.path.exists(save_path):
        mkdir(save_path)
    for filename in filenames:
        #PIL_DOWN(filename, HR_path, save_path)
        PIL_UP(filename, LR_path, save_path)
        #CV2_DOWN(filename, HR_path, save_path)
        #CV2_UP(filename, LR_path, save_path)
        #PIL_HRsize(filename, LR_path, HR_path, save_path)
