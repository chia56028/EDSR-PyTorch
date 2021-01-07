
import os
import cv2

input_dir = './hw4/training_hr_images/training_hr_images/'
scale = 3
output_dir = './DIV2K/DIV2K_train_LR_bicubic/X'+str(scale)+'/'
if not os.path.isdir('./DIV2K/DIV2K_train_HR/'):
    os.makedirs('./DIV2K/DIV2K_train_HR/')
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)
    
imgNames = os.listdir(input_dir)
# print(imgNames)
k = 1
for imgName in imgNames:
    pic = cv2.imread(input_dir+imgName)
    newName = str(k).rjust(4,'0')+'.png'
    cv2.imwrite('./DIV2K/DIV2K_train_HR/'+newName, pic)
    h, w, c = pic.shape
    pic = cv2.resize(pic, (int(w/scale), int(h/scale)), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(output_dir+newName.replace('.png','')+'x'+str(scale)+'.png', pic)
    k += 1

# cv2.imshow('', pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
