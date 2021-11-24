# HW2-SVHN-Detection

## Introduction
The Homework2 for NYCU CS Selected Topics in Visual Recognition using Deep Learning. In this homework, we use Google dataset **Streets View House Number(SVHN) format1**  to identify the house number on the street. This dataset contains 33,402 training images, 13,068 test images.

I used Keras and YOLO3 to implement this project. Before training, I convert SVHN Dataset to PASCAL VOC Format, and then convert it to my own data format. After training, it will generate result meet the [COCO result](https://cocodataset.org/#format-results).

## Bench Mark
Please click [here](https://colab.research.google.com/drive/1wQXYzRpMPIPyA7vzpSkLRgAqhk9FWnB1?usp=sharing).

## Environment
- Ubuntu 20.04
- Python 3.6.9
- GeForce GTX 1080Ti
- Cuda 10.1

## Project Structure
```
Root/
    dataset
    ├── train
    |   ├── data
    |   |   ├── 1.png
    |   |   ├── 10.png
    |   |   ├── ...
    |   ├── annotation
    |   |   ├── 1.xml
    |   |   ├── 10.xml
    |   |   ├── ...
    ├── test
    |   ├── 1.png
    |   ├── 2.png
    |   ├── ...
    font
    ├── FiraMono-Medium.otf
    ├── SIL Open Font License.txt
    model_data
    ├── svhn_classes.txt
    ├── yolo_anchors.txt
    yolo3
    ├── model.py
    ├── utils.py
    convert.py
    LICENSE
    parse_matFile.py
    README.md
    requirements.txt
    yolo_video.py
    yolo.py
    yolov3.cfg
    yolov3.weights
    voc_annotation.py


```

## Reproducing_submission
To reproducing my submission, please follow the step below:
1. Download the test dataset(format1) from [SVHN](http://ufldl.stanford.edu/housenumbers/), and then move all images to directory **dataset/test**.
2. Download model from [here](https://drive.google.com/file/d/1NWA574VSHuws7JbeXZKNyX5Hy5mdeKVe/view?usp=sharing) and put model to folder **model_data**.
3. Open inference.ipynb, and run all cells.
4. The submission.zip will be generated.

## Training
In this part, I am used pre-trained model **yolov3.weights**
To start training, please follow the steps below:
1. Download train dataset(format1) from [SVHN](http://ufldl.stanford.edu/housenumbers/), and move **digitStruct.mat** file and all images to the directory **dataset/train/data**.
2. Download the pre-trained model.
```
wget https://pjreddie.com/media/files/yolov3.weights
```
3. Run the following command to produce PASCAL VOC Annotation Format.
```
$ python3 parse_matFile.py
```
If got the error like "TypeError: 'NoneType' object is not subscriptable", then run the above command again.

4. Run the following command to generate txt file which contains image path and label.
```
$ python voc_annotation.py
```
5. Run the following command to generate th pre-trained weight from **yolov3.weights**
```
python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5
```
6. Open train.ipynb, and run all cell.
7. The best model weight will be generated in **logs/svhn_weights**.
8. Open **inference.py** and replace **config** variable as follow:
```
config = {
    "model_path": "logs/svhn_weights/{your_model_file_name}"
}
```
9. [Start making inference](#Reproducing_submission)

## Reference
1. https://github.com/qqwweee/keras-yolo3
2. https://keras.io/api/models/
3. https://github.com/Yunyung/Object-Detector-on-SVHN-Datasets
4. http://pjreddie.com/darknet/yolo/
5. https://github.com/yan-roo/Digit-Detector-YOLOv3
