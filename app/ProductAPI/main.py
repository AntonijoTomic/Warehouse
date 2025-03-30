from fastapi import FastAPI
from database.database import init_db
from routes.product_routes import router as product_router
from routes.category_routes import router as category_router



app = FastAPI()

init_db()  
app.include_router(product_router)
app.include_router(category_router)