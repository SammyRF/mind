FROM python:3.6-slim-stretch

RUN pip install pandas xlwt

VOLUME [ "/data" ]

COPY ./conv.py .
COPY ./*.tar .

CMD ["python", "conv.py"]