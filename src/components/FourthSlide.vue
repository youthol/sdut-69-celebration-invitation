<script setup>
import { http } from '@/utils/http'
import Danmaku from 'danmaku'
import { onBeforeUnmount, onMounted, ref } from 'vue'

const blessList = ref([])
const danmakuRef = ref(null)
let danmaku = null
const showModal = ref(false)
const wishText = ref('')
let cycleTimer = null

// 拉取祝福列表
async function fetchBlessList() {
  //生成十句美好的祝福
  const res = await http.get('/bless/list/')
  blessList.value = res.data
  console.log(res)
}

function openModal() {
  showModal.value = true
  wishText.value = ''
}

function closeModal() {
  showModal.value = false
}

function onSend() {
  if (!wishText.value.trim()) return
  http
    .post('/bless/send/', { content: wishText.value })
    .then((res) => {
      // 发送成功后，祝福列表后追加新的内容
      blessList.value.push(res.data.content)
      alert('发送成功！')
      closeModal()
    })
    .catch((err) => {
      console.error(err)
      alert('发送失败，请稍后再试')
    })
}

// 播放一轮弹幕，并在最后安排下一轮
function playCycle() {
  if (!danmaku || blessList.value.length === 0) return

  const colors = ['#FFD66B', '#F0A430', '#D63E0F', '#ffffff', '#ffeab4']
  const baseInterval = 200 // 每条间隔基础
  const maxRand = 3500 // 随机延迟上限
  const durations = []

  blessList.value.forEach((text, i) => {
    const delay = i * baseInterval + (500 + Math.random() * maxRand)
    durations.push(delay)
    setTimeout(() => {
      const fontSize = 16 + Math.random() * 12
      const color = colors[Math.floor(Math.random() * colors.length)]
      const y = 20 + Math.random() * 60

      danmaku.emit({
        mode: 1,
        text,
        style: {
          fontSize: `${fontSize}px`,
          color,
          textShadow: '1px 1px 2px rgba(0,0,0,0.6)',
          padding: '6px 12px',
          borderRadius: '400px',
          background: 'rgba(0,0,0,0.2)',
        },
        y,
      })
    }, delay)
  })

  // 计算本轮最后一条弹幕“结束”时间：最长延时 + 0ms 持续
  const maxDelay = Math.max(...durations)

  // 安排下一轮
  cycleTimer = setTimeout(playCycle, maxDelay)
}

onMounted(async () => {
  // 初始化 Danmaku
  danmaku = new Danmaku({
    container: danmakuRef.value,
    engine: 'dom',
    width: danmakuRef.value.clientWidth,
    height: danmakuRef.value.clientHeight,
    defaultDuration: 8000,
    mode: 'right',
    comments: [],
  })

  await fetchBlessList()
  playCycle()
})

onBeforeUnmount(() => {
  clearTimeout(cycleTimer)
})
</script>

<template>
  <div class="slide-item">
    <div class="top-gap"></div>
    <div class="board">
      <div class="board-header">祝福母校</div>
      <div ref="danmakuRef" class="board-body"></div>
    </div>

    <div class="send-wish-group">
      <div class="send-btn" @click="openModal">点我发送祝福</div>
    </div>

    <!-- 弹出对话框 -->
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-dialog">
        <div class="modal-header">发送您的祝福</div>
        <textarea
          v-model="wishText"
          class="modal-input"
          placeholder="在此输入您的祝福……"
          rows="4"
        ></textarea>
        <div class="modal-actions">
          <button class="btn btn-cancel" @click="closeModal">取消</button>
          <button class="btn btn-send" @click="onSend">发送</button>
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
  height: 10vh;
}

/* 留言板整体 */
.board {
  position: relative;
  width: 85vw;
  max-width: 600px;
  height: 50vh;
  background: rgba(0, 0, 0, 0.3);
  border: 6px solid transparent;
  border-image: linear-gradient(45deg, #ffd66b, #f0a430) 1;
  border-radius: 1rem;
  box-shadow: 0 0 20px rgba(240, 164, 48, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  flex-direction: column;
}

/* 留言板标题 */
.board-header {
  flex: 0 0 3rem;
  background: linear-gradient(90deg, #f0a430, #ffd66b);
  color: #4a2d0b;
  font-family: 'STKaiti', KaiTi, serif;
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  line-height: 3rem;
  border-top-left-radius: 0.75rem;
  border-top-right-radius: 0.75rem;
  box-shadow: inset 0 -2px 4px rgba(0, 0, 0, 0.2);
}

/* 弹幕跑道区域 */
.board-body {
  position: relative;
  flex: 1;
  margin: 0.5rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 0.5rem;
  overflow: hidden;
}

/* 弹幕元素局限在这里滚动   如果需要，可以再微调字体、背景等*/
/* .board-body .danmaku-comment {

} */

/* 发送祝福按钮 */
.send-wish-group {
  margin-top: 2rem;
  text-align: center;
}
.send-btn {
  display: inline-block;
  font-size: 1.2rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(45deg, #f0a430, #ffd66b);
  color: #ce310b;
  font-weight: 700;
  border-radius: 0.75rem;
  box-shadow: 0 4px 12px rgba(240, 164, 48, 0.6);
  cursor: pointer;
  transition:
    transform 0.2s,
    box-shadow 0.2s;
}
.send-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(240, 164, 48, 0.8);
}

/* Modal 遮罩 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
  backdrop-filter: blur(2px);
}

/* 对话框 */
.modal-dialog {
  width: 75%;
  max-width: 400px;
  background: rgba(255, 255, 255, 0.1);
  border: 4px solid transparent;
  border-image: linear-gradient(45deg, #ffd66b, #f0a430) 1;
  border-radius: 1rem;
  box-shadow: 0 0 20px rgba(240, 164, 48, 0.5);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* 标题 */
.modal-header {
  font-family: 'STKaiti', KaiTi, serif;
  font-size: 1.5rem;
  color: #ffd66b;
  text-align: center;
  margin-bottom: 1rem;
}

/* 输入框 */
.modal-input {
  width: 90%;
  padding: 0.75rem;
  font-size: 1rem;
  border: 1px solid rgba(255, 215, 0, 0.6);
  background: rgba(0, 0, 0, 0.2);
  color: #ffeab4;
  border-radius: 0.5rem;
  resize: none;
  margin-bottom: 1rem;
}

/* 按钮组 */
.modal-actions {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
}

/* 取消按钮 */
.btn-cancel {
  flex: 1;
  padding: 0.5rem;
  background: rgba(255, 255, 255, 0.2);
  color: #ffeab4;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-cancel:hover {
  background: rgba(255, 255, 255, 0.3);
}

/* 发送按钮 */
.btn-send {
  flex: 1;
  padding: 0.5rem;
  background: linear-gradient(45deg, #f0a430, #ffd66b);
  color: #fff;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition:
    transform 0.2s,
    box-shadow 0.2s;
  box-shadow: 0 3px 10px rgba(240, 164, 48, 0.5);
}
.btn-send:hover {
  transform: translateY(-1px);
  box-shadow: 0 5px 14px rgba(240, 164, 48, 0.7);
}

.btn {
  width: 100px;
}
</style>
