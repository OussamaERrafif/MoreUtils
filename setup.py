from setuptools import setup, find_packages

setup(
    name='moreutils',        # Name of your package
    version='0.1',                  # Package version
    description='A collection of utility functions for text, and conversions',
    author='Oussama Errafif',
    author_email='Oussamaerra2002@gmail.com',
    url='https://github.com/OussamaERrafif/MoreUtils',  # GitHub repo link
    packages=find_packages(),       # Automatically find and include all modules in the package
    install_requires=[
        'numpy', 'pandas', 'matplotlib', 'scikit-learn', 'seaborn', 'nltk', 'scipy', 'tqdm', 'torch', 'torchvision', 'transformers', 'sentencepiece', 'tensorflow', 'keras', 'gensim', 'spacy', 'stanza', 'beautifulsoup4', 'requests', 'flask', 'fastapi', 'uvicorn', 'streamlit', 'dash', 'plotly', 'bokeh', 'dash-bootstrap-components', 'dash-core-components', 'dash-html-components', 'dash-renderer', 'dash-table', 'dash-daq', 'dash-cytoscape', 'dash-canvas', 'dash-uploader', 'dash-extensions', 'dash-leaflet', 'dash-geoplot', 'dash-bio', 'dash-bio-utils', 'dash-cytoscape'
    ],            
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',        
)
