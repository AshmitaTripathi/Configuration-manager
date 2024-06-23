from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import router

app = FastAPI()

# add database tables
Base.metadata.create_all(bind=engine)

# Include the router
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)