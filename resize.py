from configparser import Interpolation
import cv2
from PIL import Image, ImageOps
import os
# 이미지 파일C:\Users\tjdn9\Documents\srdata\Urban100\LR_bicubic\X4_CV2
#LR_path = C:\Users\tjdn9\Documents\srdata\T-91\HR
HR_path = "C:/Users/tjdn9/Documents/srdata/T-91/HR"
save_path = "C:/Users/tjdn9/Documents/srdata/T-91/LRx4"
#filenames = [filename for filename in os.listdir(LR_path) if filename.endswith(".png")]
filenames = [filename for filename in os.listdir(HR_path) if filename.endswith(".png")]
scale = 4

# 이미지 읽어오기
for filename in filenames:
    # HR = Image.open(os.path.join(HR_path, filename)).convert('RGB')
    # LR = HR.resize((int(HR.size[0] * scale), int(HR.size[1] * scale)), Image.BICUBIC)
    # save_name = os.path.join(save_path, filename)
    # LR.save(save_name)

    HR = cv2.imread(os.path.join(HR_path, filename), flags=cv2.IMREAD_COLOR)
    h, w, c = HR.shape
    h /= scale
    w /= scale

    #LR = cv2.imread(os.path.join(LR_path, filename), flags=cv2.IMREAD_COLOR)
    # h, w, c = LR.shape
    # h *= scale
    # w *= scale
    resized_img = cv2.resize(HR, (int(w), int(h)), cv2.INTER_CUBIC)
    save_name = os.path.join(save_path, filename)
    cv2.imwrite(save_name, resized_img)