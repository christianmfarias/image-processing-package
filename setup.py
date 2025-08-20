from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_package",
    version="0.0.2",
    author="Christian Farias",
    author_email="christian.farias@ctlbrasil.com.br",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/christianmfarias/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)