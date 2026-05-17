# Планировщик задач
Простая консольная программу: добавление задач, постановка дедлайнов и приоритетов, при запуске показывает, что необходимо срочно выполнить

## Команда и роли
| Участник | Роль |Ветка | Основные функции 
|----------|------|-------|------------------
| Шагиева С. | Тимлид | main | мерж, README, deadlone_check
| Шубина А. | Аналитик | feature/tasks_crud | add_task, view_tasks, display_tasks, get_all_tasks
| Аллаярова А. | UI | allayarova_t | mark_task_done, delete_task
| Леонтьева Е. | Тестировщик | (тех.проблема) | sort_by_deadline, show_statistics

## Как запустить проект
1. Склонируйте репозиторий: git clone <url>
2. Создайте виртуальное окружение: python -m venv .venv
3. Активируйте: source .venv/bin/activate (Linux/macOS) или .venv\Scripts\activate (Windows)
4. Установите зависимости: pip install -r requirements.txt
5. Запустите: python main.py

## Технологии и модули
- Python 3.10+
- Стандартные модули: string, collections, datetime
- Без сторонних NLP-библиотек

## Структура репозитория
project/
├── README.md           # описание, как запустить
├── requirements.txt    # зависимости (пустой, практика работы с pip)
├── main.py                    # точка входа
└── modules/                  # собственные модули команды
    ├── task_manager.py
