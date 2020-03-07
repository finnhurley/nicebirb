FROM python:3.7-alpine

COPY bot/config.py /bots/
COPY bot/messages.py /bots/
COPY bot/wholesome.py /bots/
COPY requirements.txt /tmp
COPY util/messages.txt /util/
RUN pip3 install -r /tmp/requirements.txt

CMD ["python3", "bots/wholesome.py"]