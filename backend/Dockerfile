# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt ./

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend source code
COPY . .

# Run the backend server
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "app.app:app", "--bind", "0.0.0.0:8000"]

