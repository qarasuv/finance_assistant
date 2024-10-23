# Finance Assistant

**Finance Assistant** — это приложение для управления личными финансами, которое позволяет регистрироваться пользователям, вести учёт доходов и расходов, а также анализировать свои финансовые данные.

## Установка
    ```bash
    git clone https://github.com/qarasuv/finance_assistant.git
    cd finance_assistant
    git checkout 8-report-generation
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python3 manage.py runserver
    ```

## Использование

- Перейдите на `http://127.0.0.1:8000/users/` после запуска.
- Зарегистрируйтесь или войдите в систему.
- Добавляйте доходы и расходы для отслеживания ваших финансов.
- Анализируйте данные на дашборде для контроля финансового состояния.

## Стек технологий

- Python (Django)
- JavaScript
- HTML/CSS

## Лицензия

Проект лицензирован под MIT License.
