from setuptools import setup, find_packages

setup(
    name='plotshell',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'configparser',
        'distro',
        'rich'
       
    ],
    entry_points={
        'console_scripts': [
            'plot=plot.main:main'
        ]
    },
    author='Sajith Amma',
    author_email='sajith@tshaped.in',
    description='AI helper for DevOps using OpenAI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://plot.sh',
)
