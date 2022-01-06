from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='hek',
  version='0.1.0',
  description='first version of hek',
  long_description=open('README.txt').read(),
  url='https://github.com/greedalbadi/hek',
  author='greed albadi',
  author_email='greedalbadi@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='none',
  packages=find_packages(),
  install_requires=['pillow']
)