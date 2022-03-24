all:
	@echo you need to specify a command

bootstrap:
	./bootstrap_v4

format:
	black ./jikan_api_client

publish:
	poetry publish --build

lint:
	flake8 ./jikan_api_client ./jikanpy
	mypy -p jikan_api_client -p jikanpy

install:
	python3 -m pip install .
