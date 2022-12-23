setup:
	pip install -U pip setuptools
	pip install -r requirements.txt
	pip install .

setup-dev:
	pip install -U pip setuptools
	pip install -r requirements.txt
	pip install -e .


backend_name = 'sudoku_backend'

build-docker-backend:
	docker build . -t $(backend_name) -f backend.dockerfile
