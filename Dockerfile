FROM python:3.10.5
COPY . /apk
WORKDIR /apk
RUN pip install -r requirement.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT apk:apk
