import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
CHANGELOG = (HERE / "CHANGELOG.md").read_text()

setup(
    name="jikanpy",
    version="4.3.1",
    description="Python wrapper for the Jikan API",
    license="MIT",
    long_description=README + CHANGELOG,
    long_description_content_type="text/markdown",
    author="Abhinav Kasamsetty",
    author_email="abhinavkasamsetty@gmail.com",
    package_data={"jikanpy": ["py.typed"]},
    packages=["jikanpy"],
    data_files=[(".", ["CHANGELOG.md"])],
    url="https://github.com/abhinavk99/jikanpy",
    install_requires=["requests", "aiohttp", "simplejson"],
    keywords=["jikan", "jikanpy", "api", "myanimelist"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False,
    python_requires=">=3.6",
)
