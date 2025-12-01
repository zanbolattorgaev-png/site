import { Link, useLocation } from 'react-router-dom'

export default function Navbar() {
  const location = useLocation()
  
  return (
    <nav className="bg-gradient-to-r from-blue-600 via-blue-700 to-purple-600 text-white shadow-xl sticky top-0 z-50">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <Link 
            to="/" 
            className="text-2xl font-bold hover:text-blue-200 transition-colors flex items-center gap-2"
          >
            <span className="text-3xl">📚</span>
            <span>JavaScript Course</span>
          </Link>
          <div className="flex items-center space-x-6">
            <Link
              to="/"
              className={`px-4 py-2 rounded-lg font-medium transition-all ${
                location.pathname === '/' 
                  ? 'bg-white bg-opacity-20 text-white' 
                  : 'hover:bg-white hover:bg-opacity-10'
              }`}
            >
              Главная
            </Link>
            <Link
              to="/lectures"
              className={`px-4 py-2 rounded-lg font-medium transition-all ${
                location.pathname === '/lectures' 
                  ? 'bg-white bg-opacity-20 text-white' 
                  : 'hover:bg-white hover:bg-opacity-10'
              }`}
            >
              Лекции
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
}

