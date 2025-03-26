from fastapi import FastAPI
from database.database import init_db

app = FastAPI()


init_db()