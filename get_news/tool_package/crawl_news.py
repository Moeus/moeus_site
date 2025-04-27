"""
主文件
爬虫 今日头条，微博，知乎日报
coze异步调用工作流api对新闻内容做处理
生成html字符串
保存队列信息到res文件夹
检查res文件夹，清除旧文件
"""
import os.path
from DrissionPage import WebPage
#多条件定位下使用"tag():a"  而不是tag:a
from DrissionPage import ChromiumOptions,SessionOptions
import time
import re
from root_logger import root_logger
import random
import queue
from typing import TypedDict
#全局浏览器配置
co=ChromiumOptions()
co.set_load_mode("eager")#html的Dom加载完毕就开始爬，因为爬的是文字，所以可以这样设置
co.set_argument('--autoplay-policy','no-user-gesture-required')#禁用视频播放
# co.no_imgs()#禁用图片加载
# co.no_js()#禁用js加载
co.set_local_port(9222)
co.set_argument("--remote-debugging-port","9222")
# co.set_user_data_path(r"C:\Users\26627\AppData\Local\Google\Chrome\User Data")
#无头模式
# co.headless()
co.auto_port()
so=SessionOptions()
#今日头条cookies
# so.set_cookies(cookies="__ac_signature=_02B4Z6wo00f01cANIsgAAIDBHJLMKqKmu5HALSZAABfL13; tt_webid=7479022789643683378; ttcid=728594bcd125422692aefadda34bb85831; csrftoken=428aac1521442651429d59222d7665f6; s_v_web_id=verify_m7yo9x5b_dkdZmngR_5FJz_4VLV_9FnX_oeGt3K5E1Nc4; WIN_WH=1442_740; PIXIEL_RATIO=1.25; FRM=new; gfkadpd=24,6457; local_city_cache=%E5%B4%87%E5%B7%A6; passport_csrf_token=2513d5840448b8692bee9fa9245bafba; passport_csrf_token_default=2513d5840448b8692bee9fa9245bafba; passport_mfa_token=Cjd8me7u9CrWWpC7xBRqq8rbnuFnFYzffty6DZoSoszTmxzZraj7b0pFwsGF4B6LoEjTMFaQo21GGkoKPDxlynDtOSV3tuOkCor2oJ6zLlv%2BaeXtchOnLreXivZnQiICS3tASXN1x9fYSJslC%2BRc8wa87Tc%2BD9errhCi7u8NGPax0WwgAiIBA8f47uE%3D; d_ticket=faf5eeb752be9732671f0eb9da42a897ee11d; n_mh=TWl_HFIp4ubsNBbCD2NZH9xjy8ImSLER1LVADSGawRE; sso_auth_status=3cda001ece5310cd5f1443efa4eb0841; sso_auth_status_ss=3cda001ece5310cd5f1443efa4eb0841; sso_uid_tt=a956d493790edfab9beb920065bf8ec0; sso_uid_tt_ss=a956d493790edfab9beb920065bf8ec0; toutiao_sso_user=412c63179541c96a5ec599737e08fec3; toutiao_sso_user_ss=412c63179541c96a5ec599737e08fec3; sid_ucp_sso_v1=1.0.0-KDIxNDJlZjUyMTllODdhY2YxMzI4ZDExY2IzOTFiODNlNmFmNDYxMGUKHgiDvLCggc2CARCxhLjABhgYIAwwvYCFrAY4AkDxBxoCaGwiIDQxMmM2MzE3OTU0MWM5NmE1ZWM1OTk3MzdlMDhmZWMz; ssid_ucp_sso_v1=1.0.0-KDIxNDJlZjUyMTllODdhY2YxMzI4ZDExY2IzOTFiODNlNmFmNDYxMGUKHgiDvLCggc2CARCxhLjABhgYIAwwvYCFrAY4AkDxBxoCaGwiIDQxMmM2MzE3OTU0MWM5NmE1ZWM1OTk3MzdlMDhmZWMz; passport_auth_status=c708a69bd115233a0517c78f30195b6c%2C2debbadad6c27cca5a180beea59869d3; passport_auth_status_ss=c708a69bd115233a0517c78f30195b6c%2C2debbadad6c27cca5a180beea59869d3; sid_guard=f8b2a6bcd2d9867ca40913cc0641c9b3%7C1745748529%7C5184002%7CThu%2C+26-Jun-2025+10%3A08%3A51+GMT; uid_tt=9d074cfe20617892f953da297a334d03; uid_tt_ss=9d074cfe20617892f953da297a334d03; sid_tt=f8b2a6bcd2d9867ca40913cc0641c9b3; sessionid=f8b2a6bcd2d9867ca40913cc0641c9b3; sessionid_ss=f8b2a6bcd2d9867ca40913cc0641c9b3; is_staff_user=false; sid_ucp_v1=1.0.0-KDdlNjA2ODlhNWVkMTM1NDhiZmZhYmE2OGY3YjE0ZjhkOTg1NTQ3NWEKGAiDvLCggc2CARCxhLjABhgYIAw4AkDxBxoCbGYiIGY4YjJhNmJjZDJkOTg2N2NhNDA5MTNjYzA2NDFjOWIz; ssid_ucp_v1=1.0.0-KDdlNjA2ODlhNWVkMTM1NDhiZmZhYmE2OGY3YjE0ZjhkOTg1NTQ3NWEKGAiDvLCggc2CARCxhLjABhgYIAw4AkDxBxoCbGYiIGY4YjJhNmJjZDJkOTg2N2NhNDA5MTNjYzA2NDFjOWIz; ttwid=1%7C_libU-z56BlqzEc2lcd_bAR1Sb7sMz_s4cY9f6Hig6o%7C1745748531%7Cf123820223e5bbdee19bb3a497f5935a93d972739eee567d6f8ab06b2f9f8fec; tt_anti_token=l2sVNtXId-9101d18468465138e1d16cfca287de872acc602544628a35acd16c9cbbe5491f; tt_scid=PUkXaGMM.-PROP37r5vrcQ8I4hNqCxHP4iDnAy7Aw.ANjv2Hc68KbjmxGTxWUL4Xa1a4; odin_tt=be26fae28cc323f95bde97b5f38312b4257f272a22986519a54d111aed0ea710245e54c42dfa8766b413c6bed29aa034")
#全局爬取文章配置
"""
NewsItem {
  "MainText": string;
  "Title": string;
  "SourceTextLink":string[];// [text, link]
  "ImageUrl": string;
}
"""
class NewsItem(TypedDict):
    """
    新闻内容格式
    """
    MainText: str;
    Title: str;
    SourceTextLink:list[str];
    ImageUrl: str;

def get_toutiao(webpage:WebPage,news_queue:queue.Queue):
    """
    今日头条热榜上的链接可能是trendeing类也可能是article类，trending类没办法抓取，trending类找到的article类可以抓取
    获取今日头条上的今日热点内容
    """

    url="https://www.toutiao.com"
    #主tab
    main_tab=webpage.new_tab(url=url)#返回mixtab对象
    main_tab.get(url)
    main_tab.set.cookies("__ac_signature=_02B4Z6wo00f01cANIsgAAIDBHJLMKqKmu5HALSZAABfL13; tt_webid=7479022789643683378; ttcid=728594bcd125422692aefadda34bb85831; csrftoken=428aac1521442651429d59222d7665f6; s_v_web_id=verify_m7yo9x5b_dkdZmngR_5FJz_4VLV_9FnX_oeGt3K5E1Nc4; WIN_WH=1442_740; PIXIEL_RATIO=1.25; FRM=new; gfkadpd=24,6457; local_city_cache=%E5%B4%87%E5%B7%A6; passport_csrf_token=2513d5840448b8692bee9fa9245bafba; passport_csrf_token_default=2513d5840448b8692bee9fa9245bafba; passport_mfa_token=Cjd8me7u9CrWWpC7xBRqq8rbnuFnFYzffty6DZoSoszTmxzZraj7b0pFwsGF4B6LoEjTMFaQo21GGkoKPDxlynDtOSV3tuOkCor2oJ6zLlv%2BaeXtchOnLreXivZnQiICS3tASXN1x9fYSJslC%2BRc8wa87Tc%2BD9errhCi7u8NGPax0WwgAiIBA8f47uE%3D; d_ticket=faf5eeb752be9732671f0eb9da42a897ee11d; n_mh=TWl_HFIp4ubsNBbCD2NZH9xjy8ImSLER1LVADSGawRE; sso_auth_status=3cda001ece5310cd5f1443efa4eb0841; sso_auth_status_ss=3cda001ece5310cd5f1443efa4eb0841; sso_uid_tt=a956d493790edfab9beb920065bf8ec0; sso_uid_tt_ss=a956d493790edfab9beb920065bf8ec0; toutiao_sso_user=412c63179541c96a5ec599737e08fec3; toutiao_sso_user_ss=412c63179541c96a5ec599737e08fec3; sid_ucp_sso_v1=1.0.0-KDIxNDJlZjUyMTllODdhY2YxMzI4ZDExY2IzOTFiODNlNmFmNDYxMGUKHgiDvLCggc2CARCxhLjABhgYIAwwvYCFrAY4AkDxBxoCaGwiIDQxMmM2MzE3OTU0MWM5NmE1ZWM1OTk3MzdlMDhmZWMz; ssid_ucp_sso_v1=1.0.0-KDIxNDJlZjUyMTllODdhY2YxMzI4ZDExY2IzOTFiODNlNmFmNDYxMGUKHgiDvLCggc2CARCxhLjABhgYIAwwvYCFrAY4AkDxBxoCaGwiIDQxMmM2MzE3OTU0MWM5NmE1ZWM1OTk3MzdlMDhmZWMz; passport_auth_status=c708a69bd115233a0517c78f30195b6c%2C2debbadad6c27cca5a180beea59869d3; passport_auth_status_ss=c708a69bd115233a0517c78f30195b6c%2C2debbadad6c27cca5a180beea59869d3; sid_guard=f8b2a6bcd2d9867ca40913cc0641c9b3%7C1745748529%7C5184002%7CThu%2C+26-Jun-2025+10%3A08%3A51+GMT; uid_tt=9d074cfe20617892f953da297a334d03; uid_tt_ss=9d074cfe20617892f953da297a334d03; sid_tt=f8b2a6bcd2d9867ca40913cc0641c9b3; sessionid=f8b2a6bcd2d9867ca40913cc0641c9b3; sessionid_ss=f8b2a6bcd2d9867ca40913cc0641c9b3; is_staff_user=false; sid_ucp_v1=1.0.0-KDdlNjA2ODlhNWVkMTM1NDhiZmZhYmE2OGY3YjE0ZjhkOTg1NTQ3NWEKGAiDvLCggc2CARCxhLjABhgYIAw4AkDxBxoCbGYiIGY4YjJhNmJjZDJkOTg2N2NhNDA5MTNjYzA2NDFjOWIz; ssid_ucp_v1=1.0.0-KDdlNjA2ODlhNWVkMTM1NDhiZmZhYmE2OGY3YjE0ZjhkOTg1NTQ3NWEKGAiDvLCggc2CARCxhLjABhgYIAw4AkDxBxoCbGYiIGY4YjJhNmJjZDJkOTg2N2NhNDA5MTNjYzA2NDFjOWIz; odin_tt=be26fae28cc323f95bde97b5f38312b4257f272a22986519a54d111aed0ea710245e54c42dfa8766b413c6bed29aa034; ttwid=1%7C_libU-z56BlqzEc2lcd_bAR1Sb7sMz_s4cY9f6Hig6o%7C1745748749%7C9067c41f33e7d8190c907f463fbfd5b80528603e70d82357ee1323eced6979ae; tt_anti_token=bkZDFfqSRkce-f3dcad7e7636fc5db79ef083aa9aa3519ccd036b179f3aaddfa922d5d152732e; tt_scid=emLMklt5zjxx75gkz5c0W8MRCn7gMxh-vtcL7UCNIngtDFfdz7EhmaGgP8toUDbt3f35")
    root_logger.info("[今日头条]开始抓取今日头条内容")
    hotspot_linklist=[]
    #匹配热榜区域上的<a/>标签
    hot_eles=main_tab.eles("@@tag():a@@class=article-item@@rel=noopener nofollow")
    target_count=-1#后面要去除首个，所以取-1
    for ele in hot_eles:
        #获取热榜文章链接，可能是trending链接也可能是article链接
        pre_url=ele.attr("href")
        #确保是article链接，如果不是找trending链接里面的article链接
        if re.search("video",pre_url):
            continue
        if re.search("trending",pre_url):
            find_tab=webpage.new_tab(url=pre_url)
            try:
                #尝试寻找trending下的article链接
                new_ele=find_tab.ele("@@tag():a@@href:article",timeout=1)#模糊匹配article
                article_url=new_ele.attr("href")
            except Exception as e:
                root_logger.info(f"[今日头条]当前链接不是article链接，链接内也未找到article链接{pre_url}")
                find_tab.close()
                continue
            else:
                find_tab.close()
                hotspot_linklist.append(article_url)
                root_logger.info(f"[今日头条]找到热榜文章链接{article_url}")#少个冒号做区别
        else :
            root_logger.info(f"[今日头条]找到热榜文章链接:{pre_url}")
            hotspot_linklist.append(pre_url)

    hotspot_linklist=hotspot_linklist[1:]
    #单个新闻的格式
    root_logger.info("[今日头条]开始抓取新闻内容")
    #遍历所有hot链接，获取内容，
    # 新开标签，爬新闻，存入list，退出
    tab = webpage.new_tab()
    for hot_url in hotspot_linklist:
        toutiao_news=NewsItem()
        toutiao_news["SourceTextLink"] = ["来源于[头条新闻]点击查看原文",hot_url]
        tab.get(hot_url)
        #对文章属性进行提取
        try:
            toutiao_news["Title"]=tab.ele("@tag():h1").text
            p_list=tab.ele("@tag():article").eles("@tag():p")
            contents=[]
            for p in p_list:
                content=p.text
                contents.append(content)
            toutiao_news["MainText"]="".join(contents)
            
            toutiao_news["ImageUrl"]=tab.ele("@tag():article",timeout=1).ele("@tag():img",timeout=1).attr("src")#头条新闻没有图片
            contents=[]
            news_queue.put(toutiao_news.copy())#传回副本，因为这个变量被复用
            root_logger.info(f"[今日头条]单次抓取完成:{hot_url}")
        except Exception as e:
            root_logger.error(e)
            root_logger.info(f"[今日头条]可能是链接内没有文本内容有问题{hot_url}，跳过")
            continue
    time.sleep(0.5)
    #子tab关闭
    tab.close()
    #主tab关闭
    main_tab.close()
    time.sleep(0.5)


def get_zhihuToday(webpage: WebPage,news_queue:queue.Queue):
    """
    获取知乎日报的文章
    """
    url = "https://tophub.today/n/KMZd7VOvrO"  # 进入知乎日报
    # 主tab
    main_tab = webpage.new_tab(url=url)  # 返回mixtab对象
    root_logger.info("[知乎日报]开始抓取知乎日报内容")
    linklist = []
    hot_eles = main_tab.ele("@@tag():div@@class=cc-dc-c").eles("@@tag():a@@rel=nofollow@!title")
    #存在重复a标签，所以加@!title
    for ele in hot_eles:
        linklist.append(ele.attr("href"))
    # 单个新闻的格式
    zhihu_articles = NewsItem()
    root_logger.info("[知乎日报]开始抓取知乎日报内容")
    tab = webpage.new_tab()
    for hot_url in linklist:
        zhihu_articles["SourceTextLink"] = ["来源于[知乎日报]点击查看原文",hot_url]
        tab.get(hot_url)
        # 对文章属性进行提取,有些文章可能不完整不包含部分内容，所以使用try语块
        try:
            zhihu_articles["Title"] = tab.ele("@@tag()=p@@class=DailyHeader-title", timeout=1).text
            # 获取文章内所有p标签
            content_eles=tab.ele("@@tag()=div@@class=content").eles("@tag():p")
            contents =""
            for ele in content_eles:
                contents=contents+ele.text
            zhihu_articles["MainText"] = contents
            zhihu_articles["ImageUrl"] = tab.ele("@@tag():img@@alt:头图",timeout=1).attr("src")#知乎日报没有图片
            if zhihu_articles["MainText"]=="":continue
            news_queue.put(zhihu_articles.copy())  # 传回副本，因为这个变量被复用
            root_logger.info(f"[知乎日报]单次抓取完成{hot_url}")
        except Exception as e:
            root_logger.error(e)
            root_logger.info(f"[知乎日报]可能是链接内没有文本内容有问题{hot_url}，跳过")
            continue
    time.sleep(0.5)
    # 子tab关闭
    tab.close()
    # 主tab关闭
    main_tab.close()
    time.sleep(0.5)

def get_pengpai(webpage: WebPage,news_queue:queue.Queue):
    url = "https://tophub.today/n/wWmoO5Rd4E"  # 进入澎湃新闻列表
    # 主tab
    main_tab = webpage.new_tab(url=url)  # 返回mixtab对象
    root_logger.info("[澎湃新闻]开始抓取澎湃新闻内容")
    linklist = []
    #第一个cc-dc-c下的所有a标签
    hot_eles = main_tab.ele("@@tag():div@@class=cc-dc-c").eles("@@tag():a@@rel=nofollow@!title")
    #存在重复a标签，所以加@!title
    for ele in hot_eles:
        linklist.append(ele.attr("href"))
    root_logger.info("[澎湃新闻]开始抓取澎湃新闻的内容")
    tab = webpage.new_tab()
    pengpai_news=NewsItem()
    for hot_url in linklist:
        pengpai_news["SourceTextLink"] = ["来源于[澎湃新闻]点击查看原文",hot_url]
        tab.get(hot_url)
        # 对文章属性进行提取,有些文章可能不完整不包含部分内容，所以使用try语块
        try:
            pengpai_news["Title"] = tab.ele("@@tag()=h1@@class:index_title", timeout=1).text
            # 获取文章内所有p标签
            content_eles=tab.ele("@@tag()=div@@class:index_centent").eles("@tag():p")
            contents =""
            for ele in content_eles:
                pengpai_context=ele.text
                if type(pengpai_context) is list:
                    contents=contents+("".join(pengpai_context))
                else:
                    contents=contents+pengpai_context
            pengpai_news["content"] = contents
            pengpai_news["ImageUrl"] = tab.ele("@@tag()=div@@class:index_centent",timeout=1).ele("@tag()=img",timeout=1).attr("src")#澎湃新闻没有图片
            news_queue.put(pengpai_news.copy())  # 传回副本，因为这个变量被复用
            root_logger.info(f"[澎湃新闻]单次抓取完成{hot_url}")
        except Exception as e:
            root_logger.error(e)
            root_logger.info(f"[澎湃新闻]可能是链接没有文本内容{hot_url}，跳过")
            continue
    time.sleep(0.5)
    # 子tab关闭
    tab.close()
    # 主tab关闭
    main_tab.close()
    time.sleep(0.5)


def crawl_entrence(script_dir,news_queue:queue.Queue):
    root_logger.info("[crawl]开始爬虫抓取新闻原稿")
    co.set_browser_path(os.path.join(script_dir,r"chrome-win\chrome.exe")) 
    webpage=WebPage(mode="d",chromium_options=co,session_or_options=so)#返回webpage对象

    get_pengpai(webpage,news_queue,)
    get_zhihuToday(webpage=webpage,news_queue=news_queue)
    get_toutiao(webpage=webpage,news_queue=news_queue,)
    root_logger.info("[crawl]爬虫完成，文章内容在news_queue队列")
    webpage.clear_cache(True,True,True,True)
    webpage.close()
    return