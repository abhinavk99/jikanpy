import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="jikanpy",
    version="3.4.0",
    description="Python wrapper for the Jikan API",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Andrew Conant, Abhinav Kasamsetty",
    package_data={"jikanpy": ["py.typed"]},
    packages=["jikanpy"],
    url="https://github.com/AWConant/jikanpy",
    install_requires=["requests", "aiohttp"],
    keywords=["jikan", "jikanpy", "api", "myanimelist"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
)
