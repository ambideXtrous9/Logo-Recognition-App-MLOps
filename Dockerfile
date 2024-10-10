FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the /app directory in the container
COPY . .

# Build argument for credentials
ARG GOOGLE_APPLICATION_CREDENTIALS

# Copy the credentials file into the container
COPY ${GOOGLE_APPLICATION_CREDENTIALS} /app/credentials.json

# Set the environment variable to point to the credentials file
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json



RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port you want your app on
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "–server.port=8501", "–server.address=0.0.0.0"]
