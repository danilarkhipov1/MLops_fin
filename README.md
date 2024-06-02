# MLops_fin


## Структура проекта и назначение файлов:
```
src/                                - каталог с исполняемыми скриптами приложения
    src/api_app_titanic.py            - API приложение на FastAPI
    src/dataset_titanic_modifed.py    - создаем модифицированный датасет
    src/make_dataset_titanic.py       - сохраняем датасет Titanic
    src/model_titanic.py              - обучаем модель на данных датасета Titanic
```
## Тестирование
```
test/
    test/api_app_test.py               - модульное тестирование API приложения
    test/dataset_test.py               - функциональное тестирование предсказательной способности модели
```
## Сборка Docker контейнера
```
./doker_container_run.bat           - запуск docker контейнера с приложением из образа (Windows)
./doker_container_run.sh            - запуск docker контейнера с приложением из образа (Unix)
./Dokerfile                         - файл для создания doker образа приложения
./Jenkinsfile                       - конвейер для автоматического развертывания приложения, тестирования и сборка doker образа
```     

```
./predict_titanic.bat               - командный файл для проверки работы API приложения (Windows)
./predict_titanic.sh                - командный файл для проверки работы API приложения (Unix)
```
## DVC 
Версии дата сета хранятся в [Google Drive](https://drive.google.com/drive/folders/1AdDlbd3qt9NB2Vwn2UypTrmZI9AmLmWc)
Путь также отображается в файле [config](./dvc/config)

Приложение собирается в docker контейнере. Сборка приложения, тестирование и создание docker образа происходит в
автоматическом режиме в Jenkins на основе файла сценария Jenkinsfile.

После создания docker образа приложения запускаем командный файл doker_container_run.bat (doker_container_run.sh) для 
сборки и запуска docker контейнера с приложением. Приложение запускается на порту 8091.

Для проверки работы приложения запускаем командные файлы: predict_titanic.bat (predict_titanic.sh)