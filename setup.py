import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
# optionally read the CHANGELOG.md file, to include this with pypi releases
# may not be necessary, just to be safe
CHANGELOG_FILE = HERE / "CHANGELOG.md"
CHANGELOG = CHANGELOG_FILE.read_text() if CHANGELOG_FILE.exists() else ""

setup(
    name="jikanpy_v4",
    version="1.0.1",
    description="Python wrapper for the Jikan API",
    license="MIT",
    long_description=README + CHANGELOG,
    long_description_content_type="text/markdown",
    author="Chris Peterson",
    author_email="chris.peterson444@gmail.com",
    package_data={"jikanpy": ["py.typed"]},
    packages=["jikanpy"],
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
