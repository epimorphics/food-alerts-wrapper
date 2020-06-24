import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="food-alerts-wrapper-drianclark",
    version="0.0.1",
    author="Adrian David",
    author_email="adrian.david@epimorphics.com",
    description="A python wrapper for the FSA food alerts API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/epimorphics/food-alerts-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
