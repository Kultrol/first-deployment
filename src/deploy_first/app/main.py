from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from .database import engine
from .dependencies import get_db
from .models import DeploymentTest

app = FastAPI()


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/db")
def database_health() -> dict[str, str]:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        return {"database": "ok"}


@app.post("/deployment-tests")
def create_deployment_test(db: Session = Depends(get_db)) -> dict[str, int]:
    deployment_test = DeploymentTest()

    db.add(deployment_test)
    db.commit()
    db.refresh(deployment_test)

    return {"id": deployment_test.id}
