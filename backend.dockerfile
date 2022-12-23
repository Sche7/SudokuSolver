FROM python:3.9.15

# Set working directory
WORKDIR /sudoku_solver

# Install dependencies
COPY requirements.txt /sudoku_solver/
RUN pip install --no-cache-dir --upgrade pip setuptools && \
    pip install --no-cache-dir --upgrade -r requirements.txt

# Copy backend
COPY /core /sudoku_solver/core
COPY main.py /sudoku_solver/
