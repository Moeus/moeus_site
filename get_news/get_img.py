import requests
import os

def download_image(image_url, file_name, save_dir="./src/public"):
    try:
        # 发送 GET 请求获取图片
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        #从响应头中获取类型
        content_type = response.headers.get('Content-Type')
        if content_type == 'image/jpeg':
            file_extension = '.jpg'
        elif content_type == 'image/png':
            file_extension = '.png'
        else:
            file_extension = '.jpg'
        file_name += file_extension  # 添加文件扩展名

        # 保存图片到指定路径
        with open(os.path.join(save_dir,file_name), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    except Exception as e:
        print(f"Failed to download image from {image_url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")