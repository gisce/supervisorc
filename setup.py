from setuptools import setup, find_packages


setup(
    name='supervisorc',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/gisce/supervisorc',
    install_requires=[],
    license='MIT',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    description='A high level api for XML-RPC supervisor server',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
    ]
)