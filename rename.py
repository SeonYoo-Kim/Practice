import os
import cv2

# 원본 파일명 CC:\Users\tjdn9\Documents\srdata\BSD100\LR_bicubic_PIL\X16
image_path = "C:/Users/tjdn9/Documents/srdata/DIV8k/LR_bicubic_PIL/X16"
filenames = [filename for filename in os.listdir(image_path) if filename.endswith(".png")]
save_path = "C:/Users/tjdn9/Documents/srdata/DIV8k/LR_bicubic_PIL/X16_bmp"

if not os.path.exists(save_path):
    os.makedirs(save_path)

for old_name in filenames:
    # "x4"를 제거한 새로운 파일명 생성
    img = cv2.imread(os.path.join(image_path, old_name), flags=cv2.IMREAD_COLOR)

    new_name = old_name.replace("png", "bmp")

    # 파일명 변경
    os.rename( os.path.join(image_path, old_name),  os.path.join(image_path, new_name))

    save_name = os.path.join(save_path, new_name)

    print(f"Renamed {old_name} to {new_name}")
    cv2.imwrite(save_name, img)
