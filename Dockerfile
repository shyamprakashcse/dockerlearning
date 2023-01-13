FROM python:3.10 


WORKDIR /DockerDemo
COPY ./requirements.txt /DockerDemo
RUN pip install -r requirements.txt 
COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
