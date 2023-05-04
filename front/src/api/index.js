import axios from 'axios'
import config from '../config'

const api = axios.create({
    baseURL: config.BACKEND_URL || ''
})

export default api