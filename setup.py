from setuptools import setup

setup(name='sony-headphones-control',
      version='0.1',
      description='Control sony headphones noise cancelling modes',
      url='',
      author='Ivan Pankratov',
      author_email='im.pankratov@ya.ru',
      license='MIT',
      packages=['sony-headphones-control'],
      install_requires=[
          'PyBluez',
      ],
      zip_safe=False)
