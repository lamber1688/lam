import os
from PIL import Image
from pyzbar.pyzbar import decode

def decode_barcodes_in_images(image_directory):
    # 获取目录下所有图片文件
    image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]

    for image_file in image_files:
        # 打开并解码图片
        image_path = os.path.join(image_directory, image_file)
        image = Image.open(image_path)
        decoded_objects = decode(image)

        # 打印解码结果
        for obj in decoded_objects:
            print(f'在图片 {image_file} 中找到条码: {obj.data.decode("utf-8")}')

# 使用你的图片目录替换 'go'
#C:\Users\it.lamber\go
decode_barcodes_in_images('go')

