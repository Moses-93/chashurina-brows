# Проєкт: chashurina-brows

## Призначення: 

### Цей сайт створений для автоматизації процесу запису клієнтів до майстра-бровіста. Він значно спрощує комунікацію між клієнтом та майстром, заощаджуючи час обох сторін.

## Основні функції:

#### Запис клієнта: Клієнт може самостійно обрати бажану послугу та зручну дату на сайті. Після вибору доступних послуг, система автоматично генерує вільні часові слоти.
#### Сповіщення для майстра: Після того, як клієнт записався, майстер отримує сповіщення у Telegram з усіма деталями запису.
#### Автоматизація процесу: Майстер заздалегідь вказує, на які дати доступний для приймання клієнтів, а подальший процес запису відбувається без його участі.
## Переваги
#### Зручність для клієнта: Нема потреби писати майстру особисто, щоб дізнатися про доступні дати та часи. Клієнт самостійно вибирає послугу та зручний час на сайті.
#### Ефективність для майстра: Всі сповіщення надходять автоматично, що звільняє майстра від ручної роботи із записом клієнтів.


# Технологічний стек
## Back-end:
#### Django (Python) Використано для розробки основної логіки веб-застосунку, обробки форм, створення моделей та відображення сторінок.

## Front-end: HTML, CSS
#### Використано для верстки сторінок, оформлення інтерфейсу користувача та інтерактивності.

## База даних: PostgreSQL
#### Відповідає за збереження інформації про клієнтів, записи та послуги. Реалізовано через ORM Django.

## Контейнеризація: Docker
#### Сайт працює у Docker-контейнерах для забезпечення ізольованого середовища розробки та продакшн-розгортання.

## Сервер: Nginx
#### Використовується як зворотний проксі та для обслуговування статичних файлів.

## Gunicorn:
#### Використано як WSGI сервер для обробки запитів до Django.

## CI/CD: Git та Docker Compose
#### Налаштовано інтеграцію для зручного деплою проєкту.

## Сповіщення: Telegram API
#### Автоматичні сповіщення про нові записи надсилаються майстру через Telegram.
