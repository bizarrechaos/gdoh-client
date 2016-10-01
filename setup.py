from setuptools import setup


setup(
    name='gdoh-client',
    version='1.0',
    author='bizarrechaos',
    packages=['gdoh'],
    license='Apache License Version 2.0',
    description='Libraries and command line tool for Google\'s DNS-over-HTTPS',
    install_requires=['docopt==0.6.2',
                      'requests==2.11.1',
                      'prettytable==0.7.2'],
    url='https://github.com/bizarrechaos/gdoh-client',
    entry_points='''
        [console_scripts]
        gdoh = gdoh.__main__:main
    '''
)
