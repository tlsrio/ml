from setuptools import setup, find_packages

requires = []

setup(
    name="NLP API",
    version="0.0",
    description="NLP Text Summarization API",
    author="Malcolm Yeh and Zayaan Moez",
    author_email="anon@email.com",
    keywords="flask REST NLP",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
