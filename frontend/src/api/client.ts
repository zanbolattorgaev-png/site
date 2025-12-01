import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export interface Lecture {
  id: number
  title: string
  description: string | null
  content: string
  video_url: string | null
}

export interface Test {
  id: number
  lecture_id: number
  question: string
  options: string[]
  correct_answer: number
}

export interface Result {
  id: number
  lecture_id: number
  user_name: string
  score: number
  total: number
  date: string
}

export interface ResultSubmit {
  name: string
  answers: Record<string, number>
}

export const lecturesApi = {
  getAll: async (): Promise<Lecture[]> => {
    const response = await apiClient.get<Lecture[]>('/api/lectures/')
    return response.data
  },
  
  getById: async (id: number): Promise<Lecture> => {
    const response = await apiClient.get<Lecture>(`/api/lectures/${id}`)
    return response.data
  },
}

export const testsApi = {
  getByLectureId: async (lectureId: number): Promise<Test[]> => {
    const response = await apiClient.get<Test[]>(`/api/tests/${lectureId}`)
    return response.data
  },
  
  submit: async (lectureId: number, data: ResultSubmit): Promise<Result> => {
    const response = await apiClient.post<Result>(
      `/api/tests/${lectureId}/submit`,
      data
    )
    return response.data
  },
}

export const resultsApi = {
  getByLectureId: async (lectureId: number): Promise<Result[]> => {
    const response = await apiClient.get<Result[]>(`/api/results/${lectureId}`)
    return response.data
  },
}

