FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
COPY . /opt/afnor_api/
WORKDIR /opt/afnor_api/
EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
RUN python manage.py migrate

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]