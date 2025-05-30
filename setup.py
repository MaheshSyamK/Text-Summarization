import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

setup(
    name="TextSummarizer",
    version="0.1",
    author="K. Mahesh Syam Kumar",
    author_email="maheshkondapalli5@gmail.com",
    description="A deep learning project for summarizing text using NLP models like RNN, LSTM, or Transformers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaheshSyamK/Text-Summarization.git",
    package_dir={"": "src"}, 
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.8',
)
 