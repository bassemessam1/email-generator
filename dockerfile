FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY email_generator.py .

# Default command (overridable)
ENTRYPOINT ["python", "email_generator.py"]
