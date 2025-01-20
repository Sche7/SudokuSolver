FROM python:3.10

# Set working directory
WORKDIR /sudoku_solver/core

# Install dependencies
COPY ./core/pyproject.toml .
COPY ./core/poetry.lock .
RUN pip install --no-cache-dir --upgrade pip setuptools && \
    pip install --no-cache-dir pyproject.toml

# Copy backend
COPY ./core ./
RUN pip install -e .
