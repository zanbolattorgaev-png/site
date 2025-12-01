import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { resultsApi, Result } from '../api/client'

export default function TestResult() {
  const { id } = useParams<{ id: string }>()
  const [result, setResult] = useState<Result | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchLastResult = async () => {
      if (!id) return

      try {
        setLoading(true)
        const results = await resultsApi.getByLectureId(parseInt(id))
        // Получаем последний результат (самый свежий)
        if (results.length > 0) {
          setResult(results[0])
        }
      } catch (err) {
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchLastResult()
  }, [id])

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-12">
        <div className="text-center text-gray-600">Загрузка результата...</div>
      </div>
    )
  }

  if (!result) {
    return (
      <div className="container mx-auto px-4 py-12">
        <div className="text-center text-red-600">Результат не найден</div>
        <Link to="/lectures" className="block mt-4 text-blue-600 hover:underline">
          Вернуться к лекциям
        </Link>
      </div>
    )
  }

  const percentage = Math.round((result.score / result.total) * 100)
  const isExcellent = percentage >= 90
  const isGood = percentage >= 70 && percentage < 90
  const isFair = percentage >= 50 && percentage < 70

  return (
    <div className="container mx-auto px-4 py-16 min-h-screen flex items-center justify-center">
      <div className="max-w-2xl w-full">
        <div className="card text-center">
          <div className="mb-8">
            {isExcellent && <div className="text-7xl mb-4">🎉</div>}
            {isGood && <div className="text-7xl mb-4">👍</div>}
            {isFair && <div className="text-7xl mb-4">📚</div>}
            {!isExcellent && !isGood && !isFair && <div className="text-7xl mb-4">💪</div>}
            <h1 className="text-4xl font-extrabold text-gray-900 mb-2 bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
              Результаты теста
            </h1>
          </div>

          <div className="mb-8">
            <div className={`text-7xl font-extrabold mb-4 ${
              isExcellent ? 'text-green-500' :
              isGood ? 'text-blue-500' :
              isFair ? 'text-yellow-500' :
              'text-orange-500'
            }`}>
              {percentage}%
            </div>
            <div className="text-2xl text-gray-700 font-semibold mb-2">
              {result.score} из {result.total} правильных ответов
            </div>
            {isExcellent && <p className="text-green-600 font-medium">Отлично! 🌟</p>}
            {isGood && <p className="text-blue-600 font-medium">Хорошо! 👏</p>}
            {isFair && <p className="text-yellow-600 font-medium">Неплохо! Продолжайте! 💪</p>}
            {!isExcellent && !isGood && !isFair && <p className="text-orange-600 font-medium">Попробуйте еще раз! 📖</p>}
          </div>

          <div className="bg-gradient-to-br from-gray-50 to-blue-50 rounded-xl p-6 mb-8 border-2 border-gray-200">
            <div className="grid grid-cols-2 gap-6 text-left">
              <div>
                <span className="text-gray-600 text-sm font-medium block mb-1">Имя:</span>
                <div className="font-bold text-gray-900 text-lg">{result.user_name}</div>
              </div>
              <div>
                <span className="text-gray-600 text-sm font-medium block mb-1">Дата:</span>
                <div className="font-bold text-gray-900 text-lg">
                  {new Date(result.date).toLocaleDateString('ru-RU', {
                    day: 'numeric',
                    month: 'long',
                    year: 'numeric'
                  })}
                </div>
              </div>
            </div>
          </div>

          <div className="flex flex-wrap justify-center gap-4">
            <Link
              to={`/lectures/${id}`}
              className="inline-block bg-gradient-to-r from-blue-600 to-blue-700 text-white px-8 py-4 rounded-xl font-bold hover:from-blue-700 hover:to-blue-800 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
            >
              ← Вернуться к лекции
            </Link>
            
            <Link
              to={`/lectures/${id}/test/start`}
              className="inline-block bg-gradient-to-r from-green-600 to-emerald-600 text-white px-8 py-4 rounded-xl font-bold hover:from-green-700 hover:to-emerald-700 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
            >
              🔄 Пройти тест снова
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}

