
from setuptools import setup, find_packages

# Read README for long description
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='MyTColor',
    version='1.0.1',
    author='Zidan IDz',
    author_email='zeyshyy@gmail.com',
    description='Simple, Fast, Zero-Dependency Terminal Coloring',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zidan-idz/MyTColor',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Terminals',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'myt=MyTColor.__main__:main',
        ],
    },
)
