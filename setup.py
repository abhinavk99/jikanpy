from setuptools import setup

setup(
   name='jikanpy',
   version='2.0.0',
   description='Python wrapper for the Jikan API',
   author='Andrew Conant, Abhinav Kasamsetty',
   packages=['jikanpy'],
   install_requires=['requests', 'aiohttp'],
)
