from distutils.core import setup

#Read the contents of README.md for Project Description
def readme():
    with open("README.md") as f:
        README = f.read()
    return README

setup(
    name = 'Topsis_Taranpreet_102017050',
    packages = ['Topsis_Taranpreet_102017050'],
    version = '0.4',
    license='MIT',
    description = 'Topsis implementation',
    long_description = readme(),
    long_description_content_type = "text/markdown",
    author = 'Taranpreet Kaur Dhiman',
    author_email = 'taranpreet391@gmail.com',
    url = 'https://github.com/thetarandhiman/Topsis_Taranpreet_102017050',
    download_url = 'https://github.com/thetarandhiman/Topsis_Taranpreet_102017050/archive/refs/tags/v.0.4.tar.gz',
    keywords = ['TOPSIS', 'RANKING', 'PERFORMANCE'],
    install_requires=[ 
        'pandas',
        'numpy',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
