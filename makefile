build-wheel:
	python setup.py sdist bdist_wheel

check:
	twine check dist/*

upload-legacy:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	twine upload --repository-url https://upload.pypi.org/legacy/ --skip-existing dist/*
