FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python userdetails.py
CMD python api.py
