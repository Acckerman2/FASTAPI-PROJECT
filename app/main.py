from fastapi import FastAPI 
from .database import engine 
from  . import models
from .routers import posts, users,auth,votes


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)



    
