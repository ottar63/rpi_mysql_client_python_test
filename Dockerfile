FROM alpine

RUN apk update \
    && apk add bash \
    && apk add python3 \
    && python3 -m pip install --upgrade pip 

WORKDIR "/app"

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 80

COPY test_con.py .

CMD ["python3","test_con.py"]
