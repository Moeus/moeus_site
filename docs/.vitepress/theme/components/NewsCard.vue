<template>
    <ClientOnly>
      <AnimatedTestimonials :NewsItems="NewsItems" :autoplay="false" :duration="5000" />
    </ClientOnly>
  </template>
  
  <script lang="ts" setup>
import AnimatedTestimonials from "./inspira_ui/AnimatedNewsItems.vue";


  const NewsItems= [
//(@#
    {
      "MainText": "123123",
  "Title": "ceshi",
  "SourceTextLink":["ceshiyx","/qq.jpg"],// [text, link]
  "ImageUrl": "/qq.jpg",
    }
//(@#
  ];

  </script>