FROM python:3.10-slim-bullseye
WORKDIR /
RUN pip install timg 
COPY ./run.py /
COPY ./test.png /
CMD python run.py