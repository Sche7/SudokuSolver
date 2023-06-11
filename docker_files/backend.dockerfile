FROM python:3.9.15

# Set working directory
WORKDIR /sudoku_solver/core

# Install dependencies
COPY ./core/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools && \
    pip install --no-cache-dir --upgrade -r requirements.txt

# Copy backend
COPY ./core ./
RUN pip install -e .
