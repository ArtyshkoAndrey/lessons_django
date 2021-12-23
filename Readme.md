# Урок 4 - Работа с Моделями и миграциями

### Цель:
* Создать модель и миграции
* Научится работать с административной панели
* Изучить работу консоли разработчика

### Задачи:
* Создайте дополнительное поле `description` в таблице категорий (`char`, `null`)
* Измените поле `name` в категориях: уникальные значения
* Создайте модуль `products` с таблицей товаров (`product`):
  * `name` (`char`, `unique`)
  * `description` (`char`, `null`)
  * `cost` (`int`)
  * `ordered` (`int`, `default = 0`)
* Создайте модуль `brands` с таблицей брендов (`brand`):
  * `name` (`char`, `unique`)

###Ссылки на документацию
* Изучение Моделей - https://docs.djangoproject.com/en/4.0/topics/db/models/
* Типы полей в моделях - https://docs.djangoproject.com/en/4.0/ref/models/fields/
* Создание моделей и миграций | Обновление моделей - https://docs.djangoproject.com/en/4.0/intro/tutorial02/
* Миграции - https://docs.djangoproject.com/en/4.0/topics/migrations/
* Создание запросов в ORM - https://docs.djangoproject.com/en/4.0/topics/db/queries/