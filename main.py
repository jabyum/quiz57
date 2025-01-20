import pydantic
from fastapi import FastAPI, Request

app = FastAPI(docs_url="/")


# запуск uvicorn main:app --reload
