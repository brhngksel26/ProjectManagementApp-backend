FROM python:3.10

COPY . /project_management
WORKDIR ./project_management

run ls

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]