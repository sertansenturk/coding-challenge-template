FROM python:3.8

RUN apt-get update -y && \
    apt-get -y install ffmpeg && \
    apt-get -y autoremove && \
    apt-get clean

RUN python -m pip install --upgrade pip
WORKDIR /app/

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./src/ /app/src/
COPY ./setup.py /app/

RUN python3 -m pip install .

CMD ["ct", "--help"]
