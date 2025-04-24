<template>
    <ClientOnly>
      <AnimatedTestimonials :testimonials="testimonials" />
    </ClientOnly>
  </template>
  
  <script lang="ts" setup>
  import AnimatedTestimonials from "./inspira_ui/AnimatedTestimonials.vue";
  const testimonials = [
    {
      quote:
        "The attention to detail and innovative features have completely transformed our workflow. This is exactly what we've been looking for.",
      name: "Sarah Chen",
      designation: "Product Manager at TechFlow",
      image:
        "/qq.jpg",
    },
    {
      quote:
        "Implementation was seamless and the results exceeded our expectations. The platform's flexibility is remarkable.",
      name: "Michael Rodriguez",
      designation: "CTO at InnovateSphere",
      image:
        "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=3540&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    {
      quote:
        "This solution has significantly improved our team's productivity. The intuitive interface makes complex tasks simple.",
      name: "",
      designation: "Operations Director at CloudScale",
      image:
        "",
    },
    {
      quote:
        "Outstanding support and robust features. It's rare to find a product that delivers on all its promises.",
      name: "今日头条",
      designation: "Engineering Lead at DataPro",
      image:
        "https://p3-sign.toutiaoimg.com/tos-cn-i-axegupay5k/1d3af89b004641179d479a89e0537a41~tplv-tt-origin-web:gif.jpeg?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1746114957&x-signature=36uyUx5pA7FKOFYXSfq9j9GzVJ0%3D",
    },
    {
      quote:
        "The scalability and performance have been game-changing for our organization. Highly recommend to any growing business.",
      name: "知乎日报",
      designation: "VP of Technology at FutureNet",
      image:
        "https://pic1.zhimg.com/v2-1f6eacca593164fbf17b3fdd2baf4304_fhd.jpg?source=8673f162",
    },
  ];
  </script>