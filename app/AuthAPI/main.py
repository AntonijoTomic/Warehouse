from fastapi import FastAPI
from database.databse import init_db
from routes.user_routes import router as user_router

app = FastAPI()

init_db()
app.include_router(user_router)



