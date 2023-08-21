import os
from PIL import Image
import numpy as np
import cv2

# Get all image filenames in the folder
HR_train_folder = "C:/Users/user/Desktop/Mypaper/DataSet/DIV2K_SW/train/HR/HR"
# MR_train_folder = "C:/Users/user/Desktop/Mypaper/DataSet/SU_DataSet/train/x8_aug"
LR_train_folder = "C:/Users/user/Desktop/Mypaper/DataSet/SU_DataSet/train/x16_aug"
HR_test_folder = "C:/Users/user/Desktop/Mypaper/DataSet/DIV2K_SW/val/HR/HR"
# MR_test_folder = "C:/Users/user/Desktop/Mypaper/DataSet/SU_DataSet/val/x8_aug"
LR_test_folder = "C:/Users/user/Desktop/Mypaper/DataSet/SU_DataSet/val/x16_aug"

Save_HR_train_folder = "C:/Users/user/Desktop/Mypaper/DataSet/SU_DataSet/train/HR_aug1"
# Save_MR_train_folder = "C:/Users/user/Desktop/Mypaper/DataSet/SU_DataSet/train/x8_aug1"
Save_LR_train_folder = "C:/Users/user/Desktop/Mypaper/DataSet/SU_DataSet/train/x16_aug1"
Save_HR_test_folder = "C:/Users/user/Desktop/Mypaper/DataSet/SU_DataSet/val/HR_aug1"
# Save_MR_test_folder = "C:/Users/user/Desktop/Mypaper/DataSet/SU_DataSet/val/x8_aug1"
Save_LR_test_folder = "C:/Users/user/Desktop/Mypaper/DataSet/SU_DataSet/val/x16_aug1"

LR_train_filenames = [filename for filename in os.listdir(LR_train_folder) if filename.endswith(".png")]
LR_test_filenames = [filename for filename in os.listdir(LR_test_folder) if filename.endswith(".png")]


i =1
# for filename in LR_train_filenames:
#     HR_train_img = cv2.imread(os.path.join(HR_train_folder, filename), flags=cv2.IMREAD_COLOR)
#     LR_train_img = cv2.imread(os.path.join(LR_train_folder, filename), flags=cv2.IMREAD_COLOR)
#
#     h, w = LR_train_img.shape[0], LR_train_img.shape[1]
#
#     if h>35 and w>35 :
#         save_name_HR = "{}/{}".format(Save_HR_train_folder, filename)
#         save_name_LR = "{}/{}".format(Save_LR_train_folder, filename)
#         cv2.imwrite(save_name_HR, HR_train_img)
#         cv2.imwrite(save_name_LR, LR_train_img)
for filename in LR_train_filenames:
    HR_test_img = cv2.imread(os.path.join(HR_train_folder, filename), flags=cv2.IMREAD_COLOR)
    # MR_test_img = cv2.imread(os.path.join(MR_train_folder, filename), flags=cv2.IMREAD_COLOR)
    LR_test_img = cv2.imread(os.path.join(LR_train_folder, filename), flags=cv2.IMREAD_COLOR)

    h1, w1 = LR_test_img.shape[0], LR_test_img.shape[1]
    if h1 > 60 and w1 > 60:
        b1 = int(h1 * 16)
        b2 = int(w1 * 16)

    # resized_MR = cv2.resize(MR_test_img, (a2, a1))
        resized_HR = cv2.resize(HR_test_img, (b2, b1))

        save_name_HR = "{}/{}".format(Save_HR_train_folder, filename)
    # save_name_MR = "{}/{}".format(Save_MR_train_folder, filename)
    # save_name_LR = "{}/{}".format(Save_LR_train_folder, filename)
        cv2.imwrite(save_name_HR, resized_HR)
    # cv2.imwrite(save_name_MR, MR_test_img)
    # cv2.imwrite(save_name_LR, LR_test_img)

for filename in LR_test_filenames:
    HR_test_img = cv2.imread(os.path.join(HR_test_folder, filename), flags=cv2.IMREAD_COLOR)
    # MR_test_img = cv2.imread(os.path.join(MR_test_folder, filename), flags=cv2.IMREAD_COLOR)
    LR_test_img = cv2.imread(os.path.join(LR_test_folder, filename), flags=cv2.IMREAD_COLOR)

    h1, w1 = LR_test_img.shape[0], LR_test_img.shape[1]

    if h1 > 60 and w1 > 60:
        b1 = int(h1 * 16)
        b2 = int(w1 * 16)

        # resized_MR = cv2.resize(MR_test_img, (a2, a1))
        resized_HR = cv2.resize(HR_test_img, (b2, b1))
        save_name_HR = "{}/{}".format(Save_HR_test_folder, filename)
        # save_name_MR = "{}/{}".format(Save_MR_test_folder, filename)
        # save_name_LR = "{}/{}".format(Save_LR_test_folder, filename)
        cv2.imwrite(save_name_HR, resized_HR)
        # cv2.imwrite(save_name_MR, MR_test_img)
        # cv2.imwrite(save_name_LR, LR_test_img)

    # for y in range(h):
    #     for x in range(w):
    #         if img1[y][x][0] < 224 and img1[y][x][1] < 224 and img1[y][x][2] < 224 :
    #             img[y][x] = img1[y][x]
    #img1 = cv2.imread('KBS_logo.png', flags=cv2.IMREAD_COLOR)
    #x=np.array(img)
    #new_image = cv2.addWeighted(img1, 0.5, img, 0.5, 0)
       #img[0:img1.shape[0], 0:img1.shape[1]]=img1
    #b ,g, r =cv2.split(img)
    #blend = cv2.merge((b, g, r))


    #blend2 = np.divide(blend, 2)






