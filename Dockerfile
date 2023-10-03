# Pull base image
FROM python:3.10.12-slim-bullseye
# Set environment variables

# 1. disables an automatic check for pip updates each time
ENV PIP_DISABLE_PIP_VERSION_CHECK 1 

# 2. means Python will not try to write .pyc file
ENV PYTHONDONTWRITEBYTECODE 1

# 3. ensures our console output is not buffered by Docker
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /django_api_crud
# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Copy project
COPY . .