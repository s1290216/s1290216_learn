import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = s1290216_learn,
    version = 1.0.0,
    description = 'This is homework',
    long_description = long_description,
    author = s1290216,
    url = 'https://github.com/s1290216/s1290216_learn',
    packages = setuptools.find_packages(),
    classifiers = {
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    },
    license = 'GPLv3',
    long_description_content_type = 'text/markdown',
    install_requires = {
        'psutil',
        'pandas',
        'plotly',
        'matplotlib',
        'resource',
        'validators',
        'urllib3',
        'Pillow',
        'numpy',
        'pami',
    },
    python_requires = '>=3.5',
)