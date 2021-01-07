Image Super Resolution
===
Super resolution (SR) is the process of taking an input of a low resolution (LR) and upscaling it to that of a high resolution.
This program is the implementation of the paper *[Enhanced Deep Residual Networks for Single Image Super-Resolution](https://openaccess.thecvf.com/content_cvpr_2017_workshops/w12/papers/Lim_Enhanced_Deep_Residual_CVPR_2017_paper.pdf)* by Bee Lim, Sanghyun Son, Heewon Kim, Seungjun Nah, and Kyoung Mu Lee.

### Hardware
- Intel(R) Core(TM) i5-9600K CPU @ 3.70GHz
- NVIDIA GeForce RTX 2080 Ti

### Environment
- Microsoft win10
- Python 3.7.3
- Pytorch 1.7.0
- CUDA 10.2

### Install Packages
- install pytorch from https://pytorch.org/get-started/locally/
- install dependencies
```
pip install -r requirements.txt
```

### Data Preparation
Download the given dataset from [Google Drive](https://drive.google.com/drive/u/3/folders/1H-sIY7zj42Fex1ZjxxSC3PV1pK4Mij6x) and put it into `src` folder. Then run `python convert.py` to generate the corresponding images and folders.
```
src
├── DIV2K
│   ├── DIV2K_train_HR
│   └── DIV2K_train_LR_bicubic
│       ├── X2
│       └── X3
└── hw4
    ├── testing_lr_images
    └── training_hr_images
```
### Training
Execute following instruction to train the model:
```
python main.py --model EDSR --scale 3 --patch_size 30 --save edsr_baseline_x3 --reset --dir_data . --lr 0.00005
```
※ get more info by `python main.py -h`

### Testing
Execute following instruction to test images:
```
python main.py --data_test Demo --dir_demo ./hw4/testing_lr_images/testing_lr_images --scale 3 --pre_train ../experiment/edsr_baseline_x3/model/model_best.pt --test_only --save_results --save HW4_result
```
