# Используем официальный образ для C++
FROM gcc:latest
LABEL authors="danilspitsyn"

# Установим рабочую директорию внутри контейнера
WORKDIR /app

# Скопируем все файлы из текущей директории внутрь контейнера
COPY . .

# Установим Poco C++ библиотеку. Вы можете подставить свои инструкции установки, если это необходимо.
RUN apt-get update && apt-get install -y libpoco-dev && apt-get install -y cmake

# Скомпилируем исходный код вашего бэкенда
RUN mkdir build_ && cd build_ && cmake ../ && make
EXPOSE 8080:8080
#
CMD ["build_/server"]

# Запустим бэкенд
#CMD ["./myapp"]

#ENTRYPOINT ["top", "-b"]