from setuptools import setup , find_packages

setup(name='namizun_core',
      version='1.3.8',
      description='namizun main functions',
      author='MalKeMit',
      author_email='khodemalkemit@gmail.com',
      packages=find_packages(include=['psutil==5.9.4',
                        'redis==4.3.5',
                        'pytz==2022.6']),
      [tool.setools]
      packages = [
          { include = "database" },
          { include = "udp" },
          # Add other packages as needed
      ]
      url='https://github.com/Arman19891006/namizun',
      setup_requires=['wheel'],
      install_requires=['psutil==5.9.4',
                        'redis==4.3.5',
                        'pytz==2022.6']
      )
