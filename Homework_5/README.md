структура проекта

project_root/
│
├── tests/
│   ├── resources/
│       ├── download.jpg               # Пример изображения для загрузки
│   ├── test_registration.py        # Исходный тест
│   ├── improved_test_form_submission.py  # Тест для ДЗ
│
├── pages/
│   ├── registration_page.py       # Страница регистрации с действиями
│
├── models/
│   ├── users.py                   # Данные пользователей в виде dataclass
│
├── resources/
│   ├── download.jpg               # Пример изображения для загрузки
│
├── requirements.txt               # Список зависимостей проекта
├── pytest.ini                     # Конфигурация для pytest (если используется)
└── README.md                      # Документация по проекту (опционально)
