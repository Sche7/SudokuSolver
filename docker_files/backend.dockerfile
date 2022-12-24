FROM python:3.9.15

# Set working directory
WORKDIR /sudoku_solver

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip setuptools && \
    pip install --no-cache-dir --upgrade -r requirements.txt

# Copy backend
COPY /core ./core
COPY main.py ./
