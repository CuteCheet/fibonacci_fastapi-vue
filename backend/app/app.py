from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"], # Adjust this to match your Vue.js app's origin
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

    # Initialize the first two numbers in the Fibonacci sequence
    first_number, second_number = 0, 1

    # Loop n times to calculate the nth Fibonacci number
    for _ in range(n):
        # Calculate the next number in the sequence by adding the current two numbers
        first_number, second_number = second_number, first_number + second_number

    # Convert the result to a string for JSON serialization
    result = str(first_number)

    # Return the result as a JSON object
    return {"fibonacci": result}