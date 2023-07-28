from math import log10, sqrt
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import os
#C:\Users\tjdn9\Documents\SuperResolution\TEST\x16\2_M-FBN-S_x4_2\DIV8K
ori_folder = "C:/Users/tjdn9/Documents/srdata/DIV8k/HR"
compare_folder = "C:/Users/tjdn9/Documents/SuperResolution/TEST/x16/SRFBN/1_MLx4_2_MLx4/DIV8k"
ori_filenames = [filename for filename in os.listdir(ori_folder) if filename.endswith(".png")]
compare_filenames = [filename for filename in os.listdir(compare_folder) if filename.endswith(".png")]
# Open and resize all images
images = []
print(ori_filenames)
# for filename in image_filenames:
#     ori_img = cv2.imread(os.path.join(ori_folder, filename), flags=cv2.IMREAD_COLOR)
#     compare_img = cv2.imread(os.path.join(compare_folder, filename), flags=cv2.IMREAD_COLOR)
def PSNR(original, compressed): #
    #mse = np.mean((original[0:230, 0:390] - compressed[0:230, 0:390]) ** 2)
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
def main():
    # original = cv2.imread("10_16blend.png")
    # compressed = cv2.imread("10_16blend4blend_train.pth_x3.png", 1)

    # 파일 열기
    name_path = 'C:/Users/tjdn9/Documents/SuperResolution/NAME.txt'
    psnr_path = 'C:/Users/tjdn9/Documents/SuperResolution/PSNR.txt'
    ssim_path = 'C:/Users/tjdn9/Documents/SuperResolution/SSIM.txt'
    file_mode = 'w'  # 쓰기 모드
    name_txt = open(name_path, file_mode)
    psnr_txt = open(psnr_path, file_mode)
    ssim_txt = open(ssim_path, file_mode)

    for filename in ori_filenames:

        #name_txt.write(f"{filename}\n")

        ori_img = cv2.imread(os.path.join(ori_folder, filename), flags=cv2.IMREAD_COLOR)
        compare_img = cv2.imread(os.path.join(compare_folder, filename), flags=cv2.IMREAD_COLOR)

        ho, wo, co = ori_img.shape
        h, w, c = compare_img.shape
        if ((ho != h) or (wo != w)):
            compare_img = cv2.resize(compare_img, (wo, ho), cv2.INTER_CUBIC)

        value = PSNR(ori_img, compare_img)
        psnr_txt.write(f"{value}\n")
        print(f"{filename} PSNR value is {value} dB")

        grayA = cv2.cvtColor(compare_img, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(ori_img, cv2.COLOR_BGR2GRAY)
        #
        # # 5. Compute the Structural Similarity Index (SSIM) between the two
        # #    images, ensuring that the difference image is returned
        (score, diff) = ssim(grayA, grayB, full=True)
        # diff = (diff * 255).astype("uint8")
        ssim_txt.write(f"{score}\n")
        print("SSIM: {}".format(score))

    name_txt.close()
    psnr_txt.close()
    ssim_txt.close()

if __name__ == "__main__":
    main()
