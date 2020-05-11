import cv2
import os
import sys
from pathlib import Path

input_path = Path('./')  # 第一个输入参数是包含视频片段的路径

frame_interval = 100  # 隔多少帧截取一帧

filenames = ['01.mp4'] # shuru de ship lujing
# Path('./01').mkdir(parents=True, exist_ok=True)
frame_path = Path('./01')

for filename in filenames:
    print("ok!")
    filepath = input_path / filename
    print(filepath)
    cap = cv2.VideoCapture(str(filepath))  # 初始化一个VideoCapture对象
    i = 0
    while(True):
        i = i + 1
        ret, frame = cap.read()
        if ret is False:
            break
        # 每隔frame_interval帧进行一次保存帧
        if (i - 1) % frame_interval == 0:
            imagename = '{}_{:0>6d}.jpg'.format(filename.split('.')[0], i)
            imagepath = str(frame_path / imagename)
            print('exported {}!'.format(imagepath))
            cv2.imwrite(imagepath, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cap.release()