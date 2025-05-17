<script setup>
import { reactive } from 'vue'

const particlesLoaded = async (container) => {
  console.log('Particles container loaded', container)
}

const particlesOptions = reactive({
  fpsLimit: 60,
  particles: {
    number: { value: 0 },
    shape: {
      type: 'character',
      options: {
        character: {
          value: ['🎂'],
          font: 'Verdana',
          style: '',
          weight: '400',
          fill: true,
        },
      },
    },
    size: { value: { min: 16, max: 32 } },
    opacity: { value: 1 },
    move: {
      enable: true,
      direction: 'bottom',
      speed: { min: 10, max: 40 },
      gravity: { enable: true, acceleration: 8 },
      straight: true, // ← 让运动轨迹笔直
      random: false, // ← 关闭随机偏移
      outModes: {
        default: 'destroy',
        top: 'none', // ← 关键：允许顶部生成再落下
      },
    },
    life: {
      duration: { value: 10, sync: false },
      count: 0,
    },
  },
  emitters: {
    direction: 'bottom',
    position: { x: 50, y: -5 }, // 可微调，-5 比 -10 更贴近可见区域
    rate: { quantity: 1, delay: 0.5 },
    size: { width: 100, height: 0 },
    life: { count: 0 },
  },
  detectRetina: true,
})
</script>

<template>
  <div class="slide-item">
    <vue-particles
      id="tsparticles"
      @particles-loaded="particlesLoaded"
      :options="particlesOptions"
    />
    <div class="sdut-name animate__animated animate__fadeIn">山东理工大学</div>
    <div class="letter animate__animated animate__fadeIn">
      <div class="letter-start">亲爱的SDUTers：</div>
      <div class="letter-content">
        &emsp;&emsp;六十九载春秋，感恩一路同行，幸而携手并肩
        每一份热忱都值得铭记，每一份努力都熠熠生辉 纵使山海远阔，亦挡不住思念与牵挂
        值此母校六十九周年校庆之际 让我们共同 向母校献上最真挚的祝愿
        愿山东理工大学桃李满园，再谱华章！ 山东理工大学69岁生日快乐！
      </div>
      <div class="letter-end">山东理工大学</div>
    </div>
  </div>
</template>

<style scoped>
.slide-item {
  position: relative;
  width: 100vw;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.sdut-name {
  font-size: 1.5rem;
  font-weight: 700;

  background: linear-gradient(180deg, #ffd66b, #f0a430);
  color: #d63e0f;

  padding: 10px 30px;
  border-radius: 71111px;

  display: flex;
  justify-content: center;
  align-items: center;
}

.particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.letter {
  width: 60%;
  margin: 1rem auto 2rem;
  padding: 2rem 2.5rem;
  background: rgba(0, 0, 0, 0.4); /* 半透明深底 */
  border: 1px solid rgba(255, 215, 0, 0.8); /* 金色描边 */
  border-radius: 1rem; /* 圆角 */
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.4); /* 金色光晕 */
  backdrop-filter: blur(5px); /* 背景虚化 */
  color: #ffeab4; /* 金黄色文字 */
  font-family: 'STKaiti', KaiTi, serif; /* 书法楷体 */
  line-height: 1.8;
  text-align: center;
  position: relative;

  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* 装饰用的金色角花 */
.letter::before,
.letter::after {
  content: '';
  position: absolute;
  width: 1.5rem;
  height: 1.5rem;
  border: 2px solid rgba(255, 215, 0, 0.8);
}
.letter::before {
  top: 0.5rem;
  left: 0.5rem;
  border-right: none;
  border-bottom: none;
}
.letter::after {
  bottom: 0.5rem;
  right: 0.5rem;
  border-left: none;
  border-top: none;
}

.letter-start {
  font-size: 1.25rem;
  font-weight: bold;
  margin-bottom: 1rem;
  align-self: flex-start;
}

.letter-content {
  font-size: 1.2rem;
  white-space: pre-wrap;
  margin-bottom: 1.5rem;
  text-align: left;
}

.letter-end {
  font-size: 1.2rem;
  font-style: italic;
  align-self: flex-end;
}
</style>
