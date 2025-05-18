// http.js
import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000/api/'

export const http = axios.create({
  baseURL: baseURL,
  withCredentials: true,
  timeout: 5000,
})
