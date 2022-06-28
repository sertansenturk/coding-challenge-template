FROM python:3.8

RUN python -m pip install --upgrade pip
WORKDIR /api

COPY docker/api/requirements.txt /api/api_requirements.txt
RUN pip install -r api_requirements.txt

COPY requirements.txt /api/
RUN pip install -r requirements.txt

COPY docker/api/utils/api.py /api/

COPY ./src/ /api/src/
COPY ./setup.py /api/
RUN python3 -m pip install .

ENTRYPOINT ["python"]
CMD ["api.py"]
