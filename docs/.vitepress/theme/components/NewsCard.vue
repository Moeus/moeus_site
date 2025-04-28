<template>
    <ClientOnly>
      <AnimatedTestimonials :NewsItems="NewsItems" :autoplay="false" :duration="5000" />
    </ClientOnly>
  </template>
  
  <script lang="ts" setup>
import AnimatedTestimonials from "./inspira_ui/AnimatedNewsItems.vue";


  const NewsItems= [
//(@#
{'SourceTextLink': ['来源于[知乎日报]点击查看原文', 'https://daily.zhihu.com/story/9780775'], 'Title': '为什么会有卖活蟑螂的？或者说，买蟑螂能用来干什么？', 'MainText': '活体蟑螂主要用于爬宠饲料，如樱桃蟑螂和杜比亚蟑螂，它们营养丰富、易于饲养且对人无害。此外，蟑螂也是流行的宠物，如马达加斯加发声蟑螂、犀牛蟑螂等，它们干净、安静、易养。蟑螂还是实验动物，如美洲大蠊。有些人购买蟑螂拍摄猎奇视频或虐待，还有人购买蟑螂进行放生，但这种行为并无正面意义。', 'ImageUrl': '9dced7bd94f830d72c4a904fdbd57ee3.jpg'},{'SourceTextLink': ['来源于[澎湃新闻]点击查看原文', 'https://www.thepaper.cn/newsDetail_forward_30730895'], 'Title': '野猪穿过江苏电视台楼前广场，被抓捕后送往红山森林动物园', 'MainText': '4月27日17时20分，一只野猪穿过江苏电视台楼前广场，随后从东南角跑出，跑至进香河路段。特警和消防赶到现场进行搜捕，最终野猪被成功抓捕并送往南京市红山森林动物园。遇到野猪时，应尽快远离，避免激怒野猪，寻找遮挡物，不要尝试搏斗，可报警求助。野猪主要在晨昏和夜间活动，应注意防范。', 'ImageUrl': '83c40c416f171cb60a070c63f15e2c5e.jpg'},{'SourceTextLink': ['来源于[头条新闻]点击查看原文', 'https://www.toutiao.com/article/7491247477963506213/'], 'Title': '叶落归根，“亚洲前首富”李兆基将回故乡顺德安葬，生前为顺德捐资上亿', 'MainText': '据广州日报消息，4月9日，李兆基家属宣布，李兆基将于4月27日在香港殡仪馆设灵，28日上午举行团体公祭，择吉日返回原籍顺德大良安葬。李兆基于3月17日逝世，享年97岁。作为顺德大良人，李兆基毕生热爱家乡，累计为顺德捐资超过亿元。', 'ImageUrl': 'f38271fd5bbaccb21613e0692ea95410.jpg'},{'SourceTextLink': ['来源于[头条新闻]点击查看原文', 'https://www.toutiao.com/article/7497922339380822564/'], 'Title': '印巴两军再度交火，巴铁希望中方出面调查，为巴基斯坦主持公道', 'MainText': '22日，印控克什米尔发生游客袭击事件，26人死亡，印方指责巴基斯坦。24日深夜，印巴两军在克什米尔边境交火。印度总理莫迪宣布暂停‘印度河水协定’，关闭陆地口岸，取消对巴签证。巴方否认指控，请求中国调查事件真相并增加100亿元人民币货币互换额度。中国支持巴反恐，但参与调查存在困难，需保持中立。', 'ImageUrl': '0cccab1508396d5249fc61a07dd727b1.jpg'},{'SourceTextLink': ['来源于[知乎日报]点击查看原文', 'https://daily.zhihu.com/story/9780772'], 'Title': '为什么四大家鱼是青草鲢鳙，而没有鲫鱼和鲤鱼？', 'MainText': '鲫鱼和鲤鱼在封闭鱼塘中能自我繁殖，而四大家鱼（青鱼、草鱼、鲢鱼、鳙鱼）不能。鲤鱼的养殖历史早，到唐朝前已形成产业，而四大家鱼的规模化养殖到宋代才形成。四大家鱼的育苗问题一直是个难题，直到建国后科学家才解决。鲤鱼因能自我繁殖，成本低，成为早期主要养殖对象。鲫鱼虽然也能自我繁殖，但体型小，饲料比高，且野外易捕，故不常养殖。鲢鱼和鳙鱼因滤食性，饲料比低，适合大规模养殖。', 'ImageUrl': '881107e0b3e9e1b5afb6f7903bf8f3ed.jpg'}
//(@#
  ];

  </script>