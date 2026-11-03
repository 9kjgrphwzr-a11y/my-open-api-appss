Создай полный Python-код для Streamlit приложения met_app.py.

Приложение должно искать произведения искусства через Metropolitan Museum of Art Collection API.

Используй:
- Search endpoint: https://collectionapi.metmuseum.org/public/collection/v1.1/search
- Details endpoint: https://collectionapi.metmuseum.org/public/collection/v1/objects/
- Поля: title, artistDisplayName, objectDate, primaryImageSmall, objectURL.
Функции:
- Поле поиска произведений искусства.
- По умолчанию поиск flower.
- Slider от 3 до 12 произведений.
- Показывать произведения в три колонки с изображениями.
- Показывать название, художника, год и ссылку на музей.
- Не показывать произведения без изображения.
- Обрабатывать ошибки через try/except.
- Использовать requests timeout=10.
- Кэшировать результаты на 1 час через st.cache_data.
- Добавить понятное сообщение, если ничего не найдено.
Напиши полный готовый код, который можно сразу вставить в GitHub.
Не пропускай части кода.
