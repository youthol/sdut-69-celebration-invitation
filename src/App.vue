<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'
import FirstSlide from './components/FirstSlide.vue'
import FourthSlide from './components/FourthSlide.vue'
import SecondSlide from './components/SecondSlide.vue'
import ThirdSlide from './components/ThirdSlide.vue'
const currentSlide = ref(-1)

const spaceBetween = 0
const onProgress = (e) => {
  const [swiper, progress] = e.detail
  // console.log(progress)
  // console.log(swiper.activeIndex)
}

const onSlideChange = (e) => {
  console.log('slide changed')
  const [swiper, progress] = e.detail
  console.log(swiper.activeIndex)
  currentSlide.value = swiper.activeIndex
}

onMounted(() => {
  currentSlide.value = 0
})
onBeforeUnmount(() => {})
</script>

<template>
  <div class="swiper-box">
    <swiper-container
      class="swiper"
      :slides-per-view="1"
      :space-between="spaceBetween"
      :centered-slides="true"
      :pagination="{
        hideOnClick: true,
      }"
      :breakpoints="{
        768: {
          slidesPerView: 1,
        },
      }"
      :direction="'vertical'"
      :effect="'fade'"
      @swiperprogress="onProgress"
      @swiperslidechange="onSlideChange"
    >
      <swiper-slide class="swiper-slide">
        <transition>
          <FirstSlide v-if="currentSlide === 0" :key="currentSlide"></FirstSlide>
        </transition>
      </swiper-slide>
      <swiper-slide class="swiper-slide">
        <transition>
          <SecondSlide v-if="currentSlide === 1" :key="currentSlide"></SecondSlide>
        </transition>
      </swiper-slide>
      <swiper-slide class="swiper-slide">
        <transition>
          <ThirdSlide v-if="currentSlide === 2" :key="currentSlide"></ThirdSlide>
        </transition>
      </swiper-slide>
      <swiper-slide class="swiper-slide">
        <transition>
          <FourthSlide v-if="currentSlide === 3" :key="currentSlide"></FourthSlide>
        </transition>
      </swiper-slide>
    </swiper-container>
  </div>
</template>
<style>
.swiper-box {
  width: 100vw;
  height: 100vh;
}

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  background-image: url(./assets/img/bkg.jpeg);
  /* background-image: url(./assets/img/bkg2.png); */
  background-size: cover; /* 或使用 contain 根据需求 */
  background-position: center;
  background-repeat: no-repeat;

  width: 100vw;
  color: white;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.slide-item {
  width: 100vw;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
</style>
