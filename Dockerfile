FROM python:3.7
# Creating /app
WORKDIR /app
# Copying all file and folder from docker context to /app
COPY . .
# Installing the dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
# CMD or Entrypoint
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7777"]