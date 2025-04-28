<template>
    <ClientOnly>
      <AnimatedTestimonials :NewsItems="NewsItems" :autoplay="false" :duration="5000" />
    </ClientOnly>
  </template>
  
  <script lang="ts" setup>
import AnimatedTestimonials from "./inspira_ui/AnimatedNewsItems.vue";


  const NewsItems= [
//(@#
{'SourceTextLink': ['来源于[澎湃新闻]点击查看原文', 'https://www.thepaper.cn/newsDetail_forward_30730895'], 'Title': '野猪穿过江苏电视台楼前广场，被抓捕后送往红山森林动物园', 'MainText': '4月27日17时20分左右，一只野猪穿过江苏电视台楼前广场，随后从东南角跑出，跑到进香河路段。特警和消防赶到现场搜捕，野猪已被抓捕并送往南京市红山森林动物园。专家提醒，遇到野猪应尽快远离，不要尝试装死或与之搏斗，可报警或报告林草部门。野猪主要在晨昏和夜间活动，注意防范。', 'ImageUrl': '83c40c416f171cb60a070c63f15e2c5e.jpg'},{'SourceTextLink': ['来源于[知乎日报]点击查看原文', 'https://daily.zhihu.com/story/9780783'], 'Title': '石头缝里都能长树，为什么草原不长树？', 'MainText': '草原也长树，但木本植物存活率低。草原年降水量250-750毫米，适合草本植物生长。草本植物根系密集，迅速吸收水分，阻碍树木幼苗生长。白桦幼苗穿透钙积层存活率不足5%。岩石裂隙环境独特，马尾松根系能从岩石孔隙中汲取水分。草原火灾频繁，摧毁树木幼苗，但刺激草本植物生长。河谷地带胡杨通过克隆繁殖存活。气候变化、CO2浓度升高可能改变植物竞争格局。', 'ImageUrl': 'd624229422c40ccbf4dd22c4d869fd11.jpg'},{'SourceTextLink': ['来源于[知乎日报]点击查看原文', 'https://daily.zhihu.com/story/9780772'], 'Title': '为什么四大家鱼是青草鲢鳙，而没有鲫鱼和鲤鱼？', 'MainText': '鲫鱼和鲤鱼在封闭的鱼塘中能自我繁殖，而四大家鱼不能，所以四大家鱼是放进去的鱼苗长成的。鲤鱼的养殖历史早于四大家鱼，早在唐朝前就有养殖经验。四大家鱼的育苗问题一直是个难题，直到建国后科学家才解决了这个问题。鲤鱼因其自我繁殖能力，成为唐朝前的主要养殖鱼类。养殖鱼类的饲料比是关键，鲢鱼和鳙鱼的饲料比低于1:1，而鲫鱼的饲料比高且体型有限，野外捕捞更方便，因此不作为主要养殖对象。', 'ImageUrl': '881107e0b3e9e1b5afb6f7903bf8f3ed.jpg'},{'SourceTextLink': ['来源于[澎湃新闻]点击查看原文', 'https://www.thepaper.cn/newsDetail_forward_30730768'], 'Title': '上海超万套保租房供应高校毕业生，各项目免押、打折等优惠频出', 'MainText': '2025年4月27日，上海启动‘保租房毕业季进校园’第四季，提供1万余套保租房给应届毕业生。房源集中在交通便利区域，租金2500-3000元/月。多家企业推出优惠政策，如92折、86折、首月99元、租房补贴、免押等。启动仪式后，同济大学举办供需对接会，50余家企业参与，1700余学生初步确定租赁意向。政策放宽，应届生毕业两年内可申请保租房。', 'ImageUrl': '6b4eecc2142ac391354e54298d3c1538.jpg'}
//(@#
  ];

  </script>