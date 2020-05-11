"""
    将labelme 生成的标注数据进行合并
"""
import json
import shutil
from pycocotools.coco import COCO
from pathlib import Path


img_files_path = ['./01/car_light_img', './02/normal_img', './03/human_img']
json_files_path = ['./01/car_light_json', './02/normal_json', './03/human_json']

jpeg_file_dir = './JPEGImgs'
json_file_dir = './JSON'

def process_json(input_json_file, output_json_file, change_file_name_path):
    file_in = open(input_json_file, "r")
    file_out = open(output_json_file, "w")
    # load数据到变量json_data
    json_data = json.load(file_in)
    print(json_data["imagePath"], "after update  --->" ,change_file_name_path)
    json_data["imagePath"] = change_file_name_path
    # 将修改后的数据写回文件
    file_out.write(json.dumps(json_data))
    file_in.close()
    file_out.close()


def copy_img_file(img_file, to_file):
    print('copy:', img_file, 'to -> ', to_file)
    shutil.copy(str(img_file), str(to_file))
    return True


def copy_json(input_json_file, output_json_file, change_file_name_path):
    file_in = open(input_json_file, "r")
    file_out = open(output_json_file, "w")
    # load数据到变量json_data
    json_data = json.load(file_in)
    print(json_data["imagePath"], "after update  --->", change_file_name_path)
    json_data["imagePath"] = change_file_name_path
    # 将修改后的数据写回文件
    file_out.write(json.dumps(json_data))
    file_in.close()
    file_out.close()

for i in range(len(img_files_path)):
    img_file_dir = img_files_path[i]
    json_files_dir = json_files_path[i]
    img_file_list = list(Path(img_files_path[i]).glob('*.jpg'))
    # print(img_file_list)
    json_file_list = list(Path(json_files_path[i]).glob('*.json'))
    # print(json_file_list)

    for json_path in json_file_list:
        img_name = ""
        with open(str(json_path), 'r') as load_f:
            car_light_json = json.load(load_f)
            img_name = str(
                Path(
                    car_light_json['imagePath']
                ).name
            )

        json_name = json_path.name
        new_json_name = str(i) + '_' + str(json_name)
        new_img_name = str(i) + '_' + str(img_name)

        # copy image file
        result = copy_img_file(str(Path(img_files_path[i]) / img_name),
                               str(Path(jpeg_file_dir) / new_img_name))
        if not result:
            break
        # copy json file
        copy_json(
            str(Path(json_files_path[i]) / json_name),
            str(Path(json_file_dir) / new_json_name),
            str(Path(jpeg_file_dir) / new_img_name)
        )

