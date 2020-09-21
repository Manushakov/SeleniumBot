[English version](README.en.md)
```
Основной задачей проекта является получение информации об оценках с сайта grade.sfedu.ru
С помощью Selenium производится авторизация и получение необходимых строк, далее они высылаются ботом в телеграмме
Для бота используется библиотека telebot, работает на поллинге.
```

Для бота необходим токен, который находится в файле constants.py\
получить его можно у BotFather в телеграмме

**Установка зависимостей**\
`pip install -r requirements`

**Запуск бота**\
`python main.py`