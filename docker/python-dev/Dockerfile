FROM python:3.8

RUN python -m pip install --upgrade pip
WORKDIR /app/

COPY docker/python-dev/requirements.txt /app/python_dev_requirements.txt
RUN pip install -r python_dev_requirements.txt

COPY requirements.txt /app/
RUN pip install -r requirements.txt

RUN rm /app/requirements.txt /app/python_dev_requirements.txt

CMD ["python"]
