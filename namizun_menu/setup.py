from setuptools import setup, find_packages

setup(
    name='namizun_menu',
    version='1.0.0',
    description='namizun menu',
    author='MalKeMit',
    author_email='khodemalkemit@gmail.com',
    url='https://github.com/malkemit/namizun',
    packages=find_packages(include=['database', 'udp', 'time', 'log', 'network', 'ip']),
    install_requires=[
        'colored~=1.4.4',
        'pyfiglet~=0.8.post1',
        'prettytable~=3.5.0'
    ],
)
