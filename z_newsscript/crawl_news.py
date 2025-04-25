import requests
from bs4 import BeautifulSoup
import re
import os
'''
interface NewsItem {
	"MainText": string;
	"Title": string;
	"SourceTextLink":string[];// [text, link]
	"ImageUrl": string;
}
'''
NewsItem={
    "MainText": "",
    "Title": "",
    "SourceTextLink":["",""],
    "ImageUrl": ""
}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

def PengPai(path,):
	url="https://www.thepaper.cn/newsDetail_forward_30714200"
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	Title=soup.find("h1").get_text()
	MainText_tag=soup.find("div", class_="index_cententWrap__Jv8jK")
	MainText=MainText_tag.get_text()
	image_url=MainText_tag.find("img")["src"]
	NewsItem["MainText"]=MainText
	NewsItem["Title"]=Title
	NewsItem["ImageUrl"]=image_url
	NewsItem["SourceTextLink"]=["澎湃新闻",url]
	print(NewsItem)	
	#下载图片
	response = requests.get(image_url, headers=headers)
	print(response.text)
	with open(os.path.join(,/image.jpg, "wb") as f:
		f.write(response.content)
 
	

 
if __name__=="__main__":
    script_path = os.path.dirname(os.path.abspath(__file__))
    print(script_path)
	# PengPai()