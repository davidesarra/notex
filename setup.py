import setuptools


NAME = "notex"
VERSION = "0.0.1"
AUTHOR = "Davide Sarra"
URL = "https://github.com/davidesarra/notex"
DESCRIPTION = "Turning markdown notes with formulas into LaTeX PDFs "
LICENSE = "MIT"
CLASSIFIERS = [
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Development Status :: 3 - Alpha ",
]
KEYWORDS = "markdown latex pdf python cli app"

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()


def get_requirements(filepath):
    with open(file=filepath, mode="r") as file:
        return [line.strip() for line in file.readlines()]


REQUIREMENTS = get_requirements(filepath="requirements.txt")
TEST_REQUIREMENTS = get_requirements(filepath="test_requirements.txt")

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    url=URL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires="~=3.6",
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    extras_require={"dev": TEST_REQUIREMENTS},
    entry_points={"console_scripts": ["notex=notex.commands:main"]},
)
