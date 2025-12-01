import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { lecturesApi, Lecture } from '../api/client'

export default function Lectures() {
  const [lectures, setLectures] = useState<Lecture[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchLectures = async () => {
      try {
        setLoading(true)
        const data = await lecturesApi.getAll()
        setLectures(data)
      } catch (err) {
        setError('Не удалось загрузить лекции')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchLectures()
  }, [])

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-12">
        <div className="text-center text-gray-600">Загрузка...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="container mx-auto px-4 py-12">
        <div className="text-center text-red-600">{error}</div>
      </div>
    )
  }

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="mb-8">
        <h1 className="text-5xl font-extrabold text-gray-900 mb-4 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
          Лекции
        </h1>
        <p className="text-gray-600 text-lg">
          Выберите лекцию для изучения. Каждая лекция включает видео, теорию, практику и тест.
        </p>
      </div>
      
      {lectures.length === 0 ? (
        <div className="bg-gradient-to-br from-yellow-50 to-orange-50 border-2 border-yellow-200 rounded-xl p-8 text-center shadow-lg max-w-2xl mx-auto">
          <div className="text-6xl mb-4">📚</div>
          <p className="text-yellow-800 text-xl font-bold mb-4">Лекции пока не добавлены в базу данных</p>
          <div className="bg-white rounded-lg p-6 text-left text-gray-700 space-y-3">
            <p className="font-semibold">Чтобы добавить лекции, выполните:</p>
            <ol className="list-decimal list-inside space-y-2 ml-2">
              <li>Откройте терминал в папке <code className="bg-gray-100 px-2 py-1 rounded">backend</code></li>
              <li>Запустите: <code className="bg-gray-100 px-2 py-1 rounded">python reset_db.py</code></li>
              <li>Убедитесь, что backend сервер запущен: <code className="bg-gray-100 px-2 py-1 rounded">uvicorn app.main:app --reload</code></li>
              <li>Обновите эту страницу</li>
            </ol>
          </div>
        </div>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {lectures.map((lecture) => (
            <div
              key={lecture.id}
              className="card group cursor-pointer transform hover:scale-105"
            >
              <div className="flex items-center justify-between mb-4">
                <div className="text-4xl opacity-80 group-hover:opacity-100 transition-opacity">
                  {lecture.id === 1 && '🌱'}
                  {lecture.id === 2 && '⚡'}
                  {lecture.id === 3 && '📦'}
                  {lecture.id === 4 && '🎯'}
                  {lecture.id === 5 && '🔄'}
                  {lecture.id === 6 && '🌐'}
                  {lecture.id === 7 && '🎪'}
                  {lecture.id === 8 && '⏱️'}
                  {lecture.id === 9 && '✨'}
                  {lecture.id === 10 && '🛡️'}
                  {!lecture.id && '📚'}
                </div>
                {lecture.video_url && (
                  <span className="bg-red-500 text-white text-xs px-2 py-1 rounded-full">🎥 Видео</span>
                )}
              </div>
              <h2 className="text-xl font-bold text-gray-900 mb-3 group-hover:text-blue-600 transition-colors">
                {lecture.id}. {lecture.title}
              </h2>
              {lecture.description && (
                <p className="text-gray-600 mb-5 line-clamp-2">{lecture.description}</p>
              )}
              <Link
                to={`/lectures/${lecture.id}`}
                className="inline-block w-full text-center bg-gradient-to-r from-blue-600 to-purple-600 text-white px-4 py-3 rounded-lg font-semibold hover:from-blue-700 hover:to-purple-700 transition-all shadow-md hover:shadow-lg"
              >
                Открыть лекцию →
              </Link>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

