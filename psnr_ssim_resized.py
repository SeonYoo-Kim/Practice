from math import log10, sqrt
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image


    #h, w, c = compressed.shape

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def main():                 # C:\Users\tjdn9\Documents\SuperResolution\3_blend\DataSet\ImageNet\IMG_KBS blend_imgnet\HD\tmp
    original = cv2.imread("C:/Users/tjdn9/Documents/SuperResolution/3_blend/DataSet/ImageNet/IMG_KBS blend_imgnet/HD/tmp/blend_accumulated_599999.JPEG_0.4.png")
    compressed = cv2.imread("C:/Users/tjdn9/Documents/SuperResolution/3_blend/Results/2_SRFBN/imagenet/KBS/x3/blend_accumulated_599999.JPEG_0.4.png", 1)
    #shape = original.shape  C:\Users\tjdn9\Documents\SuperResolution\3_blend\Results\2_SRFBN\imagenet\KBS\x3
    #ori_resize = np.shape(original)
    #ori_resize = original.shape
    #compressed = cv2.resize(compressed, (3840, 2160))
    compressed = cv2.resize(compressed, (1024, 768))
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


