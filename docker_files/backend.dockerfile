FROM python:3.9.15

# Set working directory
WORKDIR /sudoku_solver/core

# Copy backend
COPY ./core ./

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools && \
    pip install --no-cache-dir --upgrade -r requirements.txt && \
    pip install -e .
