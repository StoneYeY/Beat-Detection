# -*- coding: utf-8 -*-

import sys
import os
import time
import random
import traceback


DATASET_PATH = "/dataset"
OUTPUT_PATH = "/output"


# 遍历文件夹，获得文件列表
def scan_file(list_file, file_path):
    try:
        for filename in os.listdir(file_path):
            abs_path = file_path + "/" + filename
            if os.path.isdir(abs_path):
                    scan_file(list_file, abs_path)
            elif os.path.isfile(abs_path):
                list_file.append(abs_path)
                print(abs_path)
    except:
        traceback.print_exc()
    
    
# 将数据写入文件
def write_data(file):
    fp = open(file, 'w')
    for i in range(0, random.randint(10,30)):
        fp.write(str(i) + "." + str(random.randint(1,999)) + "\n")
    fp.close()
    print(file)
    
    
# 预测函数，根据自己的算法自行实现，Demo中为随机生成结果
def predict(file, filename):
    # 输出beat数据
    s_output_beat = OUTPUT_PATH + "/" + filename + ".beat"
    write_data(s_output_beat)
    
    # 输出downbeat数据
    s_output_downbeat = OUTPUT_PATH + "/" + filename + ".downbeat"
    write_data(s_output_downbeat)
    
    return 0


if __name__ == "__main__":
    print("this is python pro")
    
    # 扫描获得待预测的 wav 文件列表
    list_file = []
    scan_file(list_file, DATASET_PATH)
        
    # 遍历待预测的 wav 文件列表，执行结果预测
    for file in list_file:
        path, fullname = os.path.split(file)
        filename, ext = os.path.splitext(fullname)

        # 对 wav 文件进行预测
        if os.path.splitext(file)[1].lower() == ".wav":
            predict(file, filename)
