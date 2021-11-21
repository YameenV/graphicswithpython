from setuptools import setup


setup(
    name="GraphicswithPython",
    version="0.0.1",
    description="Say hello!",
    py_modules=["graphicswithpython"],
    package_dir={"": "src"},
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/YameenV/graphicswithpython.git",
    author="Yameen Vinchu, Ashutosh Upadayeah",
    author_email="yameenvinchu38@gmail.com, ashutosh.aku.aau@gmail.com",

    install_requires = [
        "pygame ~= 2.1.0",
    ]
)