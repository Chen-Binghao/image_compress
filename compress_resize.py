## 图片压缩

from PIL import Image
import os

def get_size(file):
    # 获取文件大小:KB
    size = os.path.getsize(file)
    return size / 1024

def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, suffix)
    return outfile

def compress_image(infile, mb=100, outfile='', step=5, quality=90):
    """
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    """
    o_size = get_size(infile)
    if o_size <= mb:
        return infile
    outfile = get_outfile(infile, outfile)
    picture_type = str(infile)
    if os.path.splitext(infile)[-1] == ".jpg":
        print("jpg")
        while o_size > mb:
            im = Image.open(infile)
            im.save(outfile, quality=quality)

            if quality - step < 40:
                resize_image(outfile, mb, 0)
                break
            quality -= step
            o_size = get_size(outfile)
    else:
        if os.path.splitext(infile)[-1] == ".png":
            print("png")
            resize_image(infile, mb , 1)

def resize_image(infile, mb, fro, outfile=''):
    """修改图片尺寸
    :param infile: 图片源文件
    :param outfile: 重设尺寸文件保存地址
    :param x_s: 设置的宽度
    :return:
    """
    im = Image.open(infile)
    x, y = im.size
    x_s = x
    y_s = y
    step = 0.8
    o_size = get_size(infile)
    if o_size <= mb:
        return infile
    if fro == 0:
        outfile = infile
    else:
        outfile = get_outfile(infile, outfile)
    while o_size > mb:
        im = Image.open(infile)
        x_s = int(x_s * step)
        y_s = int(y_s * step)
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        outfile = get_outfile(infile, outfile)
        out.save(outfile)
        o_size = get_size(outfile)
    return outfile, get_size(outfile)
    

if __name__ == '__main__':
    compress_image(r'C:\Users\rivaille\Desktop\开业海报.jpg', 20)