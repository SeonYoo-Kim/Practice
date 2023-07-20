from math import log10, sqrt
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def main():                #C:\Users\tjdn9\Documents\SuperResolution\Set5\DataSet\HR
    original = cv2.imread("C:/Users/tjdn9/Documents/SuperResolution/Set5/DataSet/HR/baby.png")
    compressed = cv2.imread("C:/Users/tjdn9/Documents/SuperResolution/Set5/Results/SRFBN/x2/baby-S.png", 1)
    #ori_resize = np.shape(originl)
    #ori_resize = original.shape
    
    #h, w, c = compressed.shape
    #ori_resize = cv2.resize(original, (1920, 1080))
    #value = PSNR(ori_resize, compressed)
    value = PSNR(original, compressed)
    print(f"PSNR value is {value} dB")

    # 3. Load the two input images
    #imageA = cv2.imread("10_8blendsrcnn_x3.pth_x3.png")
    #imageB = cv2.imread("10_8blend.png")
    # 만약 url에서 불러올 거면 다음을 활용
    # imageA = io.imread(args["first"])
    # imageB = io.imread(args["second"])

    # imageC = cv2.resize(imageB, (255,255))
    #imageC = cv2.resize(imageB, (510, 510))
    # 4. Convert the images to grayscale
    grayA = cv2.cvtColor(compressed, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    # 5. Compute the Structural Similarity Index (SSIM) between the two
    #    images, ensuring that the difference image is returned
    (score, diff) = ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")

    print("SSIM: {}".format(score))


if __name__ == "__main__":
    main()


