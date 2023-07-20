from math import log10, sqrt
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import os

ori_folder = "C:/Users/tjdn9/Documents/SuperResolution/4_NEW/Results/SRFBN-S/x2"
compare_folder = "C:/Users/tjdn9/Documents/SuperResolution/4_NEW/Results/SRFBN-S/x3"
ori_filenames = [filename for filename in os.listdir(ori_folder) if filename.endswith(".png")]
compare_filenames = [filename for filename in os.listdir(compare_folder) if filename.endswith(".png")]

# Open and resize all images
images = []
print(ori_filenames)


# for filename in image_filenames:
#     ori_img = cv2.imread(os.path.join(ori_folder, filename), flags=cv2.IMREAD_COLOR)
#     compare_img = cv2.imread(os.path.join(compare_folder, filename), flags=cv2.IMREAD_COLOR)


def PSNR(original, compressed):
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
    for filename in ori_filenames:
        ori_img = cv2.imread(os.path.join(ori_folder, filename), flags=cv2.IMREAD_COLOR)
        ori_name ="{}/{}".format(ori_folder,filename)
        ori_img = Image.open(ori_name)
        ori_crop = ori_img.crop((0,0,390,230))
        save_name='{}/crop/{}'.format(ori_folder, filename)
        ori_crop.save(save_name)
        #cv2.imwrite(save_name, ori_crop)
        compare_img = cv2.imread(os.path.join(compare_folder, filename), flags=cv2.IMREAD_COLOR)
        compare_name = "{}/{}".format(compare_folder, filename)
        compare_img = Image.open(compare_name)
        compare_crop = compare_img.crop((0, 0, 390, 230))
        save_name = '{}/crop/{}'.format(compare_folder, filename)
        compare_crop.save(save_name)
        #cv2.imwrite(save_name, compare_crop)
    # h, w, c = compressed.shape

        # value = PSNR(ori_crop, compare_crop)
        # print(f"{filename} PSNR value is {value} dB")

    # 3. Load the two input images
    # imageA = cv2.imread("10_8blendsrcnn_x3.pth_x3.png")
    # imageB = cv2.imread("10_8blend.png")
    # 만약 url에서 불러올 거면 다음을 활용
    # imageA = io.imread(args["first"])
    # imageB = io.imread(args["second"])

    # imageC = cv2.resize(imageB, (255,255))
    # imageC = cv2.resize(imageB, (510, 510))
    # 4. Convert the images to grayscale
    # grayA = cv2.cvtColor(compressed, cv2.COLOR_BGR2GRAY)
    # grayB = cv2.cvtColor(ori_resize, cv2.COLOR_BGR2GRAY)
    #
    # # 5. Compute the Structural Similarity Index (SSIM) between the two
    # #    images, ensuring that the difference image is returned
    # (score, diff) = ssim(grayA, grayB, full=True)
    # diff = (diff * 255).astype("uint8")
    #
    # print("SSIM: {}".format(score))


if __name__ == "__main__":
    main()
