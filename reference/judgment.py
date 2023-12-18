from PIL import Image
import os


def is_image_file(file_path):
    try:
        # 尝试打开文件
        with Image.open(file_path) as img:
            # 如果成功打开，说明是图片文件
            return True
    except Exception as e:
        # 如果打开失败，说明不是图片文件
        return False


def get_image_files(folder_path):
    image_files = []
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # 判断是否是文件且是图片文件
        if os.path.isfile(file_path) and is_image_file(file_path):
            image_files.append(file_path)
    return image_files


# 替换为你的文件夹路径
# folder_path = r'D:\UserData\Desktop\img\shuchu'
# image_files = get_image_files(folder_path)

# 打印所有图片文件的路径
# for image_file in image_files:
#     print(image_file)
