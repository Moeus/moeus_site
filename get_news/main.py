import asyncio
import json
import os
import queue
import random
import urllib3
import requests
import hashlib
import subprocess
#自制包的导入
from tool_package.dify_solve import dify_main
from tool_package.crawl_news import crawl_entrence
from tool_package.root_logger import root_logger
#禁止报错
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#新闻队列
news_queue=queue.Queue()



def download_image(image_url, Title, save_dir="./src/public"):
    file_name = hashlib.md5(Title.encode()).hexdigest()  # 使用标题的 MD5 哈希作为文件名
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
        return file_name
    except Exception as e:
        print(f"Failed to download image from {image_url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def write_to_vue(news_list):
    # 定义要处理的文件路径
    file_path = r'./docs\.vitepress\theme\components\NewsCard.vue'
    for i in range(len(news_list)):
        news_list[i]=str(news_list[i])
    # 定义要追加的新内容
    new_content =",".join(news_list)
    new_content+='\n'

    try:
        # 以只读模式打开文件
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        start_index = None
        end_index = None
        # 查找起始和结束标识符的索引
        for i, line in enumerate(lines):
            if line.strip() == '//(@#':
                if start_index is None:
                    start_index = i
                else:
                    end_index = i
                    break

        if start_index is not None and end_index is not None:
            # 删除标识符之间的内容
            del lines[start_index + 1:end_index]
            # 在标识符之间插入新内容
            lines.insert(start_index + 1, new_content)

        # 以写入模式打开文件，将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

        print("文件修改完成。")
    except FileNotFoundError:
        print(f"未找到文件: {file_path}")
    except Exception as e:
        print(f"发生错误: {e}")



def git_push(repo_path=os.path.dirname(os.path.dirname(__file__)), remote='origin', branch='master'):
    try:
        # 切换到仓库目录
        subprocess.run(['git', '-C', repo_path, 'add', '.'], check=True)
        # 提交更改
        subprocess.run(['git', '-C', repo_path, 'commit', '-m', 'python爬虫获取新闻自动提交'], check=True)
        # 推送到远程仓库
        subprocess.run(['git', '-C', repo_path, 'push', remote, branch], check=True)
        print("成功推送到远程仓库。")
    except subprocess.CalledProcessError as e:
        print(f"推送过程中出现错误: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(script_dir)
    crawl_entrence(script_dir=script_dir, news_queue=news_queue)
    #使用字典记录每个分类下的新闻的列表
    news_type_dict={}
    while not news_queue.empty():
        news=news_queue.get()
        if news["SourceTextLink"][0] in news_type_dict.keys():
            news_type_dict[news["SourceTextLink"][0]].append(news)
        else:
            news_type_dict[news["SourceTextLink"][0]]=[news]
    #对每个类别进行随机取样
    news_list=[]
    for key in news_type_dict.keys():
        if len(news_type_dict[key])>=2:
            choose=random.sample(news_type_dict[key],2)
            news_list.extend(choose)#不需要解包
        else:
            choose=news_type_dict[key][0]
            news_list.append(choose)      
    del news_type_dict
    #放回队列
    for news in news_list:
        news_queue.put(news)
    #异步处理文本内容
    asyncio.run(dify_main(news_queue))
    news_list=[]
    while not news_queue.empty():
        news=news_queue.get()
        news_list.append(news)
    for news in news_list:
        news["ImageUrl"]=download_image(news["ImageUrl"],news["Title"])
    write_to_vue(news_list)    
    with open(os.path.join(script_dir,"res.json"), 'w',encoding="utf-8") as file:
        # 将列表写入 JSON 文件
        json.dump(news_list, file, ensure_ascii=False, indent=4)
    root_logger.info("[Dify]数据处理完成，结果已保存到res.json文件中")
    git_push()