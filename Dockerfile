FROM python:3.8

WORKDIR /pyapp/

COPY src/* src/

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["src/server.py"]