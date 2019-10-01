# selenium_stepik_final_task

#*Page Object Pattern*

Набор тестов для сайта [selenium1py.pythonanywhere.com](http://selenium1py.pythonanywhere.com).

### Как установить
Скачиваем файлы и переходим в папку.
Устанавливаем chromedriver по [этой инструкции](https://selenium-python.com/install-chromedriver-chrome)

Python 3.7 должен быть уже установлен.

Затем используем pip для установки зависимостей:

```
pip install -r requirements.txt
```
### Использование

После настройки скрипт запускаем из корневой папки.

```
pytest -v --tb=line --language=en -m need_review

pytest -v --tb=line --language=en
```
### Цель проекта

Код написан в образовательных целях для [stepik.org](https://stepik.org/)
