// http.js
import axios from 'axios'

// const baseURL = 'http://127.0.0.1:8000/api/celebration/'
const baseURL = 'https://youtholapi.bulbul559.cn/api/celebration/'

export const http = axios.create({
  baseURL: baseURL,
  withCredentials: true,
  timeout: 5000,
})
