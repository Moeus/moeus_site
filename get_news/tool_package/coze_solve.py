import asyncio
import httpx
# from tool_package.root_logger import root_logger
import queue
from typing import TypedDict
class NewsItem(TypedDict):
    """
    新闻内容格式
    """
    MainText: str;
    Title: str;
    SourceTextLink:list[str];
    ImageUrl: str;

async def run_workflow(news:NewsItem):
    """
    运行coze上工作流的函数
    """
    try:
        for_send={
            "Title":news["Title"],
            "MainText":news["MainText"]}
    except Exception as e:
        print(news)
    url = 'https://api.coze.cn/v1/workflow/stream_run'
    headers = {
        "Authorization": "Bearer pat_bY68tbgW5pjSrUlA8KsS0QLWbEsquSLzA3hUrvyGFfr11Fs2BNVaaOnF92GeGqAR",
        "Content-Type": "application/json"
    }
    data = {
        "parameters": {
            "secret_key": "",
            "news": ""
        },
        "workflow_id": "7475598695737229346"
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)
            response.raise_for_status()
            print(response.text)
            return response.json()
    except httpx.HTTPStatusError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None


async def coze_main(q:queue.Queue,auth="pat_bY68tbgW5pjSrUlA8KsS0QLWbEsquSLzA3hUrvyGFfr11Fs2BNVaaOnF92GeGqAR"):
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
    # if not 0 in results:
    #     root_logger.info("[coze]coze工作流处理新闻全部成功")
    #     sum_token = sum(map(lambda result: result[1], results))
    #     root_logger.info(f"[coze]总计消耗token:{sum_token}")
    # else :
    #     root_logger.error("[coze]存在coze处理失败的任务，检查工作流或者爬取的内容")


if __name__=="__main__":
    newss={'SourceTextLink': ['来源于[澎湃新闻]点击查看原文', 'https://www.thepaper.cn/newsDetail_forward_30727268'], 'Title': '“梅花奖”快闪上海张园，朱洁静石库门前起舞', 'MainText': '周末的上海张园，春和景明，人流如织。各色潮店中，不时有身着传统戏服的演员吸引游人目光。拍照打卡，热闹非常。当舞蹈演员朱洁静手持梅花，翩然起舞，所有人举起手中相机手机，定格下眼前瞬间。朱洁静在张园舞蹈4月26日，第十届中国戏剧奖·梅花表演奖（第32届中国戏剧梅花奖） “梅花绽放在上海”活动第一站，就走入“海上第一名园”张园。来自全国的本届梅花奖参评演员，带着各色精致行头来到这里。细致装扮，轮番登场，无论是张园的石库门建筑，还是街头的明媚阳光下，都留下他们走秀打卡的身影。本次活动是第十届中国戏剧奖·梅花表演奖（第32届中国戏剧梅花奖）终评活动的系列配套活动的首场重头戏，戏剧艺术的独特魅力与张园极具海派风情的石库门里弄建筑交相辉映，吸引更多市民游客沉浸式了解梅花奖，快闪活动现场活动以快闪限定展、走秀表演、沉浸式体验为主要形式。当天，张园西区W7栋化身戏剧艺术展馆，现场LED大屏持续滚动播放本届梅花奖终评剧目的精彩片段与演员风采；海报展陈区集中呈现17场终评剧目的海报；文创市集汇聚了不同剧种的独特文创产品及宣传册；拍照打卡区的“梅”韵主题展板和可爱的戏曲人物形象，则让演员们也忍不住上前打卡留念。现场不仅有热心戏迷报名参与互动，还有外国友人加入了扮上戏装的现场体验。当天，朱洁静率先登场亮相。演员蓝天、刘李优优、鲍陈热、季春艳、尹春媛、周帆，特邀嘉宾“二度梅”得主华雯与第31届梅花奖获得者罗晨雪，兜兜身着华美戏服或现代装，依次从二楼阳台亮相，随后在一楼表演区域现场演唱，与观众近距离互动。快闪活动现场鲍陈热带来的台州乱弹折子戏《活捉三郎》、周帆的湘剧《夫人如见》、尹春媛献上古老剧种柳子戏的《玩会跳船》、季春艳带来的锡剧《玲珑女》，都向上海观众展示了各自剧种的独特魅力。而话剧演员刘李优优的参评剧目虽是话剧《主角》，但多才多艺的她在快闪中则现场演奏了一曲钢琴。虽然只有短短几分钟的亮相，但演员们都准备充足，不仅带来了精美的戏服，而且画上了和正式演出一样完整精致的妆容，每位演员都进行了两三个小时的化妆准备工作。快闪活动现场上海演员蓝天以观众耳熟能详的经典现代京剧《智取威虎山》登场，赢得了现场尤其热烈的喝彩。他表示，这场活动也是“竞梅”前的一次预热。“正好有机会看看其他演员的艺术特点，也熟悉下其他梅花奖选手的风格。”蓝天笑称，趁着快闪活动，既是和观众交流，也是和其他梅花奖演员的一次交流。朱洁静则说，在4月的上海，在张园随性起舞，会让自己觉得很松弛，也很真实。“在这里我就和大家一样，游走在张园，感受着上海的风貌，然后有微风，让我觉得上海很美。”“梅花香自苦寒来，这朵梅花对我来说意义很重要。”谈及在上海主场竞梅，朱洁静感受到，一切活动和安排都很丰富，“从舞台上走下来，走到生活当中，身边处处可以是舞台”。她透露，除了快闪，下午还要去针对上海中小学的直播，有很多艺术家的导赏。“我会觉得，梅花奖不再是那么曲高和寡，高高挂在殿堂，而是这样一个业内非常权威的展演和评奖，也可以让它落地，接地气，可以在生活当中绽放。老百姓可以在家门口，就能够欣赏到全国这么多优秀的作品和艺术家。”快闪活动吸引了大量市民群众往届上海的梅花奖得主也来到现场。二度摘得梅花奖的沪剧表演艺术家华雯为大家演唱了沪剧《芦荡火种》，曾获第31届中国戏剧梅花奖的上海昆剧团青年艺术家罗晨雪带来了昆曲《牡丹亭·游园》选段。华雯感慨，“梅花奖陪伴我走过了30年的舞台生涯，作为一个上海籍的梅花奖获奖者，能够在自己的家门口，能够在自己的城市里面，进行一个梅花奖的这样的盛会，我是非常感慨和激动的。”在华雯印象中，之前的梅花奖还没有快闪这样的形式来和观众交流，“我觉得用梅花奖比赛这样一个载体，其实宣传的是我们上海的文化、上海的人文、上海的城市，甚至是上海的街道，尤其是像今天这样接地气的方式与市民群众交流，我觉得非常了不起。”2025年5月8日至21日，由中国文联、中国剧协、中共上海市委宣传部联合主办的第十届中国戏剧奖·梅花表演奖（第32届中国戏剧梅花奖）终评活动将在上海隆重举办。快闪活动现场此次“梅花竞放 戏聚东方”快闪活动在张园首场之后，第二场将于4月27日在上海地铁人民广场音乐角举办；第三场将于5月2日在陆家嘴中心LG层下沉广场（浦东南路899号）收官。本届梅花奖参评演员鲍陈热、袁国良、李哲、黄瑞妮等及上海地区曾获得梅花奖的华雯、蔡金萍、赵志刚、安平、黎安、金喜全、沈昳丽、熊明霞、罗晨雪等艺术家还将联袂亮相演出，“梅花”的芬芳，将以全新的方式浸润这座城市。', 'ImageUrl': 'https://imgpai.thepaper.cn/newpai/image/1745659776000_cfNRdy_1745671375942.jpg?x-oss-process=image/resize,w_1024'}
    asyncio.run(run_workflow(newss))