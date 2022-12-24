setup:
	pip install -U pip setuptools
	pip install -r requirements.txt
	pip install .

setup-dev:
	pip install -U pip setuptools
	pip install -r requirements.txt
	pip install -e .


backend_name = 'backend'
frontend_name = 'frontend'

build-docker-backend:
	docker build . -t $(backend_name) -f docker_files/backend.dockerfile

run-docker-backend:
	docker run -it --rm -d -p 5000:5000 $(backend_name) python main.py

build-docker-frontend:
	docker build . -t $(frontend_name) -f docker_files/frontend.dockerfile

run-docker-frontend:
	docker run -it --rm -d -p 8080:8080 $(frontend_name)

compose-docker:
	docker-compose up --build -d
