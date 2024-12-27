# BooksCollector - Тесты

## Описание проекта

Проект содержит класс BooksCollector, который позволяет добавлять книги, устанавливать их жанры, управлять избранными книгами и получать различные списки книг по жанрам и возрастным рейтингам.

## Реализованные тесты

### Метод add_new_book
- **Добавление двух книг**: Проверка успешного добавления двух различных книг.
- **Добавление книги с допустимым названием**: Проверка добавления книги с нормальным названием.
- **Добавление книги с названием длиной 40 символов**: Проверка добавления книги на границе допустимой длины названия.
- **Попытка добавить книгу с пустым названием**: Проверка, что книга с пустым названием не добавляется.
- **Попытка добавить книгу с названием длиннее 40 символов**: Проверка, что книга со слишком длинным названием не добавляется.
- **Попытка добавить дубликат книги**: Проверка, что одна и та же книга не может быть добавлена несколько раз.

### Метод set_book_genre
- **Установка жанра для существующей книги**: Проверка успешной установки жанра.
- **Попытка установить жанр для несуществующей книги**: Проверка, что жанр не устанавливается для отсутствующей книги.
- **Установка различных допустимых жанров**: Параметризованные тесты для всех допустимых жанров.
- **Попытка установить недопустимый жанр**: Проверка, что жанр не устанавливается, если он не в списке допустимых.

### Метод get_book_genre
- **Получение жанра существующей книги**: Проверка корректного возвращения жанра.
- **Попытка получить жанр несуществующей книги**: Проверка, что возвращается None для отсутствующей книги.

### Метод get_books_with_specific_genre
- **Получение списка книг определенного жанра**: Проверка, что возвращается правильный список книг.
- **Получение списка книг при отсутствии книг с заданным жанром**: Проверка, что возвращается пустой список.

### Метод get_books_genre
- **Получение текущего состояния словаря books_genre**: Проверка корректного возвращения всего словаря.

### Метод get_books_for_children
- **Получение списка книг, подходящих для детей**: Проверка, что возвращаются только книги без возрастного рейтинга.
- **Проверка при отсутствии книг, подходящих для детей**: Проверка, что возвращается пустой список.
- **Проверка с добавленными любимыми книгами**: Проверка, что метод возвращает только книги, подходящие для детей.

### Метод add_book_in_favorites
- **Добавление книги в избранное**: Проверка успешного добавления.
- **Попытка добавить в избранное книгу, которой нет в books_genre**: Проверка, что книга не добавляется.
- **Попытка добавить книгу в избранное несколько раз**: Проверка, что дубликаты не добавляются.

### Метод delete_book_from_favorites
- **Удаление книги из избранного**: Проверка успешного удаления.
- **Попытка удалить книгу, которой нет в избранном**: Проверка, что операция проходит без ошибок.

### Метод get_list_of_favorites_books
- **Получение списка избранных книг**: Проверка корректного возвращения списка.
- **Проверка при пустом избранном**: Проверка, что возвращается пустой список.

### Новые тесты с любимыми книгами и жанрами
- **Добавление и проверка любимых книг с их жанрами**: Параметризованный тест, который добавляет ваши любимые книги, устанавливает жанры, добавляет их в избранное и проверяет корректность данных.
- **Получение избранных книг по жанрам**: Проверка метода get_books_with_specific_genre для ваших любимых жанров.
- **Получение списка книг для детей с учетом избранных книг**: Проверка, что метод get_books_for_children возвращает только подходящие книги из избранного.

## Запуск тестов

Для запуска тестов используйте команду:
`pytest -v test.py`

## Запуск тестов с покрытием

Для сбора покрытия кода и генерации отчёта используйте команду:
`pytest --cov=main -v`

## HTML-отчёт покрытия кода

Чтобы открыть HTML-отчёт покрытия кода в браузере, выполните следующие шаги:
`start htmlcov\index.html`

