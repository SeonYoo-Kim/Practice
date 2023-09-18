from math import log10, sqrt
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import os
import math
import os
import math
from datetime import datetime
import numpy as np
from PIL import Image
import cv2


#ori_folder C:C:\Users\tjdn9\Documents\srdata\DIV2k\LR_bicubic_PIL\X16
ori_folder = "C:/Users/tjdn9/Documents/srdata/DIV2k/LR_bicubic_PIL/X16"
#C:\UseC:\UseCC:CC:\Users\tjdn9\Documents\SuperResolution\data\DIV2K\valid\Augment\DIV2K_test_LR_aug\x16\non_aug
compare_folder = "C:/Users/tjdn9/Documents/SuperResolution/data/DIV2K/valid/Augment/DIV2K_test_LR_aug/x16/non_aug"
ori_filenames = [filename for filename in os.listdir(ori_folder) if filename.endswith(".png")]
compare_filenames = [filename for filename in os.listdir(compare_folder) if filename.endswith(".png")]
# Open and resize all images
images = []
print(ori_filenames)

def PSNR(original, compressed): #
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))

    return psnr

def PSNR2(original, compressed):
    mse = np.mean((original - compressed) ** 2, axis=(0,1))
    if np.all(mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(np.mean(mse)))
    return psnr
def rgb2ycbcr(img, only_y=True):
    '''same as matlab rgb2ycbcr
    only_y: only return Y channel
    Input:
        uint8, [0, 255]
        float, [0, 1]
    '''
    in_img_type = img.dtype
    img.astype(np.float32)
    if in_img_type != np.uint8:
        img *= 255.
    # convert
    if only_y:
        rlt = np.dot(img, [65.481, 128.553, 24.966]) / 255.0 + 16.0
    else:
        rlt = np.matmul(img, [[65.481, -37.797, 112.0], [128.553, -74.203, -93.786],
                                [24.966, 112.0, -18.214]]) / 255.0 + [16, 128, 128]
    if in_img_type == np.uint8:
        rlt = rlt.round()
    else:
        rlt /= 255.
    return rlt.astype(in_img_type)

def calc_metrics(img1, img2, crop_border, test_Y=True):
    #
    img1 = img1 / 255.
    img2 = img2 / 255.

    if test_Y and img1.shape[2] == 3:  # evaluate on Y channel in YCbCr color space
        im1_in = rgb2ycbcr(img1)
        im2_in = rgb2ycbcr(img2)
    else:
        im1_in = img1
        im2_in = img2
    height, width = img1.shape[:2]
    if im1_in.ndim == 3:
        cropped_im1 = im1_in[crop_border:height-crop_border, crop_border:width-crop_border, :]
        cropped_im2 = im2_in[crop_border:height-crop_border, crop_border:width-crop_border, :]
    elif im1_in.ndim == 2:
        cropped_im1 = im1_in[crop_border:height-crop_border, crop_border:width-crop_border]
        cropped_im2 = im2_in[crop_border:height-crop_border, crop_border:width-crop_border]
    else:
        raise ValueError('Wrong image dimension: {}. Should be 2 or 3.'.format(im1_in.ndim))

    psnr = calc_psnr(cropped_im1 * 255, cropped_im2 * 255)
    ssim = calc_ssim(cropped_im1 * 255, cropped_im2 * 255)
    return psnr, ssim

def calc_psnr(img1, img2):
    # img1 and img2 have range [0, 255]

    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    mse = np.mean((img1 - img2)**2)
    if mse == 0:
        return float('inf')
    return 20 * math.log10(255.0 / math.sqrt(mse))

def ssim2(img1, img2):

    C1 = (0.01 * 255)**2
    C2 = (0.03 * 255)**2

    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())

    mu1 = cv2.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(img2, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(img1**2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(img2**2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()


def calc_ssim(img1, img2):

    '''calculate SSIM
    the same outputs as MATLAB's
    img1, img2: [0, 255]
    '''
    if not img1.shape == img2.shape:
        raise ValueError('Input images must have the same dimensions.')
    if img1.ndim == 2:
        return ssim2(img1, img2)
    elif img1.ndim == 3:
        if img1.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim2(img1, img2))
            return np.array(ssims).mean()
        elif img1.shape[2] == 1:
            return ssim2(np.squeeze(img1), np.squeeze(img2))
    else:
        raise ValueError('Wrong input image dimensions.')

def main():
    # 파일 열기
    name_path = "C:/Users/tjdn9/Documents/SuperResolution/NAME.txt"
    #psnr_path = "C:/Users/tjdn9/Documents/SuperResolution/PSNR.txt"
    ssim_path = "C:/Users/tjdn9/Documents/SuperResolution/SSIM.txt"
    #psnr2_path = "C:/Users/tjdn9/Documents/SuperResolution/PSNR2.txt"
    psnr_paper_path = "C:/Users/tjdn9/Documents/SuperResolution/PSNR_paper.txt"
    file_mode = 'w'  # 쓰기 모드
    name_txt = open(name_path, file_mode)
    #psnr_txt = open(psnr_path, file_mode)
    ssim_txt = open(ssim_path, file_mode)
    #psnr2_txt = open(psnr2_path, file_mode)
    psnr_paper_txt = open(psnr_paper_path, file_mode)

    for filename in ori_filenames:

        name_txt.write(f"{filename}\n")

        ori_img = cv2.imread(os.path.join(ori_folder, filename), flags=cv2.IMREAD_COLOR)
        compare_img = cv2.imread(os.path.join(compare_folder, filename), flags=cv2.IMREAD_COLOR)

        ho, wo, co = ori_img.shape
        h, w, c = compare_img.shape

        if ((ho != h) or (wo != w)):
            compare_img = cv2.resize(compare_img, (wo, ho), cv2.INTER_CUBIC)

        value = PSNR(ori_img, compare_img)
        value2 = PSNR2(ori_img, compare_img)
        value3 , ssim3= calc_metrics(ori_img, compare_img, crop_border=4)
        #psnr_txt.write(f"{value}\n")
        #psnr2_txt.write(f"{value2}\n")
        psnr_paper_txt.write(f"{value3}\n")
        #print(f"{filename} PSNR value is {value} dB")
        #print(f"{filename} PSNR value2 is {value2} dB")
        print(f"{filename} PSNR value3 is {value3} dB")

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
    #psnr_txt.close()
    ssim_txt.close()

if __name__ == "__main__":
    main()
