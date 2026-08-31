FROM python:3.14-slim

WORKDIR /src/deploy_first

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-install-project

COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.deploy_first.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
