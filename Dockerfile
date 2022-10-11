FROM python:3.10.5
COPY . /app
WORKDIR /app
RUN pip install -r requirement.txt
EXPOSE $PORT
CMD gunicorn
