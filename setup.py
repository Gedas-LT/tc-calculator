import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calculator",
    version="0.0.1",
    author="Gediminas Šimavičius",
    author_email="gediminas.simavicius@gmail.com",
    description="Package for basic mathematical functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gedas-LT/tc-calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)