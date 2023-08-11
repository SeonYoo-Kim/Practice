from configparser import Interpolation
import cv2
from PIL import Image, ImageOps
import os
# 업스케일링
LR_path = "C:/Users/tjdn9/Documents/srdata/T-91/LR_bicubic_PIL/X8"
filenames = [filename for filename in os.listdir(LR_path) if filename.endswith(".png")]

# 다운스케일링
# HR_path = "C:/Users/tjdn9/Documents/srdata/T-91/HR"
# filenames = [filename for filename in os.listdir(HR_path) if filename.endswith(".png")]

save_path = "C:/Users/tjdn9/Documents/srdata/T-91/LR_bicubic_PIL/X8_resized"
scale = 8


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
    resized_img = cv2.resize(HR, (int(HR.shape[0] / scale), int(HR.shape[1] / scale)), cv2.INTER_CUBIC)
    save_name = os.path.join(save_path, filename)
    cv2.imwrite(save_name, resized_img)
def CV2_UP(filename, LR_path, save_path):
    LR = cv2.imread(os.path.join(LR_path, filename), flags=cv2.IMREAD_COLOR)
    resized_img = cv2.resize(LR, ((LR.shape[0] * scale), (LR.shape[1] * scale)), cv2.INTER_CUBIC)
    save_name = os.path.join(save_path, filename)
    cv2.imwrite(save_name, resized_img)

if __name__ == "__main__":
    mkdir(save_path)

    for filename in filenames:
        # PIL_DOWN(filename, HR_path, save_path)
        PIL_UP(filename, LR_path, save_path)
        # CV2_DOWN(filename, HR_path, save_path)
        #CV2_UP(filename, LR_path, save_path)