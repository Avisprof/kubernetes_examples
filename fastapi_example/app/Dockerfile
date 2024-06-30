FROM python:3.9.19-slim

WORKDIR /app

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["service.py", "./"]

EXPOSE 9696

ENTRYPOINT [ "uvicorn", "service:app", "--host", "0.0.0.0", "--port", "9696"]