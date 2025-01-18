import cv2
import os
from natsort import natsorted  # 用于对文件名进行自然排序


def images_to_video(image_folder, output_video, fps=30):
    """
    将指定文件夹中的图片拼接成视频。

    Args:
        image_folder (str): 包含图片的文件夹路径。
        output_video (str): 输出视频的路径（包括文件名和扩展名，如 'output.mp4'）。
        fps (int): 视频的帧率（每秒帧数）。
    """
    # 获取文件夹中的所有图片文件
    images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]

    # 确保按文件名排序（自然排序，处理文件名中带数字的情况）
    images = natsorted(images)

    # 检查是否有图片
    if not images:
        print("文件夹中没有找到图片！")
        return

    # 读取第一张图片以获取帧的宽度和高度
    first_image_path = os.path.join(image_folder, images[0])
    first_image = cv2.imread(first_image_path)
    height, width, layers = first_image.shape

    # 初始化视频写入器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用 mp4v 编码器
    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    # 遍历所有图片，将其写入视频
    for image_name in images:
        image_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(image_path)
        if frame is None:
            print(f"警告：无法读取图片 {image_path}，跳过该图片。")
            continue
        video_writer.write(frame)  # 将当前帧写入视频

    # 释放视频写入器
    video_writer.release()
    print(f"视频已保存到 {output_video}")


# 示例：将文件夹中的图片拼接成视频
image_folder = "/media/zhong/1.0T/zhong_work/CVB/000058916v001/data/raw_frames/1282_arm01_gopro3_20200326_033755_beh8_ani1_ins1_cut_00001"  # 替换为你的图片文件夹路径
output_video = "6.mp4"  # 输出视频文件名
fps = 30  # 设置视频帧率
images_to_video(image_folder, output_video, fps)