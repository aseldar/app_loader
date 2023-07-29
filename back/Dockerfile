# Устанавливаем базовый образ с Python
FROM python:3.9-slim

# Устанавливаем необходимые пакеты для загрузки Chrome
RUN apt-get update && \
    apt-get install -y wget gnupg2 unzip

# Устанавливаем Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Устанавливаем драйвер для Chrome
RUN LATEST_VERSION=$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$LATEST_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/

# Устанавливаем рабочую директорию в контейнере
WORKDIR /back

# Копируем файлы зависимостей и устанавливаем их
COPY /back/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /usr/local/bin/chromedriver

ENV PATH="/usr/local/bin:${PATH}"

# Копируем файлы приложения в контейнер
COPY /back  .

# Запускаем приложение при старте контейнера
CMD ["python", "app.py"]
