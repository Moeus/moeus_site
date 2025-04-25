<template>
    <ClientOnly>
      <AnimatedTestimonials :testimonials="testimonials" :autoplay="false" :duration="5000" />
    </ClientOnly>
  </template>
  
  <script lang="ts" setup>
import AnimatedTestimonials from "./inspira_ui/AnimatedTestimonials.vue";


  const testimonials= [
//@#*&
  {
  "MainText": "你好你阿红你哦啊hop",
  "Title": "Testimonial 1",
  "SourceTextLink":["今日头条", "https://www.toutiao.com"],
  "ImageUrl": "/qq.jpg",
  },
  {
  "MainText": "你好你阿红你哦啊hop",
  "Title": "Testimonial 2",
  "SourceTextLink":["澎湃新闻", "httpswww.pengpai.com"],
  "ImageUrl": "/wechat.png",
  }
//@#*&
  ];

  </script>