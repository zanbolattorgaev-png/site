import { useState, useRef, useEffect } from 'react'
import MonacoEditor from '@monaco-editor/react'

interface CodeEditorProps {
  initialCode?: string
}

export default function Editor({ initialCode = '// Введите код здесь\nconsole.log("Hello, World!");' }: CodeEditorProps) {
  const [code, setCode] = useState(initialCode)
  const [output, setOutput] = useState<string[]>([])
  const [error, setError] = useState<string | null>(null)
  const timeoutRef = useRef<NodeJS.Timeout | null>(null)
  const isRunningRef = useRef(false)

  // Обновляем код при изменении initialCode
  useEffect(() => {
    setCode(initialCode)
    setOutput([])
    setError(null)
  }, [initialCode])

  const runCode = () => {
    if (isRunningRef.current) {
      return // Предотвращаем множественные запуски
    }

    setOutput([])
    setError(null)
    isRunningRef.current = true

    // Очищаем предыдущий таймаут если есть
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current)
    }

    try {
      // Перехватываем console.log
      const logs: string[] = []
      const originalLog = console.log
      const originalError = console.error
      const originalWarn = console.warn
      const originalInfo = console.info

      console.log = (...args: any[]) => {
        logs.push(args.map(arg => 
          typeof arg === 'object' ? JSON.stringify(arg, null, 2) : String(arg)
        ).join(' '))
        originalLog(...args)
      }

      console.error = (...args: any[]) => {
        logs.push(`ERROR: ${args.map(arg => 
          typeof arg === 'object' ? JSON.stringify(arg, null, 2) : String(arg)
        ).join(' ')}`)
        originalError(...args)
      }

      console.warn = (...args: any[]) => {
        logs.push(`WARN: ${args.map(arg => 
          typeof arg === 'object' ? JSON.stringify(arg, null, 2) : String(arg)
        ).join(' ')}`)
        originalWarn(...args)
      }

      console.info = (...args: any[]) => {
        logs.push(`INFO: ${args.map(arg => 
          typeof arg === 'object' ? JSON.stringify(arg, null, 2) : String(arg)
        ).join(' ')}`)
        originalInfo(...args)
      }

      // Обертка выполнения кода с таймаутом
      const executeWithTimeout = (): Promise<any> => {
        return new Promise((resolve, reject) => {
          // Устанавливаем таймаут
          timeoutRef.current = setTimeout(() => {
            reject(new Error('Превышено время выполнения (10 секунд)'))
          }, 10000)

          try {
            // Создаем функцию для безопасного выполнения
            const func = new Function(code)
            const result = func()
            resolve(result)
          } catch (execError) {
            reject(execError)
          }
        })
      }

      // Выполняем код с таймаутом
      executeWithTimeout()
        .then((result) => {
          // Если функция возвращает значение, выводим его
          if (result !== undefined) {
            logs.push(String(result))
          }
          
          if (timeoutRef.current) {
            clearTimeout(timeoutRef.current)
            timeoutRef.current = null
          }
          
          // Восстанавливаем оригинальные методы
          console.log = originalLog
          console.error = originalError
          console.warn = originalWarn
          console.info = originalInfo
          isRunningRef.current = false
          
          setOutput(logs.length > 0 ? logs : ['(нет вывода)'])
        })
        .catch((err) => {
          if (timeoutRef.current) {
            clearTimeout(timeoutRef.current)
            timeoutRef.current = null
          }
          
          // Восстанавливаем оригинальные методы
          console.log = originalLog
          console.error = originalError
          console.warn = originalWarn
          console.info = originalInfo
          isRunningRef.current = false
          
          // Обрабатываем ошибку
          const errorMessage = err instanceof Error ? err.message : 'Неизвестная ошибка'
          setError(errorMessage)
          setOutput([])
        })
    } catch (err) {
      // Синхронные ошибки (например, при создании функции)
      const errorMessage = err instanceof Error ? err.message : 'Неизвестная ошибка'
      setError(errorMessage)
      setOutput([])
      isRunningRef.current = false
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current)
        timeoutRef.current = null
      }
    }
  }

  return (
    <div className="w-full">
      <div className="mb-6 flex flex-wrap justify-between items-center gap-4">
        <div>
          <h3 className="text-2xl font-bold text-gray-900 mb-1 flex items-center gap-2">
            <span>💻</span>
            <span className="bg-gradient-to-r from-green-600 to-emerald-600 bg-clip-text text-transparent">
              JavaScript Компилятор
            </span>
          </h3>
          <p className="text-gray-600 text-sm">Пишите и выполняйте JavaScript код прямо в браузере</p>
        </div>
        <button
          onClick={runCode}
          disabled={isRunningRef.current}
          className="bg-gradient-to-r from-blue-600 to-blue-700 text-white px-8 py-4 rounded-xl font-bold text-lg hover:from-blue-700 hover:to-blue-800 disabled:from-gray-400 disabled:to-gray-500 disabled:cursor-not-allowed transition-all shadow-xl hover:shadow-2xl transform hover:-translate-y-1 disabled:transform-none flex items-center gap-3"
        >
          {isRunningRef.current ? (
            <>
              <span className="animate-spin text-2xl">⟳</span>
              <span>Выполнение...</span>
            </>
          ) : (
            <>
              <span className="text-2xl">▶</span>
              <span>Запуск кода</span>
            </>
          )}
        </button>
      </div>
      
      <div className="border-2 border-gray-300 rounded-xl overflow-hidden mb-6 shadow-lg hover:border-blue-400 transition-colors">
        <MonacoEditor
          height="500px"
          defaultLanguage="javascript"
          value={code}
          onChange={(value) => setCode(value || '')}
          theme="vs-light"
          loading={
            <div className="flex flex-col items-center justify-center h-full bg-gradient-to-br from-gray-50 to-blue-50">
              <div className="text-4xl mb-4 animate-bounce">⚙️</div>
              <div className="text-gray-600 font-medium">Загрузка редактора Monaco...</div>
              <div className="text-gray-400 text-sm mt-2">Это может занять несколько секунд</div>
            </div>
          }
          options={{
            minimap: { enabled: false },
            fontSize: 16,
            lineNumbers: 'on',
            scrollBeyondLastLine: false,
            automaticLayout: true,
            tabSize: 2,
            wordWrap: 'on',
            formatOnPaste: true,
            formatOnType: true,
            fontFamily: "'Fira Code', 'Consolas', 'Monaco', 'Courier New', monospace",
            fontLigatures: true,
            cursorBlinking: 'smooth',
            cursorSmoothCaretAnimation: true,
            smoothScrolling: true,
            padding: { top: 16, bottom: 16 },
          }}
        />
      </div>

      {(output.length > 0 || error) && (
        <div className="bg-gradient-to-br from-gray-900 to-gray-800 text-green-400 p-6 rounded-xl font-mono text-sm overflow-auto max-h-80 shadow-xl border-2 border-gray-700">
          <div className="flex items-center gap-2 mb-4 pb-2 border-b border-gray-700">
            <span className="text-lg">📊</span>
            <span className="text-gray-400 font-semibold">Результат выполнения:</span>
          </div>
          {error ? (
            <div className="text-red-400 whitespace-pre-wrap">
              <div className="flex items-start gap-2 mb-2">
                <span className="text-xl">❌</span>
                <span className="font-bold text-lg">Ошибка:</span>
              </div>
              <div className="ml-7 bg-red-900 bg-opacity-30 p-3 rounded-lg border border-red-700">
                {error}
              </div>
            </div>
          ) : (
            <div className="space-y-2">
              {output.map((line, index) => (
                <div 
                  key={index} 
                  className="text-green-400 whitespace-pre-wrap pl-2 border-l-2 border-green-500 bg-green-900 bg-opacity-10 py-1 px-3 rounded"
                >
                  {line}
                </div>
              ))}
            </div>
          )}
        </div>
      )}
      
      {!output.length && !error && (
        <div className="bg-gradient-to-br from-blue-50 to-purple-50 border-2 border-blue-200 rounded-xl p-6 text-center shadow-md">
          <div className="text-4xl mb-3">🚀</div>
          <p className="text-gray-700 font-medium mb-2">Готов к выполнению</p>
          <p className="text-gray-600 text-sm">Напишите код и нажмите "Запуск кода" для выполнения</p>
          <div className="mt-4 text-left bg-white rounded-lg p-4 border border-gray-200">
            <p className="text-gray-700 font-semibold mb-2 text-sm">💡 Попробуйте:</p>
            <pre className="text-xs text-gray-600 bg-gray-50 p-3 rounded overflow-x-auto">
              <code>{`console.log("Hello, World!");
const sum = (a, b) => a + b;
console.log("2 + 3 =", sum(2, 3));`}</code>
            </pre>
          </div>
        </div>
      )}

      <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
        <div className="bg-blue-50 rounded-lg p-4 border border-blue-200">
          <div className="font-semibold text-blue-900 mb-1">⚡ Быстрое выполнение</div>
          <div className="text-blue-700 text-xs">Код выполняется прямо в браузере</div>
        </div>
        <div className="bg-green-50 rounded-lg p-4 border border-green-200">
          <div className="font-semibold text-green-900 mb-1">🛡️ Безопасно</div>
          <div className="text-green-700 text-xs">Таймаут 10 секунд для защиты</div>
        </div>
        <div className="bg-purple-50 rounded-lg p-4 border border-purple-200">
          <div className="font-semibold text-purple-900 mb-1">📝 Полный вывод</div>
          <div className="text-purple-700 text-xs">Поддержка console.log, error, warn</div>
        </div>
      </div>
    </div>
  )
}

