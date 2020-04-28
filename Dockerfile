FROM python:3.8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY runit.sh /bin/
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

ENV PORT 9001
EXPOSE 9001
CMD ["runit.sh"]