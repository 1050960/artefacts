# ����� ����� python 10 slim-bullseye �� ��������� � �������
from python:3.10-slim-bullseye
# ������������� ������� ���������� �� ���������
WORKDIR /code
# �������� ���� requirements � ������� ������� ��� ����������� ����
COPY ./requirements.txt /code/requirements.txt
# ������������� ��� ��� ����� ��� python �� �������� ��� ���� ����� ��� �� �������
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# �������� ���
COPY ./app /code/app
# ��������� ��� FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]