FROM python:3.10

RUN apt update
RUN python --version

RUN mkdir /music_magazine

WORKDIR /music_magazine

COPY ./src ./src
COPY ./commands ./commands
COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]
# ["python", "src/manage.py", "runserver", "0:8008"]