FROM python:3.14-slim

WORKDIR /src/deploy_first

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-install-project

COPY . .

RUN uv sync --frozen --no-dev

ENV PORT=8000

EXPOSE 8000

CMD ["sh", "-c", "uv run alembic upgrade head && exec uv run uvicorn deploy_first.app.main:app --host 0.0.0.0 --port \"$PORT\""]
