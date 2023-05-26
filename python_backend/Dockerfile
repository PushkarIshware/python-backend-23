FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
EXPOSE 8000

ENV JWT_TOKEN_SECRET_NAME=secret

CMD python manage.py runserver
