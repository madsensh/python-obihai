import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="obihai",
    version="0.0.1",
    author="Shannon Madsen",
    author_email="shannon.madsen@gmail.com",
    description="Small package for reading status from Obihai VOIP gateways such as Obi202",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madsensh/python-obihai",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)