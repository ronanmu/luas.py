from distutils.core import setup

setup(
    name = 'luas.py',
    version = '0.1',
    packages = ['luas', 'luas.models'],
    url = 'https://github.com/ronanmu/luas.py',
    download_url = 'https://github.com/ronanmu/luas.py/tarball/0.1',
    license = 'MIT',
    requires=['requests'],
    author = 'Ronan Murray',
    author_email = 'ronanmu@users.noreply.github.com',
    description = 'Python module for interacting with Dublin Luas real-time API',
    keywords = ['luas', 'transport', 'dublin', 'ireland', 'tram'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
    ]
)
