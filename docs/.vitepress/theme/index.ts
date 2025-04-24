// https://vitepress.dev/guide/custom-theme
import { h } from 'vue'
import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import './style.css'
import MyLayout from './components/Layout.vue'
import  Linkcard  from './components/Linkcard.vue'
import NewsCard from './components/NewsCard.vue'

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(MyLayout, null, {
      // https://vitepress.dev/guide/extending-default-theme#layout-slots
    })
  },
  enhanceApp({ app, router, siteData }) {
    // ...
    // https://vitepress.dev/guide/extending-default-theme#enhanceapp
    app.component("Linkcard",Linkcard)
    app.component("NewsCard",NewsCard)
  }
} satisfies Theme
