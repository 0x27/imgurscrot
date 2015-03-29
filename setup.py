from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="imgurscrot",
    version="0.1.0",
    description="imgur/scrot screengrabber/uploader",
    license="MIT",
    author="David Davidson",
    packages=find_packages(),
    install_requires=['pyscreenshot', 'requests'],
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'imgurscrot=imgurscrot:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
