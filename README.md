Tests/Linters in `master`

[![Python application](https://github.com/worker-beep/api_yamdb/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/worker-beep/api_yamdb/actions/workflows/python-app.yml)

Tests/Linters in `develop`

[![Python application](https://github.com/worker-beep/api_yamdb/actions/workflows/python-app.yml/badge.svg?branch=develop)](https://github.com/worker-beep/api_yamdb/actions/workflows/python-app.yml)

[GITHUB-BADGE](https://github.com/avsedeleva/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Проект YaMDb

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на
категории: «Книги», «Фильмы», «Музыка». Список категорий (Category)
может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. В каждой
категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть
произведения «Винни Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня
«Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр из списка
предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только
администратор.

Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы (Review) и
выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок
автоматически высчитывается средняя оценка произведения.

# Пользовательские роли

* **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
* **Аутентифицированный пользователь** (`user`)— может читать всё, как и Аноним, дополнительно может
  публиковать отзывы и ставить рейтинг произведениям (фильмам/книгам/песенкам), может комментировать
  чужие отзывы и ставить им оценки; может редактировать и удалять свои отзывы и комментарии.
* **Модератор** (`moderator`) — те же права, что и у Аутентифицированного пользователя плюс право
  удалять и редактировать любые отзывы и комментарии.
* **Администратор** (`admin`) — полные права на управление проектом и всем его содержимым. Может
  создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
* **Администратор Django** — те же права, что и у роли Администратор.

# Алгоритм регистрации пользователей

1. Пользователь отправляет POST-запрос с параметром email на /api/v1/auth/email/.
1. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
1. Пользователь отправляет POST-запрос с параметрами email и confirmation_code на
   /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).

Эти операции выполняются один раз, при регистрации пользователя. В результате пользователь получает
токен и может работать с API, отправляя этот токен с каждым запросом.

После регистрации и получения токена пользователь может отправить PATCH-запрос на /api/v1/users/me/
и заполнить поля в своём профайле

# Ресурсы API YaMDb

* Ресурс **AUTH**: аутентификация.
* Ресурс **USERS**: пользователи.
* Ресурс **TITLES**: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
* Ресурс **CATEGORIES**: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
* Ресурс **GENRES**: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
* Ресурс **REVIEWS**: отзывы на произведения. Отзыв привязан к определённому произведению.
* Ресурс **COMMENTS**: комментарии к отзывам. Комментарий привязан к определённому отзыву.
