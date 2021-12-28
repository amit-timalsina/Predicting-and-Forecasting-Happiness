FROM python:3.8-slim
COPY ./app.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./model.pkl /deploy/
COPY ./templates/home.html /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]