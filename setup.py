from setuptools import setup, find_packages

setup(
    name='plotsh',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'configparser'
    ],
    entry_points={
        'console_scripts': [
            'plot=plotsh.main:main'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='AI helper for DevOps using OpenAI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://plot.sh',
)
