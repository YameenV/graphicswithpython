from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="GraphicswithPython",
    version="0.0.7",
    description="Graphic With Python (GWP) is a user-friendly and simpler way to practise and imply Computer Graphic Concept . It is better then graphics.h as GWP is faster & easy to implement. The Aim for this library is to make Computer Graphic Visualization easier and understandable by providing Fuction for each Method and support.",
    py_modules=["graphicswithpython"],
    package_dir={"": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/YameenV/graphicswithpython.git",
    author="Yameen Vinchu, Ashutosh Upadhyay",
    author_email="yameenvinchu38@gmail.com, ashutosh.aku.aau@gmail.com",

    install_requires = [
        "pygame ~= 2.1.0",
    ]
)