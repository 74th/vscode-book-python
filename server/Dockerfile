FROM python:3.8.2

# Poetryのインストール
RUN pip install poetry==1.0.5

WORKDIR /app

# 依存パッケージのインストール
COPY poetry.lock pyproject.toml ./
# devは除く
RUN poetry install --no-dev

EXPOSE 8080

# Poetry経由で実行する
CMD ["poetry", "run", "python", "api.py"]
