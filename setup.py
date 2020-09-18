import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="sabrute",
    version="1.1.2",
    authors="rmdlv",
    author_email="ksdgdfjhgaskfgdjsgf@mail.ru",
    description="Программа для подбора паролей SAMP Mobile",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/rmdlv/sabrute",
    packages=["sabrute"],
    entry_points={"console_scripts": ["sabrute=sabrute.sabrute:main"]},
    license="Mozilla Public License 2.0",
    keywords="samp mobile bruteforce",
    project_urls={
        "GitHub":
        "https://github.com/rmdlv/sabrute",
        "Documentation":
        "https://github.com/rmdlv/sabrute/blob/master/README.md",
    },
    python_requires=">=3.6",
    install_requires=["aiohttp", "selenium"]
)