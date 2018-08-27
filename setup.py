import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spamassassin_client",
    version="0.0.1",
    author="Peter Matkovski",
    author_email="p.matkovski@gmail.com",
    description="Wrapper for SpamAssassin SPAMC deamon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/petermat/spamassassin_client",
    packages=setuptools.find_packages(exclude=['tests*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
