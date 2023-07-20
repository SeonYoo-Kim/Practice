from configparser import Interpolation
import cv2
import os
# 이미지 파일 경로 지정C:\Users\tjdn9\Documents\srdata\MANGA109\HR
image_path = "C:/Users/tjdn9/Documents/srdata/DIV8k/HR"
save_path = "C:/Users/tjdn9/Documents/srdata/DIV8k/LR_bicubic/X16"
filenames = [filename for filename in os.listdir(image_path) if filename.endswith(".png")]
scale = 16

# 이미지 읽어오기
for filename in filenames:
    img = cv2.imread(os.path.join(image_path, filename), flags=cv2.IMREAD_COLOR)
    h, w, c = img.shape
    h /= scale
    w /= scale
    #img_origin = cv2.imread(os.path.join(image_path_origin, filename), flags=cv2.IMREAD_COLOR)

#    h, w, c = img_origin.shape
    

# 이미지 resize
# 여러 scale로 resize하려면 리스트 등을 사용하여 원하는 크기를 지정하면 됩니다.
    #4K 2배
    #resized_img = cv2.resize(img, (1920, 1080))
    #4K 3배
    #resized_img = cv2.resize(img, (1280, 720))
    #4K 4배
    #resized_img = cv2.resize(img, (960, 540),cv2.INTER_CUBIC)
    #4K 8배
    #resized_img = cv2.resize(img, (480, 270))
    #4K 16배
    #resized_img = cv2.resize(img, (240, 135), cv2.INTER_CUBIC)
    #4K 32배
    resized_img = cv2.resize(img, (int(w), int(h)), cv2.INTER_CUBIC)
    #resized_img = cv2.resize(img, (35, 35), Interpolation=cv2.INTER_CUBIC)

    #imagenet 2배
    #resized_img = cv2.resize(img, (512, 384))
    #imagenet 3배
    #resized_img = cv2.resize(img, (338, 254))
    #imagenet 4배
    #resized_img = cv2.resize(img, (256, 192))
    #imagenet 8배
    #resized_img = cv2.resize(img, (128, 96))
    #imagenet 16배
    #resized_img = cv2.resize(img, (64, 48))
    #imagenet 32배
    #resized_img = cv2.resize(img, (32, 24))

    #LOGO 2배
    #resized_img = cv2.resize(img, (2200, 1238))
    #LOGO 3배
    #resized_img = cv2.resize(img, (338, 254))
    #LOGO 4배
    #resized_img = cv2.resize(img, (256, 192))
    #LOGO 8배
    #resized_img = cv2.resize(img, (128, 96))
    #LOGO 16배
    #resized_img = cv2.resize(img, (64, 48))
    #LOGO 32배
    #resized_img = cv2.resize(img, (14, 8), cv2.INTER_CUBIC)
    
    #이미지 저장 C:\Users\tjdn9\Documents\SuperResolution\4\x2
    save_name = os.path.join(save_path, filename)
    
    cv2.imwrite(save_name, resized_img)