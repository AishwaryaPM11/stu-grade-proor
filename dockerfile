FROM python:3.11-slim

WORKDIR /app
COPY app.py .

# Provide default arguments here
ENTRYPOINT ["python", "app.py", "Aishwarya", "MCA", "3", "85", "78", "82"]
