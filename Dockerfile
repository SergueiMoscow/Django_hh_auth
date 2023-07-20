FROM python:3.9

COPY . /app/
WORKDIR /app

ENV DB_PASSWORD="123321"

RUN pip install -r requirements.txt

CMD ["python", "myproject/manage.py", "runserver", "0.0.0.0:8000"]


# docker build my_project .
# docler run -p 8000:8000
# https://rebrainme.com/
# Расширения для Django:
# https://www.youtube.com/watch?v=XmdoY2xJhqY
# Docker видео:
# https://www.youtube.com/watch?v=n9uCgUzfeRQ
# Для FreeBSD Jail (Контейнеры)
# https://habr.com/ru/articles/342312/
# или bhyve (Виртуализация)
# http://snakeproject.ru/rubric/article.php?art=FreeBSD_bhyve_ubuntu_07.2018

# или вообще chroot
