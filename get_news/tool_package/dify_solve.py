import httpx
import asyncio
import json
import queue
from typing import TypedDict
from tool_package.root_logger import root_logger
class NewsItem(TypedDict):
    """
    新闻内容格式
    """
    MainText: str;
    Title: str;
    SourceTextLink:list[str];
    ImageUrl: str;
    
async def send_request(news:NewsItem,q:queue.Queue):
    url = 'http://localhost/v1/workflows/run'
    headers = {
        'Authorization': 'Bearer app-xGlX757j7oWdHoCg8G6WJsuk',
        'Content-Type': 'application/json'
    }
    data = {
        "inputs": {
            "Title": f"{news['Title']}",
            "MainText": f"{news['MainText']}",
        },
        "response_mode": "blocking",
        "user": "Moeus"
    }
    try:
        timeout = httpx.Timeout(20.0)#模型思考过程至少5秒，httpx的默认超时是5秒，需要改成20秒
        
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(url, headers=headers, json=data)
            if response.status_code == 200:
                result = response.json()
                target=json.loads(result["data"]["outputs"]["text"])
                news["Title"]=target["Title"]
                news["MainText"]=target["MainText"]
                q.put(news)
        return 1

    except httpx.HTTPStatusError as http_err:
        root_logger.error(f"[Dify]HTTP error occurred: {http_err}")
        return 0
    except Exception as err:
        root_logger.error(f"[Dify]An error occurred: {err}")
        return 0
    return None

async def dify_main(q:queue.Queue):
    root_logger.info("[Dify]开始处理数据")
    #创建异步任务列表
    tasks = []
    while not q.empty():
        news=q.get()
        task = asyncio.create_task(send_request(news,q))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
