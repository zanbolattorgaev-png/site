import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import ReactMarkdown from 'react-markdown'
import { lecturesApi, Lecture } from '../api/client'
import Editor from '../components/Editor'

// Функция для извлечения YouTube video ID из URL
function getYouTubeVideoId(url: string | null): string | null {
  if (!url) return null
  
  // Различные форматы YouTube URL
  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)/,
    /youtube\.com\/.*[?&]v=([^&\n?#]+)/,
  ]
  
  for (const pattern of patterns) {
    const match = url.match(pattern)
    if (match && match[1]) {
      return match[1]
    }
  }
  
  // Если это уже просто ID
  if (/^[a-zA-Z0-9_-]{11}$/.test(url)) {
    return url
  }
  
  return null
}

export default function LectureView() {
  const { id } = useParams<{ id: string }>()
  const [lecture, setLecture] = useState<Lecture | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [showEditor, setShowEditor] = useState(false)
  
  const videoId = lecture?.video_url ? getYouTubeVideoId(lecture.video_url) : null

  useEffect(() => {
    const fetchLecture = async () => {
      if (!id) return
      
      try {
        setLoading(true)
        const data = await lecturesApi.getById(parseInt(id))
        setLecture(data)
      } catch (err) {
        setError('Не удалось загрузить лекцию')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchLecture()
  }, [id])

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-12">
        <div className="text-center text-gray-600">Загрузка...</div>
      </div>
    )
  }

  if (error || !lecture) {
    return (
      <div className="container mx-auto px-4 py-12">
        <div className="text-center text-red-600">{error || 'Лекция не найдена'}</div>
        <Link to="/lectures" className="block mt-4 text-blue-600 hover:underline">
          Вернуться к списку лекций
        </Link>
      </div>
    )
  }

  return (
    <div className="container mx-auto px-4 py-12 max-w-5xl">
      <Link
        to="/lectures"
        className="inline-flex items-center gap-2 text-blue-600 hover:text-blue-700 font-medium mb-6 transition-colors hover:gap-3"
      >
        <span>←</span>
        <span>Назад к лекциям</span>
      </Link>

      <div className="mb-8">
        <h1 className="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
          {lecture.title}
        </h1>
        
        {lecture.description && (
          <p className="text-xl text-gray-600 mb-6 leading-relaxed">{lecture.description}</p>
        )}
      </div>

      {videoId && (
        <div className="mb-8 bg-white rounded-xl shadow-xl p-4 border border-gray-200">
          <h3 className="text-lg font-semibold mb-3 text-gray-800 flex items-center gap-2">
            <span>🎥</span>
            Видеоурок
          </h3>
          <div className="relative w-full rounded-lg overflow-hidden" style={{ paddingBottom: '56.25%' }}>
            <iframe
              className="absolute top-0 left-0 w-full h-full"
              src={`https://www.youtube.com/embed/${videoId}`}
              title="YouTube video player"
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            />
          </div>
        </div>
      )}

      <div className="card mb-6">
        <div className="prose prose-lg max-w-none prose-headings:text-gray-900 prose-code:bg-gray-100 prose-code:px-2 prose-code:py-1 prose-code:rounded prose-pre:bg-gray-900">
          <ReactMarkdown>{lecture.content}</ReactMarkdown>
        </div>
      </div>

      <div className="sticky top-20 z-10 bg-gray-50 -mx-4 px-4 py-4 mb-6 border-b-2 border-gray-200 shadow-sm">
        <div className="flex flex-wrap gap-4 justify-center">
          <button
            onClick={() => setShowEditor(!showEditor)}
            className={`px-8 py-4 rounded-xl font-bold text-lg transition-all shadow-xl hover:shadow-2xl transform hover:-translate-y-1 ${
              showEditor 
                ? 'bg-gradient-to-r from-gray-600 to-gray-700 text-white hover:from-gray-700 hover:to-gray-800' 
                : 'bg-gradient-to-r from-green-600 to-emerald-600 text-white hover:from-green-700 hover:to-emerald-700'
            }`}
          >
            {showEditor ? '✖️ Скрыть компилятор' : '💻 Открыть компилятор'}
          </button>
          
          <Link
            to={`/lectures/${id}/test/start`}
            className="inline-block bg-gradient-to-r from-purple-600 to-pink-600 text-white px-8 py-4 rounded-xl font-bold text-lg hover:from-purple-700 hover:to-pink-700 transition-all shadow-xl hover:shadow-2xl transform hover:-translate-y-1"
          >
            📝 Пройти тест
          </Link>
        </div>
      </div>

      {showEditor && (
        <div className="bg-gradient-to-br from-white to-blue-50 rounded-xl shadow-2xl p-8 border-2 border-blue-200 mb-6">
          <Editor initialCode="// Начните писать код здесь\n// Попробуйте изменить код ниже:\n\nconsole.log('Привет, мир!');\n\nconst name = 'JavaScript';\nconsole.log('Изучаю', name);\n\n// Попробуйте создать функцию:\nfunction greet(name) {\n    return `Привет, ${name}!`;\n}\n\nconsole.log(greet('Друг'));" />
        </div>
      )}
    </div>
  )
}

