import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-16">
      <div className="max-w-5xl mx-auto">
        <div className="text-center mb-16">
          <h1 className="text-6xl md:text-7xl font-extrabold mb-6 bg-gradient-to-r from-blue-600 via-purple-600 to-blue-800 bg-clip-text text-transparent">
            Онлайн-курс по JavaScript
          </h1>
          <p className="text-xl md:text-2xl text-gray-700 mb-10 max-w-3xl mx-auto leading-relaxed">
            Изучите JavaScript с нуля до продвинутого уровня. Практикуйтесь в онлайн-компиляторе
            и проверяйте знания с помощью интерактивных тестов.
          </p>
          <Link
            to="/lectures"
            className="inline-block bg-gradient-to-r from-blue-600 to-purple-600 text-white px-10 py-4 rounded-xl text-lg font-bold hover:from-blue-700 hover:to-purple-700 transition-all shadow-2xl hover:shadow-blue-500/50 transform hover:-translate-y-1 hover:scale-105"
          >
            🚀 Начать обучение
          </Link>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8 mt-20">
          <div className="card transform hover:scale-105 hover:border-blue-300">
            <div className="text-5xl mb-4">📚</div>
            <h3 className="text-2xl font-bold mb-4 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
              Лекции
            </h3>
            <p className="text-gray-600 leading-relaxed">
              Изучайте материал с подробными объяснениями, примерами кода и видеоуроками с YouTube
            </p>
          </div>
          
          <div className="card transform hover:scale-105 hover:border-green-300">
            <div className="text-5xl mb-4">💻</div>
            <h3 className="text-2xl font-bold mb-4 bg-gradient-to-r from-green-600 to-blue-600 bg-clip-text text-transparent">
              Компилятор
            </h3>
            <p className="text-gray-600 leading-relaxed">
              Практикуйтесь прямо в браузере с удобным редактором кода на базе Monaco Editor
            </p>
          </div>
          
          <div className="card transform hover:scale-105 hover:border-purple-300">
            <div className="text-5xl mb-4">✅</div>
            <h3 className="text-2xl font-bold mb-4 bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
              Тесты
            </h3>
            <p className="text-gray-600 leading-relaxed">
              Проверяйте свои знания с помощью интерактивных тестов с множественным выбором
            </p>
          </div>
        </div>

        <div className="mt-20 text-center">
          <div className="inline-block bg-white rounded-2xl shadow-xl p-8 border border-gray-200">
            <h2 className="text-3xl font-bold mb-4 text-gray-800">Что вас ждет?</h2>
            <div className="grid md:grid-cols-2 gap-6 text-left max-w-2xl">
              <div className="flex items-start gap-3">
                <span className="text-2xl">✨</span>
                <div>
                  <h4 className="font-semibold text-gray-800">10 подробных лекций</h4>
                  <p className="text-gray-600 text-sm">От основ до продвинутых тем</p>
                </div>
              </div>
              <div className="flex items-start gap-3">
                <span className="text-2xl">🎥</span>
                <div>
                  <h4 className="font-semibold text-gray-800">Видеоуроки</h4>
                  <p className="text-gray-600 text-sm">Интеграция с YouTube</p>
                </div>
              </div>
              <div className="flex items-start gap-3">
                <span className="text-2xl">🧪</span>
                <div>
                  <h4 className="font-semibold text-gray-800">Практика в браузере</h4>
                  <p className="text-gray-600 text-sm">Встроенный компилятор JavaScript</p>
                </div>
              </div>
              <div className="flex items-start gap-3">
                <span className="text-2xl">📊</span>
                <div>
                  <h4 className="font-semibold text-gray-800">Проверка знаний</h4>
                  <p className="text-gray-600 text-sm">Более 90 вопросов в тестах</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

