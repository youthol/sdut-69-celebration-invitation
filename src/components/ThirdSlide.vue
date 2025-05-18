<script setup>
import { http } from '@/utils/http'
import { nextTick, onMounted, reactive, ref, watch } from 'vue'

const isRelayed = ref(false)
const visitorNum = ref(0)
const showEffect = ref(false)
const myRelayNum = ref(0)

// 成功后 触发粒子特效 3s
watch(isRelayed, (val) => {
  if (val) {
    showEffect.value = true
    setTimeout(() => {
      showEffect.value = false
    }, 3000)
  }
})

// 真正执行「接力」请求
async function doRelay() {
  try {
    const res = await http.post('/relay/')
    const num = res.data.visitorNum
    // 标记已经接力，并把当前编号存储
    localStorage.setItem('hasRelayed', '1')
    localStorage.setItem('myRelayNum', num)
    isRelayed.value = true
    visitorNum.value = num
    myRelayNum.value = num
  } catch {
    alert('接力失败，请稍后再试')
  }
}

function postRelay() {
  if (!isRelayed.value) doRelay()
}

// 仅取当前接力人数（不新增）
async function fetchVisitorNum() {
  try {
    const res = await http.get('/relay/count/')
    visitorNum.value = res.data.visitorNum
  } catch {
    alert('获取接力人数失败，请稍后再试')
  }
}

// confetti 粒子配置（红金主基调）
const confettiOptions = reactive({
  particles: {
    number: { value: 0 },
    shape: {
      type: 'circle',
      options: {},
    },
    color: {
      value: ['#FFD66B', '#F0A430', '#D63E0F'],
    },
    opacity: { value: 1 },
    size: {
      value: { min: 4, max: 8 },
      random: true,
    },
    life: {
      duration: { sync: true, value: 2 },
      count: 1,
    },
    move: {
      enable: true,
      gravity: { enable: true, acceleration: 15 },
      speed: { min: 20, max: 40 },
      decay: 0.05,
      direction: 'none',
      outModes: { default: 'destroy' },
    },
  },
  emitters: {
    direction: 'none',
    life: { count: 1, duration: 0.1 },
    rate: { quantity: 200, delay: 0.1 },
    size: { width: 0, height: 0 },
    // 默认居中，后面点击时会重写
    position: { x: 50, y: 50 },
  },
  detectRetina: true,
})

// 监听点击，动态设置发射点
function onClickSlide(e) {
  const rect = e.currentTarget.getBoundingClientRect()
  // 计算百分比
  const x = ((e.clientX - rect.left) / rect.width) * 100
  const y = ((e.clientY - rect.top) / rect.height) * 100
  // 更新 emitters 位置
  confettiOptions.emitters.position.x = x
  confettiOptions.emitters.position.y = y

  // 触发并重置定时
  showEffect.value = true
  clearTimeout(window._hideConfetti)
  window._hideConfetti = setTimeout(() => {
    showEffect.value = false
  }, 1000) // 1s 后自动隐藏

  // 强制卸载
  showEffect.value = false
  // 下一帧再挂载
  nextTick(() => {
    showEffect.value = true
    // 并且在 1s 后隐藏
    clearTimeout(window._hideConfetti)
    window._hideConfetti = setTimeout(() => {
      showEffect.value = false
    }, 1000)
  })
}

onMounted(async () => {
  // 第一次进来，检查 localStorage
  if (localStorage.getItem('hasRelayed') === '1') {
    isRelayed.value = true
    // 从存的值里读 myRelayNum
    myRelayNum.value = parseInt(localStorage.getItem('myRelayNum'), 10) || 0
    // 并同步最新总数（保持显示准确）
    await fetchVisitorNum()
  } else {
    // 如果没接力，仍然加载当前总数展示
    await fetchVisitorNum()
  }
})
</script>
<template>
  <div class="slide-item" @click="onClickSlide">
    <!-- 效果层（保持不变） -->
    <!-- 效果层 -->
    <vue-particles v-if="showEffect" id="confetti" class="confetti" :options="confettiOptions" />

    <!-- 交互卡片 -->
    <div class="top-gap"></div>
    <div class="relay-card" :class="{ success: isRelayed }">
      <div class="relay-title">
        {{ isRelayed ? '接力成功！' : '成为接力者！' }}
      </div>

      <!-- 未接力：显示按钮 -->
      <button
        v-if="!isRelayed"
        class="relay-btn animate__animated animate__pulse animate__infinite"
        @click="postRelay"
      >
        点我为校庆接力
      </button>

      <!-- 成功后：显示独立的数字文案 -->
      <div v-else class="visitor-info">
        <div class="visitor-total">已有 {{ visitorNum }} 位接力者为母校接力</div>
        <div class="visitor-myself animate__animated animate__pulse animate__infinite">
          你是第 <span class="visitor-num">{{ myRelayNum }}</span> 位接力者
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.slide-item {
  position: relative;
  width: 100vw;
  height: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  overflow: hidden;
}

.top-gap {
  height: 30vh;
}

/* 粒子全屏层 */
.confetti {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
}

/* 卡片 */
.relay-card {
  position: relative;
  z-index: 2;
  width: 70%;
  max-width: 360px;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid #ffd66b;
  border-radius: 1rem;
  box-shadow: 0 0 20px rgba(240, 164, 48, 0.5);
  text-align: center;
  transition: transform 0.3s;
}
/* .relay-card.success {
  border-color: #d63e0f;
  box-shadow: 0 0 30px rgba(214, 62, 15, 0.7);
  transform: scale(1.05);
} */

/* 标题 */
.relay-title {
  font-size: 1.75rem;
  color: #ffd66b;
  font-family: 'STKaiti', KaiTi, serif;
  margin-bottom: 1.5rem;
  transition: color 0.3s;

  font-weight: 700;
}
.relay-card.success .relay-title {
  /* color: #d63e0f; */
  color: #ffd66b;
  animation: pulse 1s ease-in-out infinite alternate;
}

/* 按钮 */
.relay-btn {
  font-size: 1.1rem;
  padding: 0.75rem 1.5rem;
  color: #fff;
  background: linear-gradient(45deg, #f0a430, #ffd66b);
  border: none;
  border-radius: 0.75rem;
  cursor: pointer;
  transition:
    transform 0.2s,
    box-shadow 0.2s;
  box-shadow: 0 4px 12px rgba(240, 164, 48, 0.6);
}
.relay-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(240, 164, 48, 0.8);
}
.relay-btn:disabled {
  opacity: 0.6;
  cursor: default;
  background: #555;
  box-shadow: none;
}

/* 成功后的数字文案容器 */
.visitor-info {
  margin-top: 1.5rem;
  font-size: 1.25rem;
  color: #ffeab4; /* 浅金色文字 */
  text-align: center;
}

.visitor-total {
  margin: 10px 0 0 0;
  font-size: 1rem;
  color: #ffeab4; /* 浅金色文字 */
}

/* 数字高亮 */
.visitor-num {
  font-size: 2.5rem; /* 更大号 */
  font-weight: bold;
  color: #ffd66b; /* 金色 */
  margin: 0 0.3em;
  display: inline-block;
}

/* success 标题闪烁动画 */
@keyframes pulse {
  from {
    text-shadow: 0 0 8px rgba(214, 62, 15, 0.8);
  }
  to {
    text-shadow: 0 0 20px rgba(214, 62, 15, 1);
  }
}
</style>
