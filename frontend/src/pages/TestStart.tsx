import { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'

export default function TestStart() {
  const { id } = useParams<{ id: string }>()
  const [name, setName] = useState('')
  const navigate = useNavigate()

  const handleStart = (e: React.FormEvent) => {
    e.preventDefault()
    if (name.trim()) {
      // Сохраняем имя в localStorage для использования после теста
      localStorage.setItem(`test_name_${id}`, name.trim())
      navigate(`/lectures/${id}/test`)
    }
  }

  return (
    <div className="container mx-auto px-4 py-16 min-h-screen flex items-center justify-center">
      <div className="max-w-md w-full card">
        <div className="text-center mb-8">
          <div className="text-6xl mb-4">📝</div>
          <h1 className="text-4xl font-extrabold text-gray-900 mb-4 bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
            Начать тест
          </h1>
          <p className="text-gray-600 text-lg">
            Введите ваше имя для начала теста
          </p>
        </div>
        
        <form onSubmit={handleStart} className="space-y-6">
          <div>
            <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-2">
              Ваше имя
            </label>
            <input
              id="name"
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Например: Иван"
              className="w-full px-4 py-4 border-2 border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all text-lg"
              required
              autoFocus
            />
          </div>
          
          <button
            type="submit"
            className="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white px-6 py-4 rounded-xl font-bold text-lg hover:from-purple-700 hover:to-pink-700 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
          >
            🚀 Начать тест
          </button>
        </form>
      </div>
    </div>
  )
}

