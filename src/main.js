import './assets/css/reset.css'

import { createPinia } from 'pinia'
import { createApp } from 'vue'

import App from './App.vue'
import router from './router'

import Particles from '@tsparticles/vue3'
import 'animate.css'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { loadFull } from 'tsparticles'

// import function to register Swiper custom elements
import { register } from 'swiper/element/bundle'
// register Swiper custom elements
register()

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ElementPlus)
app.use(Particles, {
  init: async (engine) => {
    await loadFull(engine) // you can load the full tsParticles library from "tsparticles" if you need it
  },
})
app.mount('#app')
