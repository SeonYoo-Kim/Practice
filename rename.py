import os
import cv2

# 원본 파일명 CEC:\Users\tjdn9\Documents\SuperResolution\data\DIV2K\valid\Augment\DIV2K_test_LR_aug\x16\non_aug
image_path = "C:/Users/tjdn9/Documents/SuperResolution/data/DIV2K/valid/Augment/DIV2K_test_LR_aug/x16/non_aug"
filenames = [filename for filename in os.listdir(image_path) if filename.endswith(".png")]
#save_path = "C:/Users/tjdn9/Documents/srdata/Set5/HR_bmp"

# if not os.path.exists(save_path):
#     os.makedirs(save_path)

for old_name in filenames:
    # "x4"를 제거한 새로운 파일명 생성
    img = cv2.imread(os.path.join(image_path, old_name), flags=cv2.IMREAD_COLOR)

    new_name = old_name.replace("_rot0_ds0", "")

    # 파일명 변경
    os.rename( os.path.join(image_path, old_name),  os.path.join(image_path, new_name))

    save_name = os.path.join(image_path, new_name)

    print(f"Renamed {old_name} to {new_name}")
    cv2.imwrite(save_name, img)
