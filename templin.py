from PIL import Image


class Image_Conversion:
    def __init__(self, qian, hou):
        self.qian = qian
        self.hou = hou

    def turn_img(self):  # 转化为img
        img = Image.open(self.qian)
        rgb_img = img.convert("RGB")
        rgb_img.save(self.hou)


a = 'w.webp'
b = 'w.jpg'
c = r'D:\UserData\Desktop\img'
hh = Image_Conversion(a, c+'\\'+b)
hh.turn_img()
