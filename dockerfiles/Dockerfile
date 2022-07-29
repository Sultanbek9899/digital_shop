FROM python:3.8.6-alpine3.12
LABEL maintainer="Sultanbek Beksultanov <sultanbek9899@gmail.com>"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek

RUN apk add --no-cache gcc postgresql-dev zlib-dev \
    libjpeg-turbo-dev gettext linux-headers musl-dev make \
    python3-dev libffi-dev openssl-dev cargo  postgresql-client  wkhtmltopdf \
    && rm -rf /var/apt/list/* \
CMD ["mkdir -p -m 0700 /run/user/0"]
ENV XDG_RUNTIME_DIR=/run/user/0
## ^-- This is the interesting line for you

CMD [ \
    "pandoc", \
    "demo.md", \
    "--output", "demo.pdf", \
    "--pdf-engine", "wkhtmltopdf", \
    "--metadata", "pagetitle='Demo'", \
    "chmod 7700 /tmp"  \
]
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8005

ENTRYPOINT ["sh", "./dockerfiles/docker-entrypoint.sh"]