import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moodlexport", # Replace with your own username
    version="0.0.2",
    author="Guillaume Garrigos",
    author_email="guillaume.garrigos@lpsm.paris",
    description="A package to export test questions into Moodle from python or latex",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Guillaume-Garrigos/moodlexport",
    packages=['moodlexport', 'xmltodict', 'texsoup',],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)