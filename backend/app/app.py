from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"], # Adjust this to match your Vue.js app's origin
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)


@app.get("/fibonacci/{n}")
async def fibonacci(n: int):

    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    res = str(x)
    return {"fibonacci": res}
