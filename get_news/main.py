import asyncio
import json
import os
import queue
import threading
import time
import urllib3
#自制包的导入
from tool_package.coze_solve import coze_main
from tool_package.file_colve import check_old_files,save_queue_json
from tool_package.crawl_news import crawl_entrence
from tool_package.root_logger import root_logger
from tool_package.send_solve import pushplus, news_htmlize, qiniu_push_file, get_png
#禁止报错
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#新闻队列
article_queue=queue.Queue()

if __name__ == "__main__":