from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import orders

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", reload=True)
