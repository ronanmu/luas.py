import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'luas.py',
    version = '0.3.3',
    packages = setuptools.find_packages(),
    url = 'https://github.com/ronanmu/luas.py',
    download_url = 'https://github.com/ronanmu/luas.py/tarball/0.3.3',
    license = 'MIT',
    requires=['requests'],
    author = 'Ronan Murray',
    author_email = '2470586+ronanmu@users.noreply.github.com',
    description = 'Python module for interacting with Dublin Luas real-time API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords = ['luas', 'transport', 'dublin', 'ireland', 'tram'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
    ]
)
