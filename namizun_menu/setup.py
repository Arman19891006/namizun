from setuptools import setup

setup(name='namizun_menu',
      version='1.0.0',
      description='namizun menu',
      author='MalKeMit',
      author_email='khodemalkemit@gmail.com',
      url='https://github.com/malkemit/namizun',
      setup_requires=['wheel'],
      [build-system]
      requires = ["setuptools", "wheel"]
      build-backend = "setuptools.build_meta"
      
      [tool.setools]
      packages = [
            { include = "database" },
            { include = "udp" },
            { include = "time" },
            { include = "log" },
            { include = "network" },
            { include = "ip" }
      ]

      install_requires=['colored~=1.4.4',
                        'pyfiglet~=0.8.post1',
                        'prettytable~=3.5.0']
      )
