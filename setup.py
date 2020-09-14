import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="sabrute",
    version="1.0.4",
    author="rmdlv",
    description="Программа для подбора паролей SAMP Mobile",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/rmdlv/sabrute",
    packages=setuptools.find_packages(),
    license="Mozilla Public License 2.0",
    keywords="samp mobile bruteforce",
    classifiers=[
        "Development Status :: 1 - In Dev",
        "Programming Language :: Python :: >=3.6",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "GitHub":
        "https://github.com/rmdlv/sabrute",
        "Documentation":
        "https://github.com/rmdlv/sabrute/blob/master/README.md",
    },
    python_requires=">=3.6",
    install_requires=["aiohttp", "selenium"],
)