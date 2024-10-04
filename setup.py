from setuptools import setup, find_packages

setup(
    name='moreutils',        # Name of your package
    version='0.1',                  # Package version
    description='A collection of utility functions for text, and conversions',
    author='Oussama Errafif',
    author_email='Oussamaerra2002@gmail.com',
    url='https://github.com/yourusername/my_utils_package',  # GitHub repo link
    packages=find_packages(),       # Automatically find and include all modules in the package
    install_requires=[],            # List dependencies here, if any
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',        # Minimum Python version requirement
)
