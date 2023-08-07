import cv2
import os
from PIL import Image, ImageOps
# 이미지 파일 경로 지C:\Users\tjdn9\Documents\srdata\BSD100\HR
LR_path = "C:/Users/tjdn9/Documents/srdata/MANGA109/LR_bicubic/DBPNX8"
save_path = "C:/Users/tjdn9/Documents/SuperResolution/TEST/0_Bicubic/x8/CV2_MANGA109"
filenames = [filename for filename in os.listdir(LR_path) if filename.endswith(".png")]
scale = 8

# 이미지 읽어오기
for filename in filenames:
    # LR = Image.open(os.path.join(LR_path, filename)).convert('RGB')
    # Bicubic = LR.resize((int(LR.size[0] * scale), int(LR.size[1] * scale)), Image.BICUBIC)
    img = cv2.imread(os.path.join(LR_path, filename), flags=cv2.IMREAD_COLOR)

# 보간법 지정 (Bicubic Interpolation)
    # interpolation = cv2.INTER_CUBIC

# 이미지 resize
# 여러 scale로 resize하려면 리스트 등을 사용하여 원하는 크기를 지정하면 됩니다.
    #resized_img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2), interpolation=interpolation)
    #resized_img = cv2.resize(img, (img.shape[1]*3, img.shape[0]*3), interpolation=interpolation)
    #resized_img = cv2.resize(img, (img.shape[1]*4, img.shape[0]*4), interpolation=interpolation)
    resized_img = cv2.resize(img, (img.shape[1]*8, img.shape[0]*8), cv2.INTER_CUBIC)
    #resized_img = cv2.resize(img, (img.shape[1]*16, img.shape[0]*16), interpolation=interpolation)
    #resized_img = cv2.resize(img, (img.shape[1]*32, img.shape[0]*32), interpolation=interpolation)

    #이미지 저장
    #save_name = "C:/Users/tjdn9/Documents/SuperResolution/abc/Bicubicx4/Urban100/{}".format(filename)
    cv2.imwrite(os.path.join(save_path, filename), resized_img)
    #Bicubic.save(os.path.join(save_path, filename))