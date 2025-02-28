FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    binutils \
    gdal-bin \
    libproj-dev \
    libgdal-dev \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Set work directory
WORKDIR /usr/src/app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
