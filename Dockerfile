# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /RAG_project

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY app ./app

# Copy the data folder to the container
COPY data ./data

# Expose the port that your FastAPI app will run on
EXPOSE 8000

# Command to run your application
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]