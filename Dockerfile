FROM python:3.9-slim
RUN pip install flask==2.0.3
COPY ./main.py /app/
COPY ./mathematics.py /app/
COPY ./flask_api.py /app/
WORKDIR /app/
ENTRYPOINT ["python"]
CMD ["main.py"]
