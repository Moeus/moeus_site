<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lucide-static@latest/style.css">
  <div class="mx-auto max-w-sm px-4 py-20 font-sans antialiased lg:px-12 md:max-w-4xl md:px-8">
    <div class="relative grid grid-cols-1 gap-20 md:grid-cols-2">
      <div>
        <div class="relative h-80 w-full">
          <AnimatePresence>
            <Motion
              v-for="(NewsItem, index) in props.NewsItems"
              :key="NewsItem.ImageUrl"
              as="div"
              :initial="{
                opacity: 0,
                scale: 0.9,
                z: -100,
                rotate: randomRotateY(),
              }"
              :animate="{
                opacity: isActive(index) ? 1 : 0.7,
                scale: isActive(index) ? 1 : 0.95,
                z: isActive(index) ? 0 : -100,
                rotate: isActive(index) ? 0 : randomRotateY(),
                zIndex: isActive(index) ? 40 : NewsItems.length + 2 - index,
                y: isActive(index) ? [0, -80, 0] : 0,
              }"
              :exit="{
                opacity: 0,
                scale: 0.9,
                z: 100,
                rotate: randomRotateY(),
              }"
              :transition="{
                duration: 0.4,
                ease: 'easeInOut',
              }"
              class="absolute inset-0 origin-bottom"
            >
              <img
                :src="NewsItem.ImageUrl"
                :alt="NewsItem.Title"
                width="500"
                height="500"
                :draggable="false"
                class="size-full rounded-3xl object-cover object-center"
              />
            </Motion>
          </AnimatePresence>
        </div>
      </div>
      <div class="flex flex-col justify-between py-4">
        <Motion
          :key="active"
          as="div"
          :initial="{
            y: 20,
            opacity: 0,
          }"
          :animate="{
            y: 0,
            opacity: 1,
          }"
          :exit="{
            y: -20,
            opacity: 0,
          }"
          :transition="{
            duration: 0.2,
            ease: 'easeInOut',
          }"
        >
          <h3 class="text-2xl font-bold text-black dark:text-white">
            {{ props.NewsItems[active].Title }}
          </h3>
          <a class="11" :href="props.NewsItems[active].SourceTextLink[1]" target="_blank">
            {{ props.NewsItems[active].SourceTextLink[0] }}
          </a>
          <Motion
            as="p"
            class="mt-8 text-lg text-gray-500 dark:text-neutral-300"
          >
            <Motion
              v-for="(word, index) in activeTestimonialQuote"
              :key="index"
              as="span"
              :initial="{
                filter: 'blur(10px)',
                opacity: 0,
                y: 5,
              }"
              :animate="{
                filter: 'blur(0px)',
                opacity: 1,
                y: 0,
              }"
              :transition="{
                duration: 0.2,
                ease: 'easeInOut',
                delay: 0.02 * index,
              }"
              class="inline-block"
            >
              {{ word }}&nbsp;
            </Motion>
          </Motion>
        </Motion>
        <div class="flex gap-4 pt-12 md:pt-0">
          <button
            class="group/button flex size-7 items-center justify-center rounded-full bg-gray-100 dark:bg-neutral-800"
            @click="handlePrev"
          >
            <ArrowLeft 
              name="lucide:arrow-left"
              class="size-5 text-black transition-transform duration-300 group-hover/button:rotate-12 dark:text-neutral-400"
            />
          </button>
          <button
            class="group/button flex size-7 items-center justify-center rounded-full bg-gray-100 dark:bg-neutral-800"
            @click="handleNext"
          >
            <ArrowRight
              name="lucide:arrow-right"
              class="size-5 text-black transition-transform duration-300 group-hover/button:-rotate-12 dark:text-neutral-400"
            />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ArrowRight,ArrowLeft  } from 'lucide-vue-next';
import {AnimatePresence, Motion} from "motion-v";
import { ref,computed,onMounted,onUnmounted } from "vue";
interface NewsItem {
  "MainText": string;
  "Title": string;
  "SourceTextLink":string[];// [text, link]
  "ImageUrl": string;
}
interface Props {
  NewsItems?: NewsItem[];
  autoplay?: boolean;
  duration?: number;
}

const props = withDefaults(defineProps<Props>(), {
  NewsItems: () => [],
  autoplay: () => false,
  duration: 5000,
});

const active = ref(0);

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const interval = ref<any>();

const activeTestimonialQuote = computed(() => {
  return props.NewsItems[active.value].MainText.split(" ");
});

onMounted(() => {
  if (props.autoplay) {
    interval.value = setInterval(handleNext, props.duration);
  }
});

onUnmounted(() => {
  if (!interval.value) {
    clearInterval(interval.value);
  }
});

function handleNext() {
  active.value = (active.value + 1) % props.NewsItems.length;
}

function handlePrev() {
  active.value = (active.value - 1 + props.NewsItems.length) % props.NewsItems.length;
}

function isActive(index: number) {
  return active.value === index;
}

function randomRotateY() {
  return Math.floor(Math.random() * 21) - 10;
}
</script>

<style scoped>
a {
  font-size: 0.875rem; /* text-sm 对应的值 */
  color: #6b7280; /* text-gray-500 对应的值 */
  text-decoration: underline;
}

/* 适配暗黑模式 */
@media (prefers-color-scheme: dark) {
  a {
    color: #a3a3a3; /* dark:text-neutral-500 对应的值 */
  }
}
</style> 