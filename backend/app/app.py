from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from math import sqrt

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
    """
    This function calculates the nth number in the Fibonacci sequence.
    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 1 and 1.
    """
    result = await calculate_fibonacci(n)
    return result

async def calculate_fibonacci(n: int):

    #Calculate nth term by one single formula
    num = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    result = str(int(num))

    # Return the result as a JSON object
    return result