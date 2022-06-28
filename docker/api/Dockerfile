FROM python:3.8

RUN python -m pip install --upgrade pip
WORKDIR /app

COPY docker/app/requirements.txt /app/app_requirements.txt
RUN pip install -r app_requirements.txt

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY docker/app/utils/app.py /app/

COPY ./src/ /app/src/
COPY ./setup.py /app/
RUN python3 -m pip install .

ENTRYPOINT ["python"]
CMD ["entrypoint.py"]
