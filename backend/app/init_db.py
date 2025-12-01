"""
Скрипт для инициализации базы данных с примерами данных
Запуск: python -m app.init_db
"""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import async_session_maker
from app.models import Lecture, Test


async def init_data():
    """Добавление примеров лекций и тестов"""
    async with async_session_maker() as session:
        # Проверяем, есть ли уже лекции
        from sqlalchemy import select
        result = await session.execute(select(Lecture))
        existing = result.scalars().first()
        
        if existing:
            print("⚠️  База данных уже содержит данные. Пропускаем инициализацию.")
            print("💡 Для пересоздания запустите: python reset_db.py")
            return
        
        # Лекция 1: Введение в JavaScript
        lecture1 = Lecture(
            title="Введение в JavaScript",
            description="Основы языка JavaScript: переменные, типы данных, операторы",
            video_url="https://www.youtube.com/watch?v=W6NZfCO5SIk",
            content="""# Введение в JavaScript

## Что такое JavaScript?

JavaScript — это язык программирования, который позволяет создавать интерактивные веб-страницы.

## Переменные

В JavaScript переменные можно объявлять тремя способами:

- `var` — устаревший способ (не рекомендуется)
- `let` — для переменных, которые могут изменяться
- `const` — для констант

### Примеры:

\`\`\`javascript
let name = "JavaScript";
const version = 2023;
var oldWay = "не рекомендуется";
\`\`\`

## Типы данных

JavaScript поддерживает несколько типов данных:

1. **String** (строка): `"Привет, мир!"`
2. **Number** (число): `42`, `3.14`
3. **Boolean** (логический): `true`, `false`
4. **Object** (объект): `{ name: "John" }`
5. **Array** (массив): `[1, 2, 3]`

## Пример кода

\`\`\`javascript
// Объявление переменных
let userName = "Алексей";
const age = 25;

// Вывод в консоль
console.log("Имя:", userName);
console.log("Возраст:", age);

// Массив
const fruits = ["яблоко", "банан", "апельсин"];
console.log("Фрукты:", fruits);
\`\`\`

## Операторы

JavaScript поддерживает различные операторы:

- Арифметические: `+`, `-`, `*`, `/`, `%`
- Сравнения: `==`, `===`, `!=`, `!==`, `>`, `<`
- Логические: `&&`, `||`, `!`

Продолжайте изучение в следующей лекции!"""
        )
        
        # Лекция 2: Функции
        lecture2 = Lecture(
            title="Функции в JavaScript",
            description="Изучите, как создавать и использовать функции в JavaScript",
            video_url="https://www.youtube.com/watch?v=N8ap4k_1QEQ",
            content="""# Функции в JavaScript

## Что такое функция?

Функция — это блок кода, который можно вызывать многократно.

## Объявление функции

### Function Declaration

\`\`\`javascript
function greet(name) {
    return "Привет, " + name + "!";
}
\`\`\`

### Arrow Function (Стрелочная функция)

\`\`\`javascript
const greet = (name) => {
    return "Привет, " + name + "!";
};
\`\`\`

Или более короткая форма:

\`\`\`javascript
const greet = name => "Привет, " + name + "!";
\`\`\`

## Примеры функций

\`\`\`javascript
// Функция сложения
function add(a, b) {
    return a + b;
}

// Стрелочная функция умножения
const multiply = (a, b) => a * b;

// Вызов функций
console.log(add(5, 3));        // 8
console.log(multiply(4, 7));   // 28
\`\`\`

## Параметры по умолчанию

\`\`\`javascript
function greet(name = "Гость") {
    return "Привет, " + name + "!";
}

console.log(greet());           // Привет, Гость!
console.log(greet("Анна"));    // Привет, Анна!
\`\`\`

## Callback функции

Функции можно передавать как аргументы:

\`\`\`javascript
function calculate(a, b, operation) {
    return operation(a, b);
}

const result = calculate(10, 5, (x, y) => x * y);
console.log(result); // 50
\`\`\`

Практикуйтесь в компиляторе!"""
        )

        # Лекция 3: Массивы
        lecture3 = Lecture(
            title="Массивы в JavaScript",
            description="Работа с массивами: методы, итерация, преобразование",
            video_url="https://www.youtube.com/watch?v=ZRdOb4yR0kk",
            content="""# Массивы в JavaScript

## Что такое массив?

Массив — это упорядоченная коллекция элементов.

## Создание массива

\`\`\`javascript
const fruits = ["яблоко", "банан", "апельсин"];
const numbers = [1, 2, 3, 4, 5];
const mixed = [1, "строка", true, null];
\`\`\`

## Доступ к элементам

\`\`\`javascript
const fruits = ["яблоко", "банан", "апельсин"];
console.log(fruits[0]);  // яблоко
console.log(fruits[1]);  // банан
\`\`\`

## Методы массивов

### push() и pop()

\`\`\`javascript
const arr = [1, 2, 3];
arr.push(4);        // [1, 2, 3, 4]
arr.pop();          // [1, 2, 3]
\`\`\`

### map()

\`\`\`javascript
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2);
console.log(doubled); // [2, 4, 6]
\`\`\`

### filter()

\`\`\`javascript
const numbers = [1, 2, 3, 4, 5];
const even = numbers.filter(n => n % 2 === 0);
console.log(even); // [2, 4]
\`\`\`

### forEach()

\`\`\`javascript
const fruits = ["яблоко", "банан", "апельсин"];
fruits.forEach(fruit => console.log(fruit));
\`\`\`

Изучайте дальше!"""
        )

        # Лекция 4: Объекты
        lecture4 = Lecture(
            title="Объекты в JavaScript",
            description="Работа с объектами: создание, свойства, методы",
            video_url="https://www.youtube.com/watch?v=PFmuCDHHpwk",
            content="""# Объекты в JavaScript

## Что такое объект?

Объект — это коллекция пар ключ-значение.

## Создание объекта

\`\`\`javascript
const person = {
    name: "Алексей",
    age: 25,
    city: "Москва"
};
\`\`\`

## Доступ к свойствам

\`\`\`javascript
const person = { name: "Алексей", age: 25 };

// Точечная нотация
console.log(person.name);  // Алексей

// Квадратные скобки
console.log(person["age"]); // 25
\`\`\`

## Методы объекта

\`\`\`javascript
const person = {
    name: "Алексей",
    greet: function() {
        return "Привет, я " + this.name;
    }
};

console.log(person.greet()); // Привет, я Алексей
\`\`\`

## Современный синтаксис

\`\`\`javascript
const person = {
    name: "Алексей",
    greet() {
        return `Привет, я ${this.name}`;
    }
};
\`\`\`

## Деструктуризация

\`\`\`javascript
const person = { name: "Алексей", age: 25 };
const { name, age } = person;
console.log(name, age); // Алексей 25
\`\`\`

Продолжайте практиковаться!"""
        )

        # Лекция 5: Условия и циклы
        lecture5 = Lecture(
            title="Условия и циклы",
            description="Условные операторы if/else, switch и циклы for/while",
            video_url="https://www.youtube.com/watch?v=s9wW2PpJsmQ",
            content="""# Условия и циклы

## Условные операторы

### if/else

\`\`\`javascript
const age = 18;

if (age >= 18) {
    console.log("Совершеннолетний");
} else {
    console.log("Несовершеннолетний");
}
\`\`\`

### switch

\`\`\`javascript
const day = "понедельник";

switch(day) {
    case "понедельник":
        console.log("Начало недели");
        break;
    case "пятница":
        console.log("Конец недели");
        break;
    default:
        console.log("Обычный день");
}
\`\`\`

## Циклы

### for

\`\`\`javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
\`\`\`

### while

\`\`\`javascript
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}
\`\`\`

### for...of (для массивов)

\`\`\`javascript
const fruits = ["яблоко", "банан", "апельсин"];
for (const fruit of fruits) {
    console.log(fruit);
}
\`\`\`

### for...in (для объектов)

\`\`\`javascript
const person = { name: "Алексей", age: 25 };
for (const key in person) {
    console.log(key, person[key]);
}
\`\`\`

Отличная работа!"""
        )

        # Лекция 6: DOM
        lecture6 = Lecture(
            title="Работа с DOM",
            description="Манипуляции с элементами HTML через JavaScript",
            video_url="https://www.youtube.com/watch?v=0ik6X4DJKCc",
            content="""# Работа с DOM

## Что такое DOM?

DOM (Document Object Model) — это представление HTML-документа в виде дерева объектов.

## Получение элементов

\`\`\`javascript
// По ID
const element = document.getElementById("myId");

// По классу
const elements = document.getElementsByClassName("myClass");

// Современный способ
const element = document.querySelector("#myId");
const elements = document.querySelectorAll(".myClass");
\`\`\`

## Изменение содержимого

\`\`\`javascript
const element = document.querySelector("#myId");
element.textContent = "Новый текст";
element.innerHTML = "<strong>Жирный текст</strong>";
\`\`\`

## Изменение стилей

\`\`\`javascript
const element = document.querySelector("#myId");
element.style.color = "red";
element.style.fontSize = "20px";
\`\`\`

## Добавление классов

\`\`\`javascript
const element = document.querySelector("#myId");
element.classList.add("active");
element.classList.remove("inactive");
element.classList.toggle("visible");
\`\`\`

## Создание элементов

\`\`\`javascript
const newDiv = document.createElement("div");
newDiv.textContent = "Новый элемент";
document.body.appendChild(newDiv);
\`\`\`

Практикуйтесь в браузере!"""
        )

        # Лекция 7: События
        lecture7 = Lecture(
            title="События в JavaScript",
            description="Обработка событий: клики, наведение, формы",
            video_url="https://www.youtube.com/watch?v=XFT7iJXyilQ",
            content="""# События в JavaScript

## Что такое события?

События — это действия пользователя (клик, наведение, ввод текста и т.д.).

## Обработчик событий

### addEventListener

\`\`\`javascript
const button = document.querySelector("#myButton");
button.addEventListener("click", function() {
    console.log("Кнопка нажата!");
});
\`\`\`

## Типы событий

### Клик

\`\`\`javascript
button.addEventListener("click", () => {
    console.log("Клик!");
});
\`\`\`

### Наведение мыши

\`\`\`javascript
element.addEventListener("mouseenter", () => {
    console.log("Мышь над элементом");
});

element.addEventListener("mouseleave", () => {
    console.log("Мышь покинула элемент");
});
\`\`\`

### Ввод текста

\`\`\`javascript
const input = document.querySelector("#myInput");
input.addEventListener("input", (e) => {
    console.log("Введен текст:", e.target.value);
});
\`\`\`

### Отправка формы

\`\`\`javascript
const form = document.querySelector("#myForm");
form.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log("Форма отправлена!");
});
\`\`\`

## Объект события

\`\`\`javascript
button.addEventListener("click", (event) => {
    console.log("Тип события:", event.type);
    console.log("Целевой элемент:", event.target);
});
\`\`\`

Продолжайте изучение!"""
        )

        # Лекция 8: Асинхронность
        lecture8 = Lecture(
            title="Асинхронный JavaScript",
            description="Promises, async/await, обработка асинхронных операций",
            video_url="https://www.youtube.com/watch?v=ZcQyJ-gxke0",
            content="""# Асинхронный JavaScript

## Что такое асинхронность?

Асинхронность позволяет выполнять операции без блокировки основного потока.

## Promises

### Создание Promise

\`\`\`javascript
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Успех!");
    }, 1000);
});
\`\`\`

### Использование Promise

\`\`\`javascript
promise
    .then(result => console.log(result))
    .catch(error => console.error(error));
\`\`\`

## async/await

### Async функция

\`\`\`javascript
async function fetchData() {
    const response = await fetch("https://api.example.com/data");
    const data = await response.json();
    return data;
}
\`\`\`

### Обработка ошибок

\`\`\`javascript
async function fetchData() {
    try {
        const response = await fetch("https://api.example.com/data");
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Ошибка:", error);
    }
}
\`\`\`

## fetch API

\`\`\`javascript
fetch("https://api.example.com/data")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
\`\`\`

Используйте async/await для удобства!"""
        )

        # Лекция 9: ES6+ возможности
        lecture9 = Lecture(
            title="Современный JavaScript (ES6+)",
            description="Новые возможности ES6+: стрелочные функции, деструктуризация, модули",
            video_url="https://www.youtube.com/watch?v=NCwa_xi0Uuc",
            content="""# Современный JavaScript (ES6+)

## Стрелочные функции

\`\`\`javascript
// Обычная функция
function add(a, b) {
    return a + b;
}

// Стрелочная функция
const add = (a, b) => a + b;
\`\`\`

## Деструктуризация

### Массивы

\`\`\`javascript
const arr = [1, 2, 3];
const [first, second] = arr;
console.log(first, second); // 1 2
\`\`\`

### Объекты

\`\`\`javascript
const person = { name: "Алексей", age: 25 };
const { name, age } = person;
console.log(name, age); // Алексей 25
\`\`\`

## Шаблонные строки

\`\`\`javascript
const name = "Алексей";
const greeting = `Привет, ${name}!`;
console.log(greeting); // Привет, Алексей!
\`\`\`

## Spread оператор

\`\`\`javascript
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];
console.log(arr2); // [1, 2, 3, 4, 5]
\`\`\`

## Модули

### export

\`\`\`javascript
// math.js
export function add(a, b) {
    return a + b;
}
\`\`\`

### import

\`\`\`javascript
// main.js
import { add } from './math.js';
console.log(add(2, 3)); // 5
\`\`\`

Отличный прогресс!"""
        )

        # Лекция 10: Обработка ошибок
        lecture10 = Lecture(
            title="Обработка ошибок",
            description="Try/catch, throw, правильная обработка исключений",
            video_url="https://www.youtube.com/watch?v=yeaMdTPN5Zk",
            content="""# Обработка ошибок

## Try/Catch

### Базовый синтаксис

\`\`\`javascript
try {
    // Код, который может выбросить ошибку
    const result = riskyOperation();
} catch (error) {
    // Обработка ошибки
    console.error("Произошла ошибка:", error.message);
}
\`\`\`

### Finally

\`\`\`javascript
try {
    // Код
} catch (error) {
    // Обработка ошибки
} finally {
    // Выполнится всегда
    console.log("Завершение работы");
}
\`\`\`

## Throw

### Выброс ошибки

\`\`\`javascript
function divide(a, b) {
    if (b === 0) {
        throw new Error("Деление на ноль!");
    }
    return a / b;
}
\`\`\`

## Типы ошибок

### Error

\`\`\`javascript
try {
    // Код
} catch (error) {
    if (error instanceof TypeError) {
        console.log("Ошибка типа");
    } else if (error instanceof ReferenceError) {
        console.log("Ошибка ссылки");
    } else {
        console.log("Другая ошибка");
    }
}
\`\`\`

## Пользовательские ошибки

\`\`\`javascript
class CustomError extends Error {
    constructor(message) {
        super(message);
        this.name = "CustomError";
    }
}

throw new CustomError("Моя ошибка!");
\`\`\`

Всегда обрабатывайте ошибки правильно!"""
        )
        
        # Добавляем все лекции
        session.add_all([lecture1, lecture2, lecture3, lecture4, lecture5, lecture6, lecture7, lecture8, lecture9, lecture10])
        await session.flush()  # Получаем ID лекций
        
        # Тесты для лекции 1 (10 вопросов)
        tests1 = [
            Test(lecture_id=lecture1.id, question="Какой способ объявления переменных является устаревшим?", options=["let", "var", "const", "function"], correct_answer=1),
            Test(lecture_id=lecture1.id, question="Какой тип данных используется для хранения логических значений?", options=["String", "Number", "Boolean", "Object"], correct_answer=2),
            Test(lecture_id=lecture1.id, question="Что выведет console.log(5 + 3)?", options=["53", "8", "undefined", "error"], correct_answer=1),
            Test(lecture_id=lecture1.id, question="Как объявляется константа в JavaScript?", options=["var name = value", "let name = value", "const name = value", "constant name = value"], correct_answer=2),
            Test(lecture_id=lecture1.id, question="Что такое typeof 'строка'?", options=["string", "String", "object", "text"], correct_answer=0),
            Test(lecture_id=lecture1.id, question="Какой оператор используется для строгого равенства?", options=["==", "===", "=", "!="], correct_answer=1),
            Test(lecture_id=lecture1.id, question="Что вернет выражение: '5' + 3?", options=["8", "53", "error", "undefined"], correct_answer=1),
            Test(lecture_id=lecture1.id, question="Как получить длину строки?", options=["str.length()", "str.length", "str.size", "len(str)"], correct_answer=1),
            Test(lecture_id=lecture1.id, question="Что такое NaN?", options=["Not a Number", "Null and Nothing", "New Array Number", "No Available Number"], correct_answer=0),
            Test(lecture_id=lecture1.id, question="Какой оператор возвращает остаток от деления?", options=["/", "%", "//", "mod"], correct_answer=1),
        ]
        
        # Тесты для лекции 2 (10 вопросов)
        tests2 = [
            Test(lecture_id=lecture2.id, question="Как объявляется стрелочная функция?", options=["function name() {}", "const name = () => {}", "var name = function() {}", "name() => {}"], correct_answer=1),
            Test(lecture_id=lecture2.id, question="Что вернет функция: const add = (a, b) => a + b; add(2, 3)?", options=["23", "5", "undefined", "error"], correct_answer=1),
            Test(lecture_id=lecture2.id, question="Что такое hoisting?", options=["Поднятие переменных и функций", "Ошибка в коде", "Оптимизация", "Сжатие кода"], correct_answer=0),
            Test(lecture_id=lecture2.id, question="Как объявить функцию с параметром по умолчанию?", options=["function f(x = 5) {}", "function f(x: 5) {}", "function f(x := 5) {}", "function f(x => 5) {}"], correct_answer=0),
            Test(lecture_id=lecture2.id, question="Что такое рекурсия?", options=["Функция вызывает саму себя", "Бесконечный цикл", "Ошибка", "Переменная"], correct_answer=0),
            Test(lecture_id=lecture2.id, question="Что такое callback функция?", options=["Функция передается как аргумент", "Обратная функция", "Асинхронная функция", "Стрелочная функция"], correct_answer=0),
            Test(lecture_id=lecture2.id, question="Как называется функция без имени?", options=["Arrow function", "Anonymous function", "Callback function", "Default function"], correct_answer=1),
            Test(lecture_id=lecture2.id, question="Что вернет функция без return?", options=["null", "undefined", "0", "error"], correct_answer=1),
            Test(lecture_id=lecture2.id, question="Как передать неограниченное количество аргументов в функцию?", options=["...args", "*args", "args[]", "args..."], correct_answer=0),
            Test(lecture_id=lecture2.id, question="Что такое closure (замыкание)?", options=["Доступ к внешним переменным", "Закрытие функции", "Ошибка", "Завершение функции"], correct_answer=0),
        ]
        
        # Тесты для лекции 3 (10 вопросов)
        tests3 = [
            Test(lecture_id=lecture3.id, question="Как добавить элемент в конец массива?", options=["push()", "append()", "add()", "insert()"], correct_answer=0),
            Test(lecture_id=lecture3.id, question="Как удалить последний элемент массива?", options=["remove()", "delete()", "pop()", "shift()"], correct_answer=2),
            Test(lecture_id=lecture3.id, question="Что делает метод map()?", options=["Фильтрует элементы", "Преобразует каждый элемент", "Ищет элемент", "Сортирует массив"], correct_answer=1),
            Test(lecture_id=lecture3.id, question="Что делает метод filter()?", options=["Преобразует элементы", "Фильтрует элементы по условию", "Сортирует массив", "Удаляет элементы"], correct_answer=1),
            Test(lecture_id=lecture3.id, question="Как найти элемент в массиве?", options=["find()", "search()", "get()", "locate()"], correct_answer=0),
            Test(lecture_id=lecture3.id, question="Что вернет [1,2,3].includes(2)?", options=["true", "false", "2", "error"], correct_answer=0),
            Test(lecture_id=lecture3.id, question="Как объединить два массива?", options=["concat()", "merge()", "join()", "combine()"], correct_answer=0),
            Test(lecture_id=lecture3.id, question="Что делает метод reduce()?", options=["Уменьшает массив до одного значения", "Удаляет элементы", "Сортирует", "Разворачивает массив"], correct_answer=0),
            Test(lecture_id=lecture3.id, question="Как получить длину массива?", options=["arr.length()", "arr.length", "arr.size()", "arr.count()"], correct_answer=1),
            Test(lecture_id=lecture3.id, question="Как проверить, является ли переменная массивом?", options=["Array.isArray()", "isArray()", "typeof arr", "arr.isArray()"], correct_answer=0),
        ]
        
        # Тесты для лекции 4 (10 вопросов)
        tests4 = [
            Test(lecture_id=lecture4.id, question="Как получить значение свойства объекта?", options=["obj.property", "obj['property']", "Оба варианта правильные", "obj.get('property')"], correct_answer=2),
            Test(lecture_id=lecture4.id, question="Что такое this в объекте?", options=["Ссылка на сам объект", "Глобальный объект", "Родительский объект", "Ошибка"], correct_answer=0),
            Test(lecture_id=lecture4.id, question="Как клонировать объект?", options=["Object.assign({}, obj)", "obj.clone()", "copy(obj)", "Object.copy(obj)"], correct_answer=0),
            Test(lecture_id=lecture4.id, question="Что такое деструктуризация объекта?", options=["Извлечение свойств в переменные", "Удаление свойств", "Копирование объекта", "Преобразование объекта"], correct_answer=0),
            Test(lecture_id=lecture4.id, question="Как объединить два объекта?", options=["Object.assign()", "merge()", "combine()", "concat()"], correct_answer=0),
            Test(lecture_id=lecture4.id, question="Что такое JSON?", options=["JavaScript Object Notation", "Java Script Object Name", "JavaScript Output Notation", "Just String Object"], correct_answer=0),
            Test(lecture_id=lecture4.id, question="Как преобразовать объект в JSON строку?", options=["JSON.stringify()", "JSON.parse()", "obj.toString()", "String(obj)"], correct_answer=0),
            Test(lecture_id=lecture4.id, question="Как получить все ключи объекта?", options=["Object.keys()", "obj.keys()", "keys(obj)", "Object.getKeys()"], correct_answer=0),
            Test(lecture_id=lecture4.id, question="Как проверить наличие свойства в объекте?", options=["'prop' in obj", "obj.has('prop')", "obj.contains('prop')", "hasProperty(obj, 'prop')"], correct_answer=0),
            Test(lecture_id=lecture4.id, question="Что такое метод объекта?", options=["Функция внутри объекта", "Свойство объекта", "Переменная", "Константа"], correct_answer=0),
        ]
        
        # Тесты для лекции 5 (9 вопросов)
        tests5 = [
            Test(lecture_id=lecture5.id, question="Какой оператор используется для проверки условия?", options=["if", "when", "check", "verify"], correct_answer=0),
            Test(lecture_id=lecture5.id, question="Что такое тернарный оператор?", options=["Упрощенная форма if/else", "Цикл", "Функция", "Переменная"], correct_answer=0),
            Test(lecture_id=lecture5.id, question="Что вернет: true ? 'да' : 'нет'?", options=["да", "нет", "true", "error"], correct_answer=0),
            Test(lecture_id=lecture5.id, question="Как выйти из цикла досрочно?", options=["break", "exit", "stop", "end"], correct_answer=0),
            Test(lecture_id=lecture5.id, question="Как пропустить итерацию цикла?", options=["continue", "skip", "next", "jump"], correct_answer=0),
            Test(lecture_id=lecture5.id, question="Сколько раз выполнится цикл: for(let i=0; i<5; i++)?", options=["4", "5", "6", "error"], correct_answer=1),
            Test(lecture_id=lecture5.id, question="Какой цикл используется для объектов?", options=["for...in", "for...of", "for", "while"], correct_answer=0),
            Test(lecture_id=lecture5.id, question="Какой цикл используется для массивов?", options=["for...of", "for...in", "for", "while"], correct_answer=0),
            Test(lecture_id=lecture5.id, question="Что такое бесконечный цикл?", options=["Цикл без условия остановки", "Ошибка", "Быстрый цикл", "Оптимизация"], correct_answer=0),
        ]
        
        # Тесты для лекции 6 (10 вопросов)
        tests6 = [
            Test(lecture_id=lecture6.id, question="Что такое DOM?", options=["Document Object Model", "Data Object Model", "Document Output Model", "Display Object Model"], correct_answer=0),
            Test(lecture_id=lecture6.id, question="Как получить элемент по ID?", options=["getElementById()", "getElement()", "queryId()", "findById()"], correct_answer=0),
            Test(lecture_id=lecture6.id, question="Какой метод возвращает первый элемент?", options=["querySelector()", "querySelectorAll()", "getElementsByClassName()", "find()"], correct_answer=0),
            Test(lecture_id=lecture6.id, question="Как изменить текст элемента?", options=["textContent", "innerHTML", "Оба варианта", "text()"], correct_answer=2),
            Test(lecture_id=lecture6.id, question="Как добавить класс элементу?", options=["classList.add()", "addClass()", "className =", "setClass()"], correct_answer=0),
            Test(lecture_id=lecture6.id, question="Как создать новый элемент?", options=["createElement()", "newElement()", "makeElement()", "buildElement()"], correct_answer=0),
            Test(lecture_id=lecture6.id, question="Как добавить элемент в DOM?", options=["appendChild()", "addChild()", "insert()", "append()"], correct_answer=0),
            Test(lecture_id=lecture6.id, question="Как удалить элемент из DOM?", options=["remove()", "delete()", "removeChild()", "Оба варианта A и C"], correct_answer=3),
            Test(lecture_id=lecture6.id, question="Как изменить стиль элемента?", options=["element.style.property", "element.style.setProperty()", "Оба варианта", "element.css()"], correct_answer=2),
            Test(lecture_id=lecture6.id, question="Что такое querySelector?", options=["Современный способ выборки элементов", "Устаревший метод", "Функция jQuery", "Ошибка"], correct_answer=0),
        ]
        
        # Тесты для лекции 7 (10 вопросов)
        tests7 = [
            Test(lecture_id=lecture7.id, question="Как добавить обработчик события?", options=["addEventListener()", "onEvent()", "attachEvent()", "bindEvent()"], correct_answer=0),
            Test(lecture_id=lecture7.id, question="Какое событие происходит при клике?", options=["click", "press", "tap", "touch"], correct_answer=0),
            Test(lecture_id=lecture7.id, question="Как предотвратить стандартное поведение?", options=["preventDefault()", "stopDefault()", "cancelDefault()", "blockDefault()"], correct_answer=0),
            Test(lecture_id=lecture7.id, question="Какое событие для ввода текста?", options=["input", "change", "keypress", "Оба A и B"], correct_answer=3),
            Test(lecture_id=lecture7.id, question="Что такое event.target?", options=["Элемент, на котором произошло событие", "Тип события", "Время события", "Координаты"], correct_answer=0),
            Test(lecture_id=lecture7.id, question="Как остановить всплытие события?", options=["stopPropagation()", "stopBubble()", "cancelBubble()", "preventBubble()"], correct_answer=0),
            Test(lecture_id=lecture7.id, question="Какое событие для наведения мыши?", options=["mouseenter", "mouseover", "hover", "Оба A и B"], correct_answer=3),
            Test(lecture_id=lecture7.id, question="Как удалить обработчик события?", options=["removeEventListener()", "unbindEvent()", "detachEvent()", "clearEvent()"], correct_answer=0),
            Test(lecture_id=lecture7.id, question="Что такое делегирование событий?", options=["Обработка событий на родительском элементе", "Отмена события", "Удаление обработчика", "Добавление события"], correct_answer=0),
            Test(lecture_id=lecture7.id, question="Какое событие происходит при загрузке страницы?", options=["load", "DOMContentLoaded", "ready", "Оба A и B"], correct_answer=3),
        ]
        
        # Тесты для лекции 8 (10 вопросов)
        tests8 = [
            Test(lecture_id=lecture8.id, question="Что такое Promise?", options=["Объект для асинхронных операций", "Функция", "Массив", "Ошибка"], correct_answer=0),
            Test(lecture_id=lecture8.id, question="Какие состояния у Promise?", options=["pending, fulfilled, rejected", "waiting, success, error", "loading, done, failed", "start, end, cancel"], correct_answer=0),
            Test(lecture_id=lecture8.id, question="Как обработать успешный результат Promise?", options=[".then()", ".success()", ".done()", ".result()"], correct_answer=0),
            Test(lecture_id=lecture8.id, question="Как обработать ошибку в Promise?", options=[".catch()", ".error()", ".fail()", ".reject()"], correct_answer=0),
            Test(lecture_id=lecture8.id, question="Что делает ключевое слово async?", options=["Делает функцию асинхронной", "Создает Promise", "Обрабатывает ошибки", "Останавливает выполнение"], correct_answer=0),
            Test(lecture_id=lecture8.id, question="Что делает ключевое слово await?", options=["Ожидает выполнения Promise", "Создает Promise", "Отменяет Promise", "Обрабатывает ошибку"], correct_answer=0),
            Test(lecture_id=lecture8.id, question="Что возвращает fetch()?", options=["Promise", "Объект", "Массив", "Строку"], correct_answer=0),
            Test(lecture_id=lecture8.id, question="Как получить данные из fetch?", options=[".then(r => r.json())", ".json()", ".data()", ".get()"], correct_answer=0),
            Test(lecture_id=lecture8.id, question="Можно ли использовать await без async?", options=["Нет", "Да", "Только в функциях", "Только в циклах"], correct_answer=0),
            Test(lecture_id=lecture8.id, question="Что такое Promise.all()?", options=["Ожидает все Promise", "Отменяет все Promise", "Обрабатывает один Promise", "Создает Promise"], correct_answer=0),
        ]
        
        # Тесты для лекции 9 (9 вопросов)
        tests9 = [
            Test(lecture_id=lecture9.id, question="Что такое стрелочная функция?", options=["Сокращенный синтаксис функции", "Новый тип данных", "Ошибка", "Переменная"], correct_answer=0),
            Test(lecture_id=lecture9.id, question="Что такое деструктуризация?", options=["Извлечение значений из массивов/объектов", "Удаление элементов", "Создание новых структур", "Ошибка"], correct_answer=0),
            Test(lecture_id=lecture9.id, question="Что такое шаблонные строки?", options=["Строки с интерполяцией", "Обычные строки", "Массивы", "Объекты"], correct_answer=0),
            Test(lecture_id=lecture9.id, question="Какой синтаксис для шаблонных строк?", options=["`текст ${var}`", "'текст ${var}'", '"текст ${var}"', "текст ${var}"], correct_answer=0),
            Test(lecture_id=lecture9.id, question="Что делает spread оператор (...)?", options=["Распаковывает элементы", "Собирает элементы", "Удаляет элементы", "Копирует элементы"], correct_answer=0),
            Test(lecture_id=lecture9.id, question="Как экспортировать функцию?", options=["export function name() {}", "exports.name = function() {}", "module.exports = function() {}", "Оба A и B"], correct_answer=0),
            Test(lecture_id=lecture9.id, question="Как импортировать функцию?", options=["import { name } from './file'", "require('./file')", "include('./file')", "Оба A и B"], correct_answer=0),
            Test(lecture_id=lecture9.id, question="Что такое const и let?", options=["Блочная область видимости", "Глобальная область", "Функциональная область", "Ошибка"], correct_answer=0),
            Test(lecture_id=lecture9.id, question="Чем отличается const от let?", options=["const нельзя переопределить", "let нельзя переопределить", "Нет разницы", "const только для функций"], correct_answer=0),
        ]
        
        # Тесты для лекции 10 (10 вопросов)
        tests10 = [
            Test(lecture_id=lecture10.id, question="Как обработать ошибку?", options=["try/catch", "if/else", "switch", "for"], correct_answer=0),
            Test(lecture_id=lecture10.id, question="Что такое блок finally?", options=["Выполняется всегда", "Выполняется при ошибке", "Выполняется при успехе", "Не выполняется"], correct_answer=0),
            Test(lecture_id=lecture10.id, question="Как выбросить ошибку?", options=["throw new Error()", "error()", "throwError()", "createError()"], correct_answer=0),
            Test(lecture_id=lecture10.id, question="Что такое TypeError?", options=["Ошибка типа данных", "Ошибка синтаксиса", "Ошибка логики", "Ошибка сети"], correct_answer=0),
            Test(lecture_id=lecture10.id, question="Что такое ReferenceError?", options=["Ошибка обращения к несуществующей переменной", "Ошибка типа", "Ошибка значения", "Ошибка синтаксиса"], correct_answer=0),
            Test(lecture_id=lecture10.id, question="Как создать пользовательскую ошибку?", options=["class MyError extends Error", "function MyError()", "const MyError = Error", "Ошибки нельзя создавать"], correct_answer=0),
            Test(lecture_id=lecture10.id, question="Что такое SyntaxError?", options=["Ошибка синтаксиса", "Ошибка типа", "Ошибка значения", "Ошибка сети"], correct_answer=0),
            Test(lecture_id=lecture10.id, question="Можно ли использовать несколько catch?", options=["Нет, только один", "Да, несколько", "Только в async", "Только в функциях"], correct_answer=0),
            Test(lecture_id=lecture10.id, question="Что произойдет без обработки ошибки?", options=["Программа остановится", "Программа продолжит работу", "Ничего", "Ошибка проигнорируется"], correct_answer=0),
            Test(lecture_id=lecture10.id, question="Как получить сообщение об ошибке?", options=["error.message", "error.text", "error.toString()", "Оба A и C"], correct_answer=3),
        ]
        
        # Добавляем все тесты
        all_tests = tests1 + tests2 + tests3 + tests4 + tests5 + tests6 + tests7 + tests8 + tests9 + tests10
        session.add_all(all_tests)
        await session.commit()
        
        print("✅ База данных успешно инициализирована!")
        print(f"✅ Добавлено 10 лекций")
        print(f"✅ Добавлено {len(all_tests)} тестов")
        print("✅ Лекции включают видео с YouTube")


if __name__ == "__main__":
    asyncio.run(init_data())
