from PIL import Image
import os
data_dir='data\玫瑰'
for fname in os.listdir(data_dir):
    
    try:
        fpath = os.path.join(data_dir, fname)
        image = Image.open(fpath)
        image = Image.open(fpath)
        imagePixmap = image.size	# 宽高像素
        print(imagePixmap)
    except IOError:
        os.remove(fpath)
        print("删除保存")


