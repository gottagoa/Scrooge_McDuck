FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek


RUN apk add libffi-dev\
    gcc libc-dev
RUN apk add --no-cache gcc postgresql-dev zlib-dev \
    gettext linux-headers musl-dev make \
    python3-dev libffi-dev openssl-dev cargo  postgresql-client  \
    && rm -rf /var/apt/list/*

WORKDIR /app

COPY requirements.txt requirements.txt


RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "dockerfiles/docker_entrypoint.sh"]