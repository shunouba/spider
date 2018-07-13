import tesserocr
from PIL import Image


# 此种识别效果不如下一种好
# print(tesserocr.file_to_text('CheckCode.jpeg'))


# 直接处理
# image = Image.open('CheckCode.jpeg')
# result = tesserocr.image_to_text(image)
# print(result)


# 灰度处理
# 将图片转换为灰度图像，即黑白图像
# image = image.convert('L')
# image.show()


# 二值化处理
# 采用默认阈值127
# image = image.convert('1')
# image.show()

# 指定二值化的阈值，此时要先将原图转换为灰度图像
image = Image.open('CheckCode.jpeg')
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    # if i < threshold:
    #     table.append(0)
    # else:
    #     table.append(1)

    # 模拟其他语言的？表达式，将if else 浓缩为一行代码
    table.append(0) if i < threshold else table.append(1)
image = image.point(table, '1')
image.show()
result = tesserocr.image_to_text(image)
print(result)
