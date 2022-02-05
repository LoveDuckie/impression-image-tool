import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="impression-image-tool-loveduckie",
    version="0.0.1",
    author="Luc Shelton",
    author_email="lucshetlon@gmail.com",
    description="A simple tool for generating impression images for blog posts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LoveDuckie/impression-image-tool",
    project_urls={
        "Bug Tracker": "https://github.com/LoveDuckie/impression-image-tool/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)