#REM Assuming my application files are in a directory named "myapp"
#cd myapp

#REM Create a Python script (e.g., welcome.py)
#echo print("Hello, World!") > welcome.py

#REM Create a Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
CMD ["python", "welcome.py"] > Dockerfile

#REM Build the Docker image
#docker build -t myapp .

#REM Run the Docker container
#docker run myapp
