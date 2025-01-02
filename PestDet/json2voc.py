import json
import os
import glob
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

def create_voc_xml(json_folder, img_folder, output_folder):
    # 找到json目录下的所有json文件
    json_files = glob.glob(os.path.join(json_folder, '*.json'))

    for json_path in json_files:
        # 读取json文件
        with open(json_path) as f:
            data = json.load(f)

        # 获取相应的图像文件路径
        img_path = os.path.join(img_folder, os.path.basename(json_path).replace('.json', '.jpg'))

        # 创建xml根元素
        annotation = Element('annotation')

        # 添加子元素
        folder = SubElement(annotation, 'folder')
        folder.text = os.path.dirname(img_path)

        filename = SubElement(annotation, 'filename')
        filename.text = os.path.basename(img_path)

        # 假设图像尺寸已知
        size = SubElement(annotation, 'size')
        width = SubElement(size, 'width')
        width.text = str(2560)  # 替换为实际图像宽度
        height = SubElement(size, 'height')
        height.text = str(1440)  # 替换为实际图像高度
        depth = SubElement(size, 'depth')
        depth.text = str(3)

        for item in data:
            # 添加物体元素
            obj = SubElement(annotation, 'object')

            name = SubElement(obj, 'name')
            name.text = item['class_name']

            pose = SubElement(obj, 'pose')
            pose.text = 'Unspecified'

            truncated = SubElement(obj, 'truncated')
            truncated.text = '0'

            difficult = SubElement(obj, 'difficult')
            difficult.text = '0'

            bndbox = SubElement(obj, 'bndbox')

            xmin = SubElement(bndbox, 'xmin')
            xmin.text = str(item['box'][0])

            ymin = SubElement(bndbox, 'ymin')
            ymin.text = str(item['box'][1])

            xmax = SubElement(bndbox, 'xmax')
            xmax.text = str(item['box'][2])

            ymax = SubElement(bndbox, 'ymax')
            ymax.text = str(item['box'][3])

        # 保存为xml文件
        xml_str = parseString(tostring(annotation)).toprettyxml(indent="   ")
        with open(os.path.join(output_folder, os.path.basename(img_path).replace('.jpg', '.xml')), 'w') as f:
            f.write(xml_str)

# 调用函数处理整个目录
create_voc_xml('./json/', './images/', './voc/')
