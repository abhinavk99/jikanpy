all:
	@echo No argument passed into makefile, exiting...

build-wheel:
	python setup.py sdist bdist_wheel

check:
	twine check dist/*

upload-test:
	twine upload --repository-url https://test.pypi.org/legacy/ --skip-existing dist/*

upload:
	twine upload --repository-url https://upload.pypi.org/legacy/ --skip-existing dist/*
