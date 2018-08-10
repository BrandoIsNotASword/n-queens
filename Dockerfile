FROM python:alpine3.7
COPY . /n-queens
WORKDIR /n-queens
CMD python ./queens.py