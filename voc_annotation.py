import xml.etree.ElementTree as ET
import os
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["10","1","2","3","4","5","6","7","8","9"]


def convert_annotation(image_id, list_file):
    in_file = open(label_path + '/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()


list_file = open('train.txt', 'w')
train_path = 'dataset/train/data'
label_path = 'dataset/train/annotation'

total_files_counts = len(os.listdir(train_path))
not_png = []
for image_id in os.listdir(train_path):
    if image_id.endswith('.png'):
        image_id = image_id[:-4]
        list_file.write(train_path + '/%s.png'%(image_id))
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    else:
        not_png.append(image_id)
print(not_png)
list_file.close()



