FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY ./ /app/

RUN python manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
