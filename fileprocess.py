import os
from PIL import Image


def is_image_file(file_path):
    try:
        # 尝试打开文件
        with Image.open(file_path) as img:
            # 如果成功打开，说明是图片文件
            return True
    except Exception as e:
        # 如果打开失败，说明不是图片文件
        return False


def get_all_files_in_folder(folder_path):
    image_files = []
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # 判断是否是文件且是图片文件
        if os.path.isfile(file_path) and is_image_file(file_path):
            image_files.append(file_path)
    return image_files


# 指定文件夹路径
def lujin(qian):
    qian = qian
    # 获取文件夹下所有文件的名称
    file_list = get_all_files_in_folder(qian)
    da_xiao = len(qian)
    return file_list, da_xiao


# 转换文件
def zhuanhuan(file_list, da_xiao, shucu, houzui):  # 图片名称 路径长度 结果路径 后缀名称
    i = 1
    for file in file_list:
        # print(file)
        img = Image.open(file)
        rgb_img = img.convert("RGB")
        name = file[da_xiao + 1:-4]
        rgb_img.save(shucu + '\\' + name + '.' + houzui)

        # 名称加后缀
        # print(file[da_xiao+1:])
        # 名称
        # print(file[da_xiao + 1:-4])

        print(str(i) + '\t' + shucu + name + '.' + houzui)
        i += 1
    print("转换结束")


# a = wenjian(r"D:\UserData\Desktop\py\图片\1")
# b = r"D:\UserData\Desktop\py\图片\2"
# print(a[1])
# zhuanhuan(a[0], a[1], b)


# 删除文件
def shanchu(hhh, hou):
    i = 1
    for f in hhh:
        houzui = f.split('.')[-1]
        # print(houzui)
        if houzui == hou:
            os.remove(f[:])
            print(str(i) + '\t' + f[:])
            i += 1
    print("删除结束")


# a = r"D:\UserData\Desktop\py\图片\2"
#
# b = lujin(a)
# print(b)
# shanchu(b[0],"jpg")

# filename = "jdfygkrewiuty.fdsty8ewrf87.1248907.png"
# print(filename.split('.')[-1])
def rename_files_to_numbers(folder_path, start_number):
    # 批量修改文件名称为数字
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)

    # 遍历文件夹中的每个文件
    for index, filename in enumerate(files, start=start_number):
        # 构建文件的完整路径
        old_filepath = os.path.join(folder_path, filename)

        # 检查文件是否是文件而不是子文件夹
        if os.path.isfile(old_filepath):
            # 获取文件扩展名（如 .txt）
            file_extension = os.path.splitext(filename)[1]

            # 构建新的文件名
            new_filename = f"{index}{file_extension}"
            # 构建新文件的完整路径
            new_filepath = os.path.join(folder_path, new_filename)
            print("修改中" + new_filepath)
            # 重命名文件
            os.rename(old_filepath, new_filepath)
    print("修改成功")
# a = "D:/UserData/Desktop/img/shuchu"
# b=100
# rename_files_to_numbers(a,b)
