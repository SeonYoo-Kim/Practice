import cv2
import os
# 이미지 파일 경로 지정C:\Users\tjdn9\Documents\SuperResolution\DIV2K_train\Augment\DIV2K_train_LR_aug\x32
image_path = "C:/Users/tjdn9/Documents/SuperResolution/DIV2K_valid/Augment/DIV2K_test_LR_aug/x32"
filenames = [filename for filename in os.listdir(image_path) if filename.endswith(".png")]

# 이미지 읽어오기
for filename in filenames:
    img = cv2.imread(os.path.join(image_path, filename), flags=cv2.IMREAD_COLOR)

# 보간법 지정 (Bicubic Interpolation)
    interpolation = cv2.INTER_CUBIC

# 이미지 resize
# 여러 scale로 resize하려면 리스트 등을 사용하여 원하는 크기를 지정하면 됩니다.
    #resized_img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2), interpolation=interpolation)
    #resized_img = cv2.resize(img, (img.shape[1]*3, img.shape[0]*3), interpolation=interpolation)
    #resized_img = cv2.resize(img, (img.shape[1]*4, img.shape[0]*4), interpolation=interpolation)
    #resized_img = cv2.resize(img, (img.shape[1]*8, img.shape[0]*8), interpolation=interpolation)
    resized_img = cv2.resize(img, (img.shape[1]*16, img.shape[0]*16), interpolation=interpolation)
    #resized_img = cv2.resize(img, (img.shape[1]*32, img.shape[0]*32), interpolation=interpolation)

    #이미지 저장
    save_name = "C:/Users/tjdn9/Documents/SuperResolution/DIV2K_valid/LR_resize/x32/{}".format(filename)
    cv2.imwrite(save_name, resized_img)