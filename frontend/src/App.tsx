import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import Lectures from './pages/Lectures'
import LectureView from './pages/LectureView'
import TestStart from './pages/TestStart'
import TestProcess from './pages/TestProcess'
import TestResult from './pages/TestResult'

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/lectures" element={<Lectures />} />
          <Route path="/lectures/:id" element={<LectureView />} />
          <Route path="/lectures/:id/test/start" element={<TestStart />} />
          <Route path="/lectures/:id/test" element={<TestProcess />} />
          <Route path="/lectures/:id/test/result" element={<TestResult />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App

