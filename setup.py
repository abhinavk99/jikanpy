from setuptools import setup

setup(
    name='jikanpy',
    version='3.0.2',
    description='Python wrapper for the Jikan API',
    author='Andrew Conant, Abhinav Kasamsetty',
    package_data={'jikanpy': ['py.typed']},
    packages=['jikanpy'],
    install_requires=['requests', 'aiohttp'],
    zip_safe=False
)
