from setuptools import setup, find_packages


def get_requirements(filepath):
    with open(file=filepath, mode="r") as file:
        return [line.strip() for line in file.readlines()]


requirements = get_requirements(filepath="requirements.txt")
test_requirements = get_requirements(filepath="test_requirements.txt")

setup(
    name="notex",
    version="0.0.1",
    include_package_data=True,
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    tests_require=test_requirements,
    extras_require={"dev": test_requirements},
    entry_points={"console_scripts": ["notex=notex.commands:main"]},
)
