# Используем официальный образ для C++
FROM gcc:latest
LABEL authors="danilspitsyn"

# Установим рабочую директорию внутри контейнера
WORKDIR /app

# Скопируем все файлы из текущей директории внутрь контейнера
COPY . .

# Установим Poco C++ библиотеку. Вы можете подставить свои инструкции установки, если это необходимо.
RUN apt-get update && apt-get install -y libpoco-dev \
                                            cmake  \
                                            openssh-server rsync

# Скомпилируем исходный код вашего бэкенда
 RUN mkdir build_ && cd build_ && cmake ../ && make -j2
EXPOSE 8080:8080


RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# 18000 for ssh server.
EXPOSE 18000

# Create dev user with password 'dev'
RUN useradd -m -s /bin/bash dev
RUN echo 'dev:dev' | chpasswd

# Upon start, run ssh daemon
RUN nohup /usr/sbin/sshd -D -p 18000 &

#RUN echo "/tmp/core.%e.%p.%t" |  tee /proc/sys/kernel/core_pattern && ulimit -c unlimited



#
CMD ["build_/server"]