import os
from PIL import Image


def get_all_files_in_folder(folder_path):
    files = []
    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            # 获取文件的完整路径
            file_path = os.path.join(root, filename)
            files.append(file_path)
    return files


# 指定文件夹路径
def lujin(qian):
    qian = qian
    # 获取文件夹下所有文件的名称
    file_list = get_all_files_in_folder(qian)
    da_xiao = len(qian)
    return file_list, da_xiao


# 转换文件
def zhuanhuan(file_list, da_xiao, shucu, houzui):
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
