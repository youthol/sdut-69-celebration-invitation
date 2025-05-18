<script setup>
import { Fireworks } from 'fireworks-js'
import { nextTick, onBeforeUnmount, onMounted, ref } from 'vue'

const fireworks = ref(null)
const fireworksCanvas = ref(null)

onMounted(async () => {
  await nextTick() // 等 Vue 渲染出 <canvas>
  // 如果旧实例还在，先彻底销毁
  if (fireworks.value) {
    fireworks.value.stop()
    fireworks.value.clear() // 清掉所有残余
    fireworks.value = null
  }
  // 再 new 一个新的
  fireworks.value = new Fireworks(fireworksCanvas.value, {
    /* ...options */
  })
  fireworks.value.start()
})
// 清理
onBeforeUnmount(() => {
  fireworks.value?.stop()
  fireworks.value = null
})
</script>
<template>
  <div class="slide-item">
    <canvas ref="fireworksCanvas" class="fireworks-canvas"></canvas>
    <div class="top-gap"></div>
    <div class="activity-title animate__animated animate__backInDown">山东理工大学 69 周年庆典</div>
    <div class="invite-title animate__animated animate__backInLeft">校庆邀请</div>
    <div class="activity-subtitle animate__animated animate__backInRight">庆祝学校建校 69 周年</div>
    <div class="invite-text-group animate__animated animate__backInUp">
      <div class="invite-text">山东理工大工学</div>
      <div class="invite-text">69 周年校庆诚邀您的到来</div>
    </div>
  </div>
  <div class="move-tips">
    <div class="move-tips-arrows animate__animated animate__heartBeat animate__infinite">↑</div>
    <div class="move-tips-text">向上滑动查看更多</div>
  </div>
</template>

<style scoped>
.slide-item {
  width: 100vw;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
.hidden {
  display: none;
}

.top-gap {
  height: 20vh;
}

.activity-title {
  /* 4. 渐变填充文字（chrome/safari/gecko 都支持前缀） */
  background: linear-gradient(180deg, #ffd66b, #f0a430);
  background-clip: text;
  -webkit-text-fill-color: transparent;

  font-size: 1.5rem;
  font-weight: 800;

  margin: 20px 0;
}

.invite-title {
  /* 1. 字体：使用手写、楷体等，或者引入自定义书法字体 */
  font-family: 'STKaiti', 'KaiTi', serif;
  /* 2. 字号根据需求调整 */
  font-size: 5rem;
  /* 3. 文字粗细 */
  font-weight: 900;
  /* 4. 渐变填充文字（chrome/safari/gecko 都支持前缀） */
  background: linear-gradient(180deg, #ffd66b, #f0a430);
  background-clip: text;
  -webkit-text-fill-color: transparent;
  /* 5. 给文字加一层金色描边（webkit 专用） */
  /* -webkit-text-stroke: 1px rgba(255, 204, 102, 0.8); */

  /* 7. 居中对齐（容器需 text-align: center;） */
  display: inline-block;
}

.activity-subtitle {
  font-size: 1.5rem;
  font-weight: 700;

  background: linear-gradient(180deg, #ffd66b, #f0a430);
  color: #d63e0f;

  padding: 10px 30px;
  margin: 20px 0;
  border-radius: 7px;

  display: flex;
  justify-content: center;
  align-items: center;
}

.invite-text-group {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 20px 0;
}

.invite-text {
  background: linear-gradient(180deg, #ffeab4, #ffc772);
  background-clip: text;
  -webkit-text-fill-color: transparent;

  font-size: 1.2rem;
  font-weight: 700;
  padding: 4px;
}

.fireworks-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 0; /* 放在最底层 */
}

.slide-item > *:not(.fireworks-canvas) {
  position: relative;
  z-index: 1; /* 文字内容盖在上面 */
}

.move-tips {
  position: fixed;
  bottom: 12vh;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.move-tips-arrows,
.move-tips-text {
  /* 渐变文字保持不变 */
  background: linear-gradient(180deg, #ffd66b, #f0a430);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow:
    0 0 4px rgba(255, 214, 107, 0.6),
    0 0 8px rgba(255, 214, 107, 0.4);
  /* 共同的发光动画 */
}

/* 箭头更大号 */
.move-tips-arrows {
  font-size: 3rem;
  font-weight: 900;
}

/* 文字说明稍小 */
.move-tips-text {
  font-size: 1.2rem;
  font-weight: 900;
  margin-top: 10px;
}
</style>
