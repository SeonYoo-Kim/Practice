from math import log10, sqrt
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import os
#          CC:\Users\tjdn9\Documents\SuperResolution\acc\Results\x4x2x2\MLx4MLx2FSx2\KBS_logo
ori_folder = "C:/Users/tjdn9/Documents/SuperResolution/acc/Results/x4x2x2/MLx4MLx2FSx2/new_logo"
compare_folder = "C:/Users/tjdn9/Documents/SuperResolution/acc/Results/x4x2x2/MLx4MLx2FLx2/new_logo"
compare_folder1 = "C:/Users/tjdn9/Documents/SuperResolution/acc/Results/x4x4/SLx4x4/new_logo"
ori_filenames = [filename for filename in os.listdir(ori_folder) if filename.endswith(".png")]
compare_filenames = [filename for filename in os.listdir(compare_folder) if filename.endswith(".png")]

# 모든 이미지를 열고 크기 조정
images = []
print(ori_filenames)

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def main():
    for filename in ori_filenames:
        ori_name = "{}/{}".format(ori_folder, filename)
        ori_img = Image.open(ori_name)
        ori_crop = ori_img.crop((0, 0, 390, 230))
        #ori_crop = ori_img.crop((0, 0, 1024, 416))
        ori_crop_np = np.array(ori_crop)  # PIL 이미지를 NumPy 배열로 변환
        save_name = '{}/crop/{}'.format(ori_folder, filename)
        cv2.imwrite(save_name, cv2.cvtColor(ori_crop_np, cv2.COLOR_RGB2BGR))  # BGR 형식으로 저장

        compare_name = "{}/{}".format(compare_folder, filename)
        compare_img = Image.open(compare_name)
        compare_crop = compare_img.crop((0, 0, 390, 230))
        #compare_crop = compare_img.crop((0, 0, 1024, 416))
        compare_crop_np = np.array(compare_crop)  # PIL 이미지를 NumPy 배열로 변환
        save_name = '{}/crop/{}'.format(compare_folder, filename)
        cv2.imwrite(save_name, cv2.cvtColor(compare_crop_np, cv2.COLOR_RGB2BGR))  # BGR 형식으로 저장

        name = "{}/{}".format(compare_folder1, filename)
        img = Image.open(name)
        crop = ori_img.crop((0, 0, 390, 230))
        #crop = img.crop((0, 0, 1024, 416))
        crop_np = np.array(crop)  # PIL 이미지를 NumPy 배열로 변환
        save_name = '{}/crop/{}'.format(compare_folder1, filename)
        cv2.imwrite(save_name, cv2.cvtColor(crop_np, cv2.COLOR_RGB2BGR))  # BGR 형식으로 저장

if __name__ == "__main__":
    main()
