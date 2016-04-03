FROM tp33/django-docker:1.3
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt
ADD . /code/
