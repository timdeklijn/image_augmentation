from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'Readme.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="im_augment",
    version="0.0",
    description="Image augmentation functionality",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url="To be added",
    author="TIm de Klijn",
    author_email="timdeklijn@gmail.com",
    license="MIT",
    packages=["im_augment"],
    install_requires=["matplotlib", "Pillow"],
    zip_safe=False,
)
