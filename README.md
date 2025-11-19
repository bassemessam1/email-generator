# OpenAI CLI & FastAPI Tool (Docker Ready)

This repository provides a simple yet powerful setup for interacting with the **OpenAI Responses API** using:

1. **A Python CLI tool** (argparse + dotenv)  
2. **A FastAPI web service**  
3. **A Docker container** that runs either the CLI or the API  

It is ideal for quick testing, automation, and deployment.

---

## 🚀 Features

- CLI script using `client.responses.create()`  
- FastAPI server  
- Docker container running with environment variables  
- `.env` file support  
- Fully reproducible environment via `requirements.txt`

---

## 📁 Project Structure

- email_generator.py # CLI script
- email_generator_api.py # FastAPI app
- requirements.txt
- dockerfile
- .env.example
- README.md

---

# 🧩 1. Running the CLI Tool

The CLI script allows you to send prompts directly from your terminal.


### **Requirements**
- Python 3.9+
- `.env` file containing your API key: <br>
OPENAI_API_KEY=<your_real_key_here>

### **Run the CLI**

`python email_generator.py --recipient "Ali" --topic "Q3 Discussion" --tone "neutral" --cta "setup a meeting" --your_name "Bassem"`


---

# 🌐 2. Running the FastAPI Service

The FastAPI endpoint lets you query the OpenAI API over HTTP.

### **Start the API Server**

`uvicorn email_generator_api:app --reload`

### **Send a request**

curl -X POST "http://127.0.0.1:8000/generate-email" \ <br>
 &nbsp; &nbsp; -H "Content-Type: application/json" \ <br>
 &nbsp; &nbsp; -d '{ <br>
 &nbsp; &nbsp; &nbsp;      "recipient_name": "Anna", <br>
 &nbsp; &nbsp; &nbsp;     "topic": "dashboard testing", <br>
 &nbsp; &nbsp; &nbsp;     "tone": "friendly", <br>
 &nbsp; &nbsp; &nbsp;     "cta": "let me know when we can sync",<br>
 &nbsp; &nbsp; &nbsp;     "your_name": "Bassem" <br>
 &nbsp; &nbsp; &nbsp;  }' <br>

# 3. Running With Docker (CLI or API)

This project includes a Dockerfile that installs all dependencies and supports both CLI use and FastAPI deployment.

### Build Docker Image

From the project root:

`docker build -t <image_name> .`

### Run the CLI inside Docker

Pass your environment variables:

&nbsp;&nbsp;&nbsp;`docker run --env-file .env <image_name> --recipient "Ali" --topic "Q3 Discussion" --tone "neutral" --cta "setup a meeting" --your_name "Bassem"`


# 📦 Requirements

All dependencies are listed in requirements.txt:

- python-dotenv
- openai==2.8.0
- fastapi
- uvicorn


# Notes

- The project uses client.responses.create() instead of deprecated completion endpoints.

- The Docker image is minimal and production-ready.

- You can extend it to add streaming, authentication, or multiple endpoints.