FROM python:3
ADD hello.py ./
RUN pip install flask
RUN chmod 644 hello.py
HEALTHCHECK CMD curl --fail http://localhost:8080/ || exit 1
CMD ["python", "hello.py"]
