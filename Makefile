setup:
	pip install -U pip setuptools
	pip install -r requirements.txt
	pip install .

setup-dev:
	pip install -U pip setuptools
	pip install -r requirements.txt
	pip install -e .


backend_name = 'backend'

build-docker-backend:
	docker build . -t $(backend_name) -f backend.dockerfile

run-docker-backend:
	docker run -it --rm -d -p 5000:5000 $(backend_name) python main.py
