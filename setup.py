from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel_Reservation_Prediction",
    version="0.0.1",
    author="Aakash Sinha",
    packages=find_packages(),
    install_requires=requirements,
)
    