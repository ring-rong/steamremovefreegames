# Package Deleter Script

This project contains a script designed to automate the process of removing multiple packages from a Steam account. The script utilizes jQuery and AJAX requests to handle the removal of packages through the Steam web interface.

## Files

- `function().js`: This file contains the main script that performs the package deletion.
- `appparcer.py`: This file is part of the project and contains additional functionality for parsing and handling data.

## Requirements

- jQuery library
- Python 3.12 or later

## Installation

1. Clone the repository to your local machine.
    ```bash
    git clone 
    cd 
    ```

2. Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/).

3. Install necessary Python packages.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### JavaScript Script

1. Open the `function().js` file.
2. Edit the `deletePackages` array to include the package IDs you want to remove.
3. Open the Steam account page in your web browser.
4. Open the browser's developer console (F12 key).
5. Copy and paste the contents of `function().js` into the console and press Enter.

The script will start removing the packages one by one. Do not navigate away or refresh the page until the process is complete.

### Python Script

1. Ensure you have the necessary permissions and environment set up to run Python scripts.
2. Run the `appparcer.py` script.
    ```bash
    python appparcer.py
    ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Скрипт для удаления пакетов

Этот проект содержит скрипт, предназначенный для автоматизации процесса удаления нескольких пакетов из аккаунта Steam. Скрипт использует jQuery и AJAX запросы для обработки удаления пакетов через веб-интерфейс Steam.

## Файлы

- `function().js`: Этот файл содержит основной скрипт, выполняющий удаление пакетов.
- `appparcer.py`: Этот файл является частью проекта и содержит дополнительную функциональность для парсинга и обработки данных.

## Требования

- Библиотека jQuery
- Python 3.12 или новее

## Установка

1. Клонируйте репозиторий на ваш локальный компьютер.
    ```bash
    git clone 
    cd 
    ```

2. Убедитесь, что у вас установлен Python. Вы можете скачать его с [официального сайта Python](https://www.python.org/).

3. Установите необходимые пакеты Python.
    ```bash
    pip install -r requirements.txt
    ```

## Использование

### JavaScript Скрипт

1. Откройте файл `function().js`.
2. Измените массив `deletePackages`, добавив в него идентификаторы пакетов, которые вы хотите удалить.
3. Откройте страницу аккаунта Steam в вашем веб-браузере.
4. Откройте консоль разработчика браузера (клавиша F12).
5. Скопируйте и вставьте содержимое файла `function().js` в консоль и нажмите Enter.

Скрипт начнет удалять пакеты один за другим. Не уходите со страницы и не обновляйте её, пока процесс не завершится.

### Python Скрипт

1. Убедитесь, что у вас есть необходимые разрешения и среда для запуска Python скриптов.
2. Запустите скрипт `appparcer.py`.
    ```bash
    python appparcer.py
    ```

## Вклад в проект

1. Форкните репозиторий.
2. Создайте новую ветку (`git checkout -b feature-branch`).
3. Внесите свои изменения.
4. Зафиксируйте изменения (`git commit -m 'Add some feature'`).
5. Отправьте изменения в удаленный репозиторий (`git push origin feature-branch`).
6. Создайте новый Pull Request.
