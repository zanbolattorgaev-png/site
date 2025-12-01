import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { testsApi, Test } from '../api/client'

export default function TestProcess() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [tests, setTests] = useState<Test[]>([])
  const [answers, setAnswers] = useState<Record<string, number>>({})
  const [currentQuestion, setCurrentQuestion] = useState(0)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchTests = async () => {
      if (!id) return

      try {
        setLoading(true)
        const data = await testsApi.getByLectureId(parseInt(id))
        setTests(data)
      } catch (err) {
        setError('Не удалось загрузить тест')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchTests()
  }, [id])

  const handleAnswerSelect = (testId: number, optionIndex: number) => {
    setAnswers({
      ...answers,
      [testId.toString()]: optionIndex,
    })
  }

  const handleNext = () => {
    if (currentQuestion < tests.length - 1) {
      setCurrentQuestion(currentQuestion + 1)
    }
  }

  const handlePrevious = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1)
    }
  }

  const handleSubmit = async () => {
    if (!id) return

    const name = localStorage.getItem(`test_name_${id}`)
    if (!name) {
      navigate(`/lectures/${id}/test/start`)
      return
    }

    try {
      await testsApi.submit(parseInt(id), {
        name,
        answers,
      })
      
      navigate(`/lectures/${id}/test/result`)
    } catch (err) {
      setError('Не удалось отправить ответы')
      console.error(err)
    }
  }

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-12">
        <div className="text-center text-gray-600">Загрузка теста...</div>
      </div>
    )
  }

  if (error || tests.length === 0) {
    return (
      <div className="container mx-auto px-4 py-12">
        <div className="text-center text-red-600">
          {error || 'Тест не найден'}
        </div>
      </div>
    )
  }

  const test = tests[currentQuestion]
  const currentAnswer = answers[test.id.toString()]

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="max-w-3xl mx-auto">
        <div className="bg-white rounded-lg shadow-md p-8">
          <div className="mb-6">
            <div className="flex justify-between items-center mb-2">
              <span className="text-sm text-gray-600">
                Вопрос {currentQuestion + 1} из {tests.length}
              </span>
              <span className="text-sm text-gray-600">
                {Math.round(((currentQuestion + 1) / tests.length) * 100)}%
              </span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className="bg-blue-600 h-2 rounded-full transition-all"
                style={{ width: `${((currentQuestion + 1) / tests.length) * 100}%` }}
              />
            </div>
          </div>

          <h2 className="text-2xl font-bold text-gray-900 mb-6">
            {test.question}
          </h2>

          <div className="space-y-3 mb-8">
            {test.options.map((option, index) => (
              <button
                key={index}
                onClick={() => handleAnswerSelect(test.id, index)}
                className={`w-full text-left p-4 rounded-lg border-2 transition-colors ${
                  currentAnswer === index
                    ? 'border-blue-600 bg-blue-50'
                    : 'border-gray-300 hover:border-gray-400'
                }`}
              >
                <span className="font-semibold mr-2">{String.fromCharCode(65 + index)}.</span>
                {option}
              </button>
            ))}
          </div>

          <div className="flex justify-between">
            <button
              onClick={handlePrevious}
              disabled={currentQuestion === 0}
              className="bg-gray-300 text-gray-700 px-6 py-2 rounded-lg font-semibold hover:bg-gray-400 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              Назад
            </button>

            {currentQuestion < tests.length - 1 ? (
              <button
                onClick={handleNext}
                className="bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-700 transition-colors"
              >
                Следующий
              </button>
            ) : (
              <button
                onClick={handleSubmit}
                className="bg-green-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-green-700 transition-colors"
              >
                Завершить тест
              </button>
            )}
          </div>
        </div>

        <div className="mt-4 text-center text-gray-600">
          Отвечено: {Object.keys(answers).length} из {tests.length}
        </div>
      </div>
    </div>
  )
}

