FROM python:3.11-slim-bullseye

ENV HOME /home/klefki
RUN useradd -m klefki
WORKDIR $HOME
COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt
USER klefki

COPY klefki.py klefki.py
COPY utils utils
COPY cogs cogs
COPY dbupdate dbupdate

RUN ln -sf /run/secrets/klefki-config config.json

CMD ["python3", "klefki.py"]
