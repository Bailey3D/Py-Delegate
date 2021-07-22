import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="delegate",
    version="0.0.1",
    author="Bailey3D",
    author_email="contact@bailey3d.com",
    description="Package for delegate based methods via decorators",
    long_description=long_description,
    url="https://github.com/BhMbOb/Py-Delegate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)