import asyncio
import json
import aiohttp
import root_logger
import queue
import os
async def run_workflow(news: str,q:queue.Queue,Authorization:str=""):
    """
    运行coze上工作流的函数
    """
    if Authorization=="":
        return 0
    url = 'https://api.coze.cn/v1/workflow/run'
    headers = {
        "Authorization": f"Bearer {Authorization}",
        "Content-Type": "application/json"
    }
    data = {
        "parameters": {
            "secret_key": "Moeus",
            "news": f"{news}"
        },
        "workflow_id": "7475598695737229346"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                root_logger.info(f"[coze]工作流状态:{result["msg"]}调试地址:{result["debug_url"]}")
                # 解析出目标内容
                process_article=json.loads(json.loads(result["data"])["result"])
                q.put(process_article)
                return (1,result['token'])
            else:
                print(f"Request failed with status code: {response.status}")
                return 0


async def coze_main(auth,q:queue.Queue):
    """
    取q队列内新闻信息创建异步任务的函数
    """

    task_list = []
    #创建异步任务
    while not q.empty():
        news = q.get()
        task = asyncio.create_task(run_workflow(news,q,Authorization=auth))  # 使用 create_task 替代 ensure_future
        task_list.append(task)

    #此时q已经空了，只需要启动异步把处理后的内容传入即可
    #异步任务开启
    results = await asyncio.gather(*task_list)  # 直接使用 await 等待所有任务
    if not 0 in results:
        root_logger.info("[coze]coze工作流处理新闻全部成功")
        sum_token = sum(map(lambda result: result[1], results))
        root_logger.info(f"[coze]总计消耗token:{sum_token}")
    else :
        root_logger.error("[coze]存在coze处理失败的任务，检查工作流或者爬取的内容")
