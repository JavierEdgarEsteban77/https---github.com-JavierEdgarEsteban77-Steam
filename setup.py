from setuptools import setup, find_packages

setup(
    name='steam_analysis_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'pandas',
    ],
)
