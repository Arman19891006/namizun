from setuptools import setup

setup(name='namizun_menu',
      version='1.0.0',
      description='namizun menu',
      author='MalKeMit',
      author_email='khodemalkemit@gmail.com',
      url='https://github.com/malkemit/namizun',
      packages=find_packages(include=['psutil==5.9.4',
                        'redis==4.3.5',
                        'pytz==2022.6']),
      [build-system]
      requires = ["setuptools", "wheel"]
      build-backend = "setuptools.build_meta"
      
      [tool.setools]
      py_modules = ["database", "udp", "time", "log", "network", "ip"]

      install_requires=['colored~=1.4.4',
                        'pyfiglet~=0.8.post1',
                        'prettytable~=3.5.0']
      )
