FROM python:3.8

RUN apt-get update -y && \
    apt-get install software-properties-common -y && \
    apt install nodejs npm -y && \
    apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main' && \
    apt-get update -y && \
    apt-get install -y openjdk-8-jdk libaio1 && \
    apt-get purge -y perl perl5 && \
    apt-get -y install git gcc && \
    apt-get -y install ffmpeg && \
    apt-get -y install --reinstall build-essential && \
    apt-get -y autoremove && \
    apt-get clean

RUN python -m pip install --upgrade pip

COPY docker/jupyter/requirements.txt /home/jupyter_requirements.txt
RUN pip install -r /home/jupyter_requirements.txt

COPY requirements.txt /home/
RUN pip install -r /home/requirements.txt
RUN rm /home/jupyter_requirements.txt /home/requirements.txt

RUN jupyter lab --generate-config
RUN printf "c.ServerApp.port = 8888\nc.ServerApp.ip = '*'\nc.ServerApp.allow_root = True\nc.FileCheckpoints.checkpoint_dir = '/root/.jupyter/.ipynb_checkpoints'" >> /root/.jupyter/jupyter_lab_config.py

WORKDIR /home/jupyter/
EXPOSE 8888 9999

COPY ./src/ /home/jupyter/src/
COPY ./setup.py /home/jupyter/
RUN pip install -e .

CMD ["jupyter", "lab"]
