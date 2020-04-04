from setuptools import setup

setup(name='SonyHeadphonesControl',
      version='0.1',
      description='Control sony headphones noise cancelling modes',
      url='',
      author='Ivan Pankratov',
      author_email='im.pankratov@ya.ru',
      license='GPL',
      packages=['SonyHeadphonesControl'],
      scripts=['bin/sony-headphones-control'],
      install_requires=[
          'PyBluez',
      ],
      zip_safe=False)
